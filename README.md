// Task Manager API

A simple Task Manager web application built with Django.

Features

  Add a task
  
  View all tasks
  
  Mark a task as completed or pending
  
  Delete a task
  
  SQLite database

Technologies

  Python
  
  Django
  
  SQLite
  
  HTML

// Project Structure

TaskManager_API/
│
├── manage.py
├── db.sqlite3
│
├── taskproject/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── tasks/
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── views.py
    ├── urls.py
    └── templates/
        └── tasks/
            └── home.html

Installation

Clone the project:

git clone https://github.com/Sanika-More-15/TaskManager_API.git
cd TaskManager_API

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Install the required packages:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Start the server:

python manage.py runserver

Open:

http://127.0.0.1:8000/

Usage

Open the home page, enter a task title and description, and click Add Task.

You can then use Toggle to change the task status and Delete to remove a task.
