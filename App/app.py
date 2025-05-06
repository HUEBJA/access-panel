from flask import Flask, redirect, url_for, request, session, render_template
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
import hashlib

app = Flask(__name__)
app.secret_key = 'dein_geheimer_schluessel'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webapp.db'
db = SQLAlchemy(app)

# Datenbankmodelle
class User(db.Model):
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    group = db.Column(db.String(80), db.ForeignKey('gruppe.name'))

class Gruppe(db.Model):
    name = db.Column(db.String(80), primary_key=True)

class App(db.Model):
    name = db.Column(db.String(80), primary_key=True)
    url = db.Column(db.String(200), nullable=False)

class AppGruppeZuweisung(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gruppe_name = db.Column(db.String(80), db.ForeignKey('gruppe.name'))
    app_name = db.Column(db.String(80), db.ForeignKey('app.name'))

# Decorators
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if session.get('role') != 'admin':
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated

from flask import render_template  # falls noch nicht importiert

@app.route('/')
@login_required
def dashboard():
    username = session['user']
    role = session['role']
    user = User.query.get(username)
    if user is None:
        return redirect(url_for('logout'))

    gruppe = user.group
    app_links = []

    if gruppe:
        zuweisungen = AppGruppeZuweisung.query.filter_by(gruppe_name=gruppe).all()
        for z in zuweisungen:
            app = App.query.get(z.app_name)
            if app:
                app_links.append((app.name, app.url))

    return render_template("dashboard.html", username=username, role=role, app_links=app_links)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        user = User.query.get(username)
        if user and user.password == password:
            session['user'] = username
            session['role'] = user.role
            return redirect(url_for('dashboard'))
        error = "Login fehlgeschlagen"
    return render_template("login.html", error=error)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/admin', methods=['GET', 'POST'])
@admin_required
def admin():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add_app' and not App.query.get(request.form['appname']):
            db.session.add(App(name=request.form['appname'], url=request.form['appurl']))
        elif action == 'add_group' and not Gruppe.query.get(request.form['groupname']):
            db.session.add(Gruppe(name=request.form['groupname']))
        elif action == 'add_user' and not User.query.get(request.form['username']):
            pw = hashlib.sha256(request.form['password'].encode()).hexdigest()
            db.session.add(User(username=request.form['username'], password=pw, role=request.form['role'], group=None))
        elif action == 'assign_user':
            user = User.query.get(request.form['username'])
            if user: user.group = request.form['usergroup']
        elif action == 'remove_user_from_group':
            user = User.query.get(request.form['username'])
            if user: user.group = None
        elif action == 'assign_app':
            exists = AppGruppeZuweisung.query.filter_by(gruppe_name=request.form['group'], app_name=request.form['app_to_group']).first()
            if not exists:
                db.session.add(AppGruppeZuweisung(gruppe_name=request.form['group'], app_name=request.form['app_to_group']))
        elif action == 'unassign_app':
            entry = AppGruppeZuweisung.query.filter_by(gruppe_name=request.form['group'], app_name=request.form['app_to_group']).first()
            if entry: db.session.delete(entry)
        elif action == 'delete_user':
            user = User.query.get(request.form['username'])
            if user: db.session.delete(user)
        elif action == 'delete_group':
            group = Gruppe.query.get(request.form['groupname'])
            if group: db.session.delete(group)
        elif action == 'delete_app':
            app = App.query.get(request.form['appname'])
            if app: db.session.delete(app)
        db.session.commit()

    users = User.query.all()
    groups = Gruppe.query.all()
    apps = App.query.all()
    assignments = AppGruppeZuweisung.query.all()

    return render_template("admin.html", users=users, groups=groups, apps=apps, assignments=assignments)

    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not User.query.get('admin'):
            db.session.add(User(username='admin', password=hashlib.sha256("adminpass".encode()).hexdigest(), role='admin', group=None))
            db.session.commit()
    app.run(debug=True)
