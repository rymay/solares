from flask import Flask
from flask_restx import Api
from models import Solares, Usuarios
from exts import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from solares import solares_ns
from auth import auth_ns
from flask_cors import CORS

def create_app(config):
     app=Flask(__name__)

     app.config.from_object(config)

     db.init_app(app)

     migrate=Migrate(app, db)
     JWTManager(app)

     api=Api(app, doc='/docs')

     api.add_namespace(solares_ns)
     api.add_namespace(auth_ns)


     @app.shell_context_processor
     def make_shell_context():
          return{
               "db":db,
               "Solares":Solares,
               "Usuarios":Usuarios
          }

     return app