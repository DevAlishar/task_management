from flask import Blueprint, request, jsonify  # برای مدیریت مسیرها و درخواست‌ها
from app.models.task import Task  # مدل وظیفه
from app import db  # پایگاه داده

task_bp = Blueprint('tasks', __name__)  # تعریف بلوپرینت برای مسیرهای مدیریت وظایف

@task_bp.route('/', methods=['POST'])
def create_task():
    """
    مسیر برای ایجاد وظیفه جدید.
    """
    data = request.get_json()  # دریافت داده‌های JSON از درخواست
    user_id = data.get('user_id')  # شناسه کاربر
    title = data.get('title')  # عنوان وظیفه
    description = data.get('description')  # توضیحات وظیفه
    due_date = data.get('due_date')  # تاریخ مهلت وظیفه
    priority = data.get('priority', 'low')  # اولویت وظیفه (پیش‌فرض: کم)

    # بررسی اطلاعات اجباری
    if not user_id or not title or not due_date:
        return jsonify({'message': 'اطلاعات اجباری وارد نشده است'}), 400

    # ایجاد وظیفه جدید
    task = Task(
        user_id=user_id,
        title=title,
        description=description,
        due_date=due_date,
        priority=priority,
    )
    db.session.add(task)  # افزودن وظیفه به پایگاه داده
    db.session.commit()  # ذخیره تغییرات در پایگاه داده

    return jsonify({'message': 'وظیفه با موفقیت ایجاد شد'}), 201
