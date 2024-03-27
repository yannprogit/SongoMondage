from flask import Blueprint, request
from controllers.utilisateur_controller import UtilController
from controllers.connexion_controller import ConnexionController

util_blueprint = Blueprint('utilisateur', __name__)

@util_blueprint.route("/inscription", methods=['POST'])
def post_util_route():
    return UtilController.add_util(request.get_json())


@util_blueprint.route("/utilisateurs/names", methods=['GET'], endpoint='get_utils_names')
@ConnexionController.auth_middleware
def get_utils_names_route():
    return UtilController.get_utils_names() 