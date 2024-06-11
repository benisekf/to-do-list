from flask import Blueprint, render_template
from app.models import Task
bp = Blueprint('main', __name__)
@bp.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)
