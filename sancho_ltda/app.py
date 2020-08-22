from flask import Blueprint
from flask_restful import Api
from resources.Paises import PaisesResource
from resources.TemplateRender import IndexResource, AddPais

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
template_bp = Blueprint('template', __name__)
template = Api(template_bp)
# Route
template.add_resource(IndexResource, '/')
template.add_resource(AddPais, 'addPais')
api.add_resource(UserResource, '/Paises')