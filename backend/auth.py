from flask_restx import Resource, Namespace, fields
from models import Usuarios
from flask_jwt_extended import (JWTManager, create_access_token,create_refresh_token, get_jwt_identity,jwt_required)
from flask import Flask,request, jsonify, make_response


auth_ns=Namespace('auth', description="A Namespace for out Authentication")

login_model=auth_ns.model(
     "Login",
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

          Usuario=data.get("usuario")
          Contrasena=data.get("contrasena")

          db_user=Usuarios.query.filter_by(usuario=Usuario).first()


          if db_user and (Contrasena==Contrasena) :

               access_token=create_access_token(identity=Usuario)
               refresh_token=create_refresh_token(identity=Usuario)

               return jsonify(
                     {
                           "access_token":access_token,"refresh_token":refresh_token
                     }
               )
          else:
               return jsonify({"message":"Invalid username or password"})
          
@auth_ns.route('/refresh')
class RefreshResource(Resource):
     @jwt_required(refresh=True)
     def post(self):
          current_user=get_jwt_identity()

          new_access_token=create_access_token(identity=current_user)
          return make_response(jsonify({"access_token":new_access_token}),200)