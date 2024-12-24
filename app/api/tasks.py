from flask import Blueprint, request, jsonify
from app.models.task import Task  # اطمینان حاصل کنید که مدل Task به درستی وارد شده است
from app import db  # پایگاه داده

# تعریف بلوپرینت
task_bp = Blueprint('tasks', __name__)

@task_bp.route('/', methods=['POST'])  # فقط متد POST مجاز است
def create_task():
    data = request.get_json()
    user_id = data.get('user_id')
    title = data.get('title')
    description = data.get('description')
    due_date = data.get('due_date')
    priority = data.get('priority', 'low')

    if not user_id or not title or not due_date:
        return jsonify({'message': 'اطلاعات اجباری وارد نشده است'}), 400

    task = Task(
        user_id=user_id,
        title=title,
        description=description,
        due_date=due_date,
        priority=priority,
    )
    db.session.add(task)
    db.session.commit()

    return jsonify({'message': 'وظیفه با موفقیت ایجاد شد'}), 201