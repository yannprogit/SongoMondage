from flask import Blueprint, request
from controllers.reponse_controller import ReponseController
from controllers.connexion_controller import ConnexionController

reponse_blueprint = Blueprint('reponse', __name__)

@reponse_blueprint.route("/sondages/<string:id>/reponse", methods=['POST'], endpoint='post_reponse')
@ConnexionController.auth_middleware
def post_reponse_route(id):
    return ReponseController.add_reponse(id, request.get_json())

@reponse_blueprint.route("/sondages/<string:id>/reponses", methods=['GET'], endpoint='get_reponses')
@ConnexionController.auth_middleware
def get_reponses_route(id):
    return ReponseController.get_reponses(id) 

@reponse_blueprint.route("/sondages/<string:sondage_id>/reponses/<string:id>", methods=['GET'], endpoint='get_reponse')
@ConnexionController.auth_middleware
def get_reponse_route(id, sondage_id):
    return ReponseController.get_reponse(id, sondage_id) 