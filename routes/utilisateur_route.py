from flask import Blueprint, request
from controllers.utilisateur_controller import UtilController

util_blueprint = Blueprint('utilisateur', __name__)

@util_blueprint.route("/inscription", methods=['POST'])
def post_util_route():
    return UtilController.add_util(request.get_json())