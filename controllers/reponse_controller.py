from services.reponse_service import ReponseService
from services.sondage_service import SondageService
from flask import jsonify, request
from bson import ObjectId

class ReponseController:

    @staticmethod
    def add_reponse(sondage_id, data):
        if 'reponses' in data and isinstance(data['reponses'], list) and len(data['reponses']) > 0:
            sondage = SondageService.get_sondage(sondage_id)
            if sondage:
                reponse = {
                    'sondage_id': ObjectId(sondage_id),
                    'utilisateur_id': ObjectId(str(request.util_id)),
                    'reponses': []
                }
                
                for reponse_data in data['reponses']:
                    if not 'question_id' in reponse_data or reponse_data['question_id'] is None:
                        return jsonify({"success": False, "message": "l'id d'une des questions n'a pas été fourni"}), 400
                    
                    
                    question = None
                    for question_data in sondage['questions']:
                        if str(question_data['_id']) == reponse_data['question_id']:
                            question = question_data
                            break

                    if question:
                        if isinstance(reponse_data['reponse'], list):
                            reponse_data['reponse'] = list(filter(lambda rep: rep.strip() != '', map(str.strip, reponse_data['reponse'])))

                        if not 'reponse' in reponse_data or (question['type']=='ouverte' and reponse_data['reponse'].strip()=='') or reponse_data['reponse'] is None or question['type'] == 'qcm' and (not isinstance(reponse_data['reponse'], list) or len(reponse_data['reponse']) == 0):
                            return jsonify({"success": False, "message": "Vous devez répondre à toutes les questions du sondage !"}), 400

                        reponse_item = {
                            '_id': ObjectId(reponse_data['question_id']),
                            'reponse': reponse_data['reponse']
                        }

                        reponse['reponses'].append(reponse_item)
                
                if len(reponse['reponses'])==len(sondage['questions']):
                    resultat = ReponseService.add_reponse(sondage_id, str(request.util_id), reponse)
                    return jsonify({"sucess": resultat}), 200
                else :
                    return jsonify({"sucess": False, "message": "Vous devez répondre à toutes les questions du sondage !"}), 400
            else:
                return jsonify({"sucess": False, "message": "Le sondage auquel vous essayez de répondre n'existe pas"}), 404
        else:
            return jsonify({"sucess": False, "message": "Les réponses n'ont pas été fourni"}), 400
        
    @staticmethod
    def get_reponses(sondage_id):
        sondage = SondageService.get_sondage(sondage_id)
        if sondage:
            if str(request.util_id)==str(sondage['createur']):
                reponses = ReponseService.get_reponses(sondage_id)
                reponses_json = [ReponseController.convertir_reponse_json(reponse) for reponse in reponses]
                return jsonify({"reponses": reponses_json}), 200
            else :
                return jsonify({"sucess": False, "message": "Vous ne pouvez pas consulter les réponses d'un sondage qui ne vous appartient pas"}), 403
        else :
            return jsonify({"sucess": False, "message": "Le sondage auquel vous essayez de consulter les réponses n'existe pas"}), 404

    @staticmethod
    def get_reponse(id, sondage_id):
        sondage = SondageService.get_sondage(sondage_id)
        if not sondage:
            return jsonify({"sucess": False, "message": "Le sondage auquel vous essayez de consulter la réponse n'existe pas"}), 404
        else:
            if str(request.util_id)==str(sondage['createur']):
                reponse = ReponseService.get_reponse(id)
                if reponse :
                    return jsonify({"sucess": True, "reponse": ReponseController.convertir_reponse_json(reponse)}), 200
                else :
                    return jsonify({"sucess": False, "message": "Cette réponse n'existe pas"}), 404
            else :
                return jsonify({"sucess": False, "message": "Vous ne pouvez pas consulter la réponse d'un sondage qui ne vous appartient pas"}), 403
        
    @staticmethod
    def convertir_reponse_json(reponse):
        reponse_json = {
            "_id": str(reponse['_id']),
            "sondage_id": str(reponse['sondage_id']),
            "utilisateur_id": str(reponse['utilisateur_id']),
            "reponses": ReponseController.convertir_objectids_reponses(reponse['reponses'])
        }
        return reponse_json

    @staticmethod
    def convertir_objectids_reponses(reponses):
        for reponse in reponses:
            if '_id' in reponse:
                reponse['_id'] = str(reponse['_id'])

            if 'reponses' in reponse and isinstance(reponse['reponses'], list):
                reponse['reponses'] = [str(rep['_id']) if isinstance(rep, dict) and '_id' in rep else rep for rep in reponse['reponses']]

            if 'questions' in reponse and isinstance(reponse['questions'], list):
                reponse['questions'] = ReponseController.convertir_objectids_reponses(reponse['questions'])

        return reponses