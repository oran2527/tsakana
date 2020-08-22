from flask import request, render_template, make_response
from flask_restful import Resource

class IndexResource(Resource):
   @staticmethod
   def get():
   headers = {'Content-Type': 'text/html'}
   return make_response(render_template('main.html'),200,headers)

class AddPais(Resource):
   @staticmethod
   def get():
   headers = {'Content-Type': 'text/html'}
   return make_response(render_template('addPais.html'),200,headers)