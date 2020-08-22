from flask import request
from flask_restful import Resource
from Model import db, Paises, PaisesSchema
import json

paises_schema = PaisesSchema(many=True)
pais_schema = PaisesSchema()

class PaisesResource(Resource):
   @staticmethod
   def get():
      paises = Paises.query.all()
      paises = json.dumps(paises)
      return {'status': 'success', 'data': paises}, 200

   @staticmethod
   def post():
      json_data = request.get_json(force=True)
      if not json_data:
         return {'message': 'No hay informacion'}, 400
      # Validate and deserialize input
     response = json.dumps(json_data)
     data = pais_schema.loads(response)
     pais = Paises.query.filter_by(pai_id=data['pai_id']).first()
     if pais:
        return {'message': 'Pais ya existe'}, 400
     pais = Countries(
     pai_id=data['pai_id'],
     pai_nom=data['pai_nom']
     )
    db.session.add(pais)
    db.session.commit()
    result = pais_schema.dump(pais)
    return {"status": 'success', 'data': result}, 201