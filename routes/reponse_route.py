from flask import Blueprint, request
from controllers.reponse_controller import ReponseController
from controllers.connexion_controller import ConnexionController

reponse_blueprint = Blueprint('reponse', __name__)

@reponse_blueprint.route("/sondages/<string:id>/reponse", methods=['POST'], endpoint='post_reponse')
@ConnexionController.auth_middleware
def post_reponse_route(id):
    return ReponseController.add_reponse(id, request.get_json())