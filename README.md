# access-panel

🗣️ *This README is available in both **English** and **German** – see below.*

---

## 🇬🇧 English

### What is *access-panel*?

**access-panel** is a modern, role-based web dashboard for managing users, groups, and app access – built with Flask and SQLAlchemy.

This project was originally written in **German**, but it is structured in a way that makes switching to **English very easy**. Labels, placeholders, and interface text can be translated with minimal effort.

---

### 🔐 Default Admin Login

* **Username:** `admin`
* **Password:** `adminpass`

---

### 📋 Description

**access-panel** is a simplified but extendable web application that allows administrators to:

* Create and delete users
* Assign users to groups
* Create and remove groups
* Register apps (URLs)
* Assign apps to groups

Users only see apps that belong to the group they're assigned to.

The system includes a session-based login, role checks (`admin` vs. `user`), and a clean user interface inspired by Apple's light-mode design.

> **Note:** Some routes may currently reject requests – this is a known issue and can be fixed with further backend adjustments. Contributions are welcome.

---

### 🛠️ Built With

* Python 3 / Flask
* SQLAlchemy (with SQLite)
* HTML/CSS (no JS frameworks)
* Jinja2 templates

---

### 🚀 Status

This is a **simplified prototype**, intended as a base for production-ready access control tools. You're welcome to use, extend, and improve it for your own projects.

---

## 🇩🇪 Deutsch

### Was ist *access-panel*?

**access-panel** ist ein modernes, rollenbasiertes Web-Dashboard zur Verwaltung von Benutzern, Gruppen und App-Zugängen – entwickelt mit Flask und SQLAlchemy.

Dieses Projekt wurde ursprünglich auf **Deutsch** geschrieben, lässt sich aber mit **minimalem Aufwand ins Englische** übersetzen. Die Beschriftungen und Texte im Frontend können schnell angepasst werden.

---

### 🔐 Standard-Admin-Login

* **Benutzername:** `admin`
* **Passwort:** `adminpass`

---

### 📋 Beschreibung

**access-panel** ist eine vereinfachte, aber erweiterbare Webanwendung, mit der Administratoren:

* Benutzer erstellen und löschen können
* Benutzer Gruppen zuweisen
* Gruppen verwalten
* Webanwendungen registrieren (URLs)
* Apps bestimmten Gruppen zuweisen

Benutzer sehen nur die Anwendungen, die ihrer Gruppe zugewiesen wurden.

Das System bietet eine loginbasierte Sitzungsverwaltung, Rollentrennung (`admin` vs. `user`) und ein benutzerfreundliches Interface – optisch angelehnt an Apples Light-Mode.

> **Hinweis:** Manche Seiten reagieren aktuell nicht korrekt auf Anfragen – dies ist bekannt und kann durch kleinere Backend-Anpassungen behoben werden. Beiträge zur Verbesserung sind sehr willkommen.

---

### 🛠️ Verwendete Technologien

* Python 3 / Flask
* SQLAlchemy (mit SQLite)
* HTML/CSS (ohne JavaScript-Frameworks)
* Jinja2-Templates

---

### 🚀 Projektstatus

Dies ist eine **vereinfachte Version**, gedacht als Basis für produktiv nutzbare Zugriffskontrollsysteme. Es darf gerne genutzt, erweitert und in produktiven Umgebungen verbessert werden.

