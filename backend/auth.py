from flask_restx import Resource, Namespace, fields
from models import Usuarios
from flask_jwt_extended import (JWTManager, create_access_token,create_refresh_token, jwt_required)
from flask import Flask,request, jsonify, make_response


auth_ns=Namespace('auth', description="A Namespace for out Authentication")

login_model=auth_ns.model(
     "Usuarios",
     {
          "usuario":fields.String(),
          "contrasena":fields.String()
     }
)
@auth_ns.route('/login')
class Login(Resource):
     @auth_ns.expect(login_model)
     def post(self):
          data=request.get_json()

          usuario=data.get("usuario")
          contrasena=data.get("contrasena")

        
          db_user=Usuarios.query.filter_by(usuario=usuario).first()


          if db_user and (contrasena==contrasena) :

               access_token=create_access_token(identity=usuario)
               refresh_token=create_refresh_token(identity=usuario)

               return jsonify(
                     {
                           "access_token":access_token,"refresh_token":refresh_token
                     }
               )
          else:
               return jsonify({"message":"Invalid username or password"})