from flask import Blueprint, redirect, url_for, request
from app import db
from app.models import Task
bp = Blueprint('task', __name__)
@bp.route('/add', methods=['POST'])
def add():
    description = request.form.get('description')
    new_task = Task(description=description)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('main.index'))
@bp.route('/complete/<int:task_id>')
def complete(task_id):
    task = Task.query.get(task_id)
    task.completed = True
    db.session.commit()
    return redirect(url_for('main.index'))
@bp.route('/delete/<int:task_id>')
def delete(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.index'))
