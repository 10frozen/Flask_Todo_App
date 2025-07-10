from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from app import db
from app.models import Task

tasks_bp = Blueprint('tasks', __name__)

def login_required(func):
    from functools import wraps
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash('Please login first.', 'warning')
            return redirect(url_for('auth.login'))
        return func(*args, **kwargs)
    return decorated_function

@tasks_bp.route('/')
@login_required
def view_tasks():
    user_id = session.get('user_id')
    tasks = Task.query.filter_by(user_id=user_id).all()
    return render_template('tasks.html', tasks=tasks)

@tasks_bp.route('/add', methods=['POST'])
@login_required
def add_task():
    title = request.form.get('title').strip()
    if title:
        new_task = Task(title=title, status='Pending', user_id=session.get('user_id'))
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully', 'success')
    else:
        flash('Task title cannot be empty.', 'danger')
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/toggle/<int:task_id>', methods=['POST'])
@login_required
def toggle_status(task_id):
    user_id = session.get('user_id')
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()

    if task:
        if task.status == 'Pending':
            task.status = 'Working'
            db.session.commit()
            flash("Task marked as Working.", 'info')

        elif task.status == 'Working':
            task.status = 'Done'
            db.session.commit()
            flash("Task marked as Done.", 'success')

        elif task.status == 'Done':
            db.session.delete(task)
            db.session.commit()
            flash("Task completed and deleted.", 'success')

    else:
        flash('Task not found or unauthorized.', 'danger')

    return redirect(url_for('tasks.view_tasks'))


@tasks_bp.route('/clear', methods=['POST'])
@login_required
def clear_tasks():
    user_id = session.get('user_id')
    Task.query.filter_by(user_id=user_id).delete()
    db.session.commit()
    flash('All your tasks cleared.', 'info')
    return redirect(url_for('tasks.view_tasks'))
