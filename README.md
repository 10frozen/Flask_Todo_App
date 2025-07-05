# 📝 Flask To-Do App

A clean, responsive, and lightweight To-Do list web application built with **Flask**, **MySQL**, and **HTML/CSS/JS**. It includes user authentication, task tracking, and modern UI styling.

---

## 🚀 Features

- ✅ User Login & Logout
- ✅ New User Registration
- ✅ Add, View, Toggle, and Clear Tasks
- ✅ Flash messages for feedback
- ✅ Mobile-responsive UI (CSS + JS)
- ✅ Password visibility toggle (JS)
- ✅ MySQL database integration with SQLAlchemy

---

## 📁 Project Structure

TODO_APP/
├── app/
│ ├── routes/
│ │ ├── init.py
│ │ ├── auth.py
│ │ └── tasks.py
│ ├── static/
│ │ ├── css/
│ │ │ └── style.css
│ │ └── js/
│ │ └── main.js
│ ├── templates/
│ │ ├── base.html
│ │ ├── login.html
│ │ ├── register.html
│ │ └── tasks.html
│ ├── models.py
│ └── init.py
├── venv/
├── run.py
└── README.md

---

## ⚙️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL (via SQLAlchemy)
- **Templates**: Jinja2
- **ORM**: SQLAlchemy

---
## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/todo-flask-app.git
cd todo-flask-app
--Create & Activate Virtual Environment
1.python -m venv venv
2.source venv/bin/activate  # On Windows: venv\Scripts\activate
3.pip install -r requirements.txt
4.pip install flask flask_sqlalchemy pymysql

 Set Up MySQL Database
*Create a database named bcaflask in MySQL:
CREATE DATABASE bcaflask;

*Update DB credentials in app/__init__.py if needed:
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/bcaflask'

*Run the App
python run.py
Visit: http://127.0.0.1:5000/
