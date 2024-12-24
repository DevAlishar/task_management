from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.api.tasks import task_bp
import app
app.register_blueprint(task_bp, url_prefix='/api/v1/tasks')
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)
    migrate.init_app(app, db)

    from app.api.users import user_bp
    from app.api.tasks import task_bp  #طمینان حاصل کنید که این خط وجود دارد
    app.register_blueprint(user_bp, url_prefix='/api/v1/users')
    app.register_blueprint(task_bp, url_prefix='/api/v1/tasks')

    @app.route('/')
    def index():
        return render_template('index.html')

    return app