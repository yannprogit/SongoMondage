from flask import Blueprint, request
from controllers.utilisateur_controller import UtilController
from controllers.connexion_controller import ConnexionController

util_blueprint = Blueprint('utilisateur', __name__)

@util_blueprint.route("/inscription", methods=['POST'])
def post_util_route():
    return UtilController.add_util(request.get_json())

@util_blueprint.route("/utilisateurs/<string:id>", methods=['GET'], endpoint='get_util')
@ConnexionController.auth_middleware
def get_util_route(id):
    return UtilController.get_util(id) 