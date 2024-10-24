from flask_restx import Namespace, Resource, fields
from models import Solares
from flask_jwt_extended import JWTManager, create_access_token,create_refresh_token, jwt_required
from flask import Flask,request, jsonify


solares_ns=Namespace("solares", description="A namespace for solares")


solares_model=solares_ns.model(
     "Solares",
     {
        "idSolar":fields.Integer(),
        "NombreFinca":fields.String(),
        "Calle":fields.String(),
        "nCalle":fields.String(),
        "Puerta":fields.String()
     }
)

@solares_ns.route('/hello')
class HelloResource(Resource):
    def get(self):
        return {"message":"Hello World"}
   
@solares_ns.route('/solares')
class SolaresResource(Resource):
    
    @solares_ns.marshal_list_with(solares_model)
    def get(self):
          """Obtiene todos los solares"""
          solares=Solares.query.all()

          return solares

    @solares_ns.marshal_with(solares_model)
    @solares_ns.expect(solares_model)
    @jwt_required()
    def post(self):
        """Crear un nuevo solar"""
        data=request.get_json()

        new_solar=Solares(
            NombreFinca = data.get('NombreFinca'),
            Calle = data.get('Calle'),
            nCalle = data.get('nCalle'),
            Puerta = data.get('Puerta'),
            Extension = data.get('Extension')
        )

        new_solar.save()
        return new_solar, 201

@solares_ns.route('/solar/<int:idSolar>')
class SolarResource(Resource):
     @solares_ns.marshal_with(solares_model)
     def get(self, idSolar):
          """Obtiene un solar por id"""
          solar=Solares.query.get_or_404(idSolar)
          return solar
          
     @solares_ns.marshal_with(solares_model)
     @jwt_required()
     def put(self, idSolar):
          """Actualiza un solar por id"""
          solar_to_update=Solares.query.get_or_404(idSolar)

          data=request.get_json()

          solar_to_update.update(
                        data.get('NombreFinca'),
                        data.get('Calle'),
                        data.get('nCalle'),
                        data.get('Puerta'),
                        data.get('Extension')
          )
          return solar_to_update, 200

     @solares_ns.marshal_with(solares_model)
     @jwt_required()
     def delete(self,idSolar):
          """Elimina un solar por id"""
          solar_to_delete=Solares.query.get_or_404(idSolar)
          solar_to_delete.delete()
          return {"message":"Solar eliminado"}, 204