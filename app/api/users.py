from flask import Blueprint, request, jsonify, render_template  # برای مدیریت مسیرها و درخواست‌ها
from app.models.user import User  # مدل کاربر
from app import db  # پایگاه داده

user_bp = Blueprint('users', __name__)  # تعریف بلوپرینت برای مسیرهای مدیریت کاربران

@user_bp.route('/register', methods=['GET'])
def show_register_form():
    return render_template('register.html') 

@user_bp.route('/register', methods=['POST'])
def register():
    """
    مسیر برای ثبت‌نام کاربر جدید.
    """
    data = request.get_json()
    email = data.get('email')  
    password = data.get('password')  # گرفتن رمز عبور کاربر

    # بررسی وجود ایمیل و رمز عبور
    if not email or not password:
        return jsonify({'message': 'ایمیل و رمز عبور اجباری است'}), 400

    # بررسی عدم وجود کاربر با این ایمیل
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'این ایمیل قبلاً ثبت شده است'}), 400

    # ایجاد کاربر جدید
    user = User(email=email)
    user.set_password(password)  # هش کردن رمز عبور

    db.session.add(user)  # افزودن کاربر به پایگاه داده
    db.session.commit()  # ذخیره تغییرات در پایگاه داده

    return jsonify({'message': 'کاربر با موفقیت ثبت شد'}), 201