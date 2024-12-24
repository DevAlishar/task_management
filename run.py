from app import create_app  # وارد کردن تابع ساخت برنامه

app = create_app()  # ایجاد برنامه با تنظیمات پیش‌فرض

if __name__ == '__main__':
    app.run(debug=True)  # اجرای برنامه در حالت اشکال‌زدایی
