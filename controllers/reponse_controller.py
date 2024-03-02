from services.reponse_service import ReponseService
from services.sondage_service import SondageService
from flask import jsonify, request
from bson import ObjectId

class ReponseController:

    @staticmethod
    def add_reponse(sondage_id, data):
        sondage = SondageService.get_sondage(sondage_id)
        if sondage:
            reponse = {
                'sondage_id': ObjectId(sondage_id),
                'utilisateur_id': ObjectId(str(request.util_id)),
                'reponses': []
            }
            
            for reponse_data in data['reponses']:
                question_exist = any(str(question['_id']) == reponse_data['question_id'] for question in sondage['questions'])

                if question_exist:
                    reponse_item = {
                        '_id': ObjectId(reponse_data['question_id']),
                        'reponse': reponse_data['reponse']
                    }
                    reponse['reponses'].append(reponse_item)
            
            resultat = ReponseService.add_reponse(sondage_id, str(request.util_id), reponse)
            return jsonify({"sucess": resultat}), 200
        else:
            return jsonify({"sucess": False, "message": "Le sondage auquel vous essayez de répondre n'existe pas"}), 404