from app import db

class Task(db.Model): 
    """
    مدل مربوط به وظایف کاربران.
    """
    id = db.Column(db.Integer, primary_key=True)  # شناسه منحصر به فرد وظیفه
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # ارتباط با کاربر
    title = db.Column(db.String(120), nullable=False)  # عنوان وظیفه
    description = db.Column(db.Text, nullable=True)  # توضیحات وظیفه
    due_date = db.Column(db.Date, nullable=False)  # تاریخ مهلت وظیفه
    status = db.Column(db.String(50), nullable=False, default='pending')  # وضعیت وظیفه
    priority = db.Column(db.String(50), nullable=False, default='low')  # اولویت وظیفه

    user = db.relationship('User', backref=db.backref('tasks', lazy=True))  # ارتباط با مدل کاربر
