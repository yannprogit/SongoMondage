from flask import Blueprint, request
from controllers.sondage_controller import SondageController
from controllers.connexion_controller import ConnexionController

sondage_blueprint = Blueprint('sondage', __name__)

@sondage_blueprint.route("/sondages", methods=['GET'], endpoint='get_sondages')
@ConnexionController.auth_middleware
def get_sondages_route():
    return SondageController.get_sondages() 

@sondage_blueprint.route("/mes_sondages", methods=['GET'], endpoint='get_mes_sondages')
@ConnexionController.auth_middleware
def get_mes_sondages_route():
    return SondageController.get_mes_sondages() 

@sondage_blueprint.route("/sondages", methods=['POST'], endpoint='post_sondage')
@ConnexionController.auth_middleware
def post_sondage_route():
    return SondageController.add_sondage(request.get_json())

@sondage_blueprint.route("/sondages/<string:id>", methods=['DELETE'], endpoint='delete_sondage')
@ConnexionController.auth_middleware
def delete_sondage_route(id):
    return SondageController.del_sondage(id)

@sondage_blueprint.route("/sondages/<string:id>", methods=['GET'], endpoint='get_sondage')
@ConnexionController.auth_middleware
def get_sondage_route(id):
    return SondageController.get_sondage(id) 

@sondage_blueprint.route("/sondages/<string:id>", methods=['PUT'], endpoint='update_sondage')
@ConnexionController.auth_middleware
def update_sondage_route(id):
    return SondageController.upd_sondage(id, request.get_json()) 