from flask import Flask  # وارد کردن کلاس Flask برای ساخت برنامه وب
from flask_sqlalchemy import SQLAlchemy  # برای تعامل با پایگاه داده
from flask_migrate import Migrate  # برای مدیریت مهاجرت پایگاه داده

# ایجاد نمونه‌هایی از افزونه‌های Flask
db = SQLAlchemy()  # نمونه‌ای از SQLAlchemy برای مدیریت مدل‌های پایگاه داده
migrate = Migrate()  # نمونه‌ای از Migrate برای مدیریت مهاجرت‌های پایگاه داده

def create_app():
    """
    تابعی برای ایجاد و پیکربندی برنامه Flask.
    """
    app = Flask(__name__)  # ساخت نمونه برنامه Flask

    # تنظیمات برنامه
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'  # آدرس پایگاه داده SQLite
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # غیرفعال کردن ویژگی‌های غیرضروری
    app.config['SECRET_KEY'] = 'your_secret_key'  # کلید رمزنگاری برای JWT

    # اتصال افزونه‌ها به برنامه
    db.init_app(app)  # اتصال پایگاه داده به برنامه
    migrate.init_app(app, db)  # اتصال مهاجرت پایگاه داده به برنامه

    # ثبت بلوپرینت‌های مسیرهای REST API
    from app.api.users import user_bp
    from app.api.tasks import task_bp
    app.register_blueprint(user_bp, url_prefix='/api/v1/users')  # مسیرهای مدیریت کاربران
    app.register_blueprint(task_bp, url_prefix='/api/v1/tasks')  # مسیرهای مدیریت وظایف

    return app  # بازگشت نمونه برنامه
