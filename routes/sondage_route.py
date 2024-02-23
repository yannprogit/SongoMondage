from flask import Blueprint, jsonify
from controllers.sondage_controller import SondageController

sondage_blueprint = Blueprint('sondage', __name__)

@sondage_blueprint.route("/sondages", methods=['GET'])
def get_sondages_route():
    sondages_result = SondageController.get_sondages()
    return jsonify(sondages_result)