from flask import Flask
from flask_migrate import Migrate
from database import db
import logging
from config import BasicConfig
#Routes
from routes.carnes.carnes import appcarne
from routes.bebidas.bebidas import appbebida
from routes.carros.carros import appcarro
from routes.computadoras.computadoras import appcomputadora
from routes.panes.panes import apppan
from routes.errores.errores import apperror

app = Flask(__name__)
#Blueprints
app.register_blueprint(appcarne)
app.register_blueprint(appbebida)
app.register_blueprint(appcarro)
app.register_blueprint(appcomputadora)
app.register_blueprint(apppan)
app.register_blueprint(apperror)
app.config.from_object(BasicConfig)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)
logging.basicConfig(level=logging.DEBUG,filename="debug.log")