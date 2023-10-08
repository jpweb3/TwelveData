from flask import Flask
from flask_migrate import Migrate 
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from config import Config
from .blueprints.site.routes import site
from .blueprints.auth.routes import auth
from .models import login_manager, db

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(site)
app.register_blueprint(auth)

db.init_app(app)
migrate = Migrate(app, db)
CORS(app) 
