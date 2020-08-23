from flask import request
from flask_restful import Resource
from Model import db, Pais, PaisSchema
import json


paises_schema = PaisSchema(many=True)
pais_schema = PaisSchema()


class PaisResource(Resource):
    @staticmethod
    def get():
        paises = Pais.query.all()
        paises = json.dumps(paises)
        return {'status': 'success', 'data': paises}, 200
