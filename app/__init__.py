from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
db = SQLAlchemy()
migrate = Migrate()
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    from app.routes.main_routes import bp as main_bp
    from app.routes.task_routes import bp as task_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(task_bp)
    return app
