from app import db  # برای تعامل با پایگاه داده
from flask_bcrypt import generate_password_hash, check_password_hash  # برای هش کردن و بررسی رمز عبور

class User(db.Model):  # تعریف مدل کاربر
    """
    مدل مربوط به کاربران سیستم.
    """
    id = db.Column(db.Integer, primary_key=True)  # شناسه منحصر به فرد برای هر کاربر
    email = db.Column(db.String(120), unique=True, nullable=False)  # ایمیل کاربر
    password_hash = db.Column(db.String(128), nullable=False)  # هش رمز عبور

    def set_password(self, password):
        """
        هش کردن رمز عبور و ذخیره آن در پایگاه داده.
        """
        self.password_hash = generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """
        بررسی صحت رمز عبور.
        """
        return check_password_hash(self.password_hash, password)