from flask import Blueprint, request
from controllers.connexion_controller import ConnexionController

connexion_blueprint = Blueprint('connexion', __name__)

@connexion_blueprint.route("/connexion", methods=['POST'])
def post_connexion_route():
    return ConnexionController.connexion(request.get_json())

@connexion_blueprint.route("/deconnexion", methods=['POST'])
def post_deconnexion_route():
    return ConnexionController.deconnexion()