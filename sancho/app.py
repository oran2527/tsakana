from flask import Blueprint
from flask_restful import Api
from resources.Pais import PaisResource
from resources.TemplateRender import AddPais


api_bp = Blueprint('api', __name__)
api = Api(api_bp)
template_bp = Blueprint('template', __name__)
template = Api(template_bp)


# Route
template.add_resource(AddPais, 'addPais')
api.add_resource(PaisResource, '/Pais')
