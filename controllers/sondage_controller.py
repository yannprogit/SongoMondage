from services.sondage_service import SondageService
from flask import jsonify, request
from bson import ObjectId

class SondageController:
    @staticmethod
    def get_sondages():
        sondages = SondageService.get_sondages(request.util_id)
        sondages_json = [SondageController.convertir_sondage_json(sondage) for sondage in sondages]
        return jsonify({"sondages": sondages_json}), 200
    
    @staticmethod
    def get_mes_sondages():
        sondages = SondageService.get_mes_sondages(request.util_id)
        sondages_json = [SondageController.convertir_sondage_json(sondage) for sondage in sondages]
        return jsonify({"sondages": sondages_json}), 200

    @staticmethod
    def add_sondage(data):
        if not SondageService.name_exists(None, data['nom']):
            sondage = {
                'nom': data['nom'],
                'createur': ObjectId(str(request.util_id)),
                'questions': []
            }

            for question_data in data['questions']:
                question_type = question_data.get('type', 'ouverte')

                if question_type == 'qcm':
                    reponses = question_data.get('reponses', [])
                    if len(reponses) < 2:
                        return jsonify({"success": False, "message": "Pour les questions de type QCM, veuillez spécifier au moins 2 réponses"}), 422

                    question = {
                        '_id': ObjectId(),
                        'intitule': question_data['intitule'],
                        'type': question_type,
                        'reponses': reponses
                    }
                else:
                    question = {
                        '_id': ObjectId(),
                        'intitule': question_data['intitule'],
                        'type': question_type
                    }

                sondage['questions'].append(question)
            
            resultat = SondageService.add_sondage(sondage)
            return jsonify({"sucess": resultat}), 200
        else:
            return jsonify({"sucess": False, "message": "Le nom est déjà pris, veuillez choisir un autre nom"}), 422
        
    @staticmethod
    def del_sondage(id):
        sondage = SondageService.get_sondage(id)
        if not sondage:
            return jsonify({"sucess": False, "message": "Ce sondage n'existe pas"}), 404
        elif str(request.util_id)!=str(sondage['createur']):
            return jsonify({"sucess": False, "message": "Ce sondage ne vous appartient pas"}), 403
        else:
            resultat = SondageService.del_sondage(id)
            return jsonify({"sucess": resultat}), 200
        
    @staticmethod
    def get_sondage(id):
        sondage = SondageService.get_sondage(id)
        if not sondage:
            return jsonify({"sucess": False, "message": "Ce sondage n'existe pas"}), 404
        else:
            return jsonify({"sucess": True, "sondage": SondageController.convertir_sondage_json(sondage)}), 200
        
    @staticmethod
    def upd_sondage(id, data):
        sondage = SondageService.get_sondage(id)
        
        if not sondage:
            return jsonify({"sucess": False, "message": "Ce sondage n'existe pas"}), 404
        elif str(request.util_id)!=str(sondage['createur']):
            return jsonify({"sucess": False, "message": "Ce sondage ne vous appartient pas"}), 403
        elif SondageService.name_exists(id, data['nom']):
            print(SondageService.name_exists(id, data['nom']))
            return jsonify({"sucess": False, "message": "Le nom est déjà pris, veuillez choisir un autre nom"}), 422
        else:
            nouveau_sondage = {
                '$set': {
                    'nom': data['nom'],
                    'createur': ObjectId(str(request.util_id))
                }
            }

            if 'questions' in data:
                nouveau_sondage['$set']['questions'] = []

                for question_data in data['questions']:
                    question_type = question_data.get('type', 'ouverte')

                    if question_type == 'qcm':
                        reponses = question_data.get('reponses', [])
                        if len(reponses) < 2:
                            return jsonify({"success": False, "message": "Pour les questions de type QCM, veuillez spécifier au moins 2 réponses"}), 422

                        question = {
                            '_id': ObjectId(question_data['_id']) if '_id' in question_data else ObjectId(),
                            'intitule': question_data['intitule'],
                            'type': question_type,
                            'reponses': reponses
                        }
                    else:
                        question = {
                            '_id': ObjectId(question_data['_id']) if '_id' in question_data else ObjectId(),
                            'intitule': question_data['intitule'],
                            'type': question_type
                        }
                    nouveau_sondage['$set']['questions'].append(question)

            resultat = SondageService.upd_sondage(id, nouveau_sondage)
            return jsonify({"sucess": resultat}), 200
        
    @staticmethod
    def convertir_sondage_json(sondage):
        sondage_json = {
            "_id": str(sondage['_id']),
            "nom": sondage["nom"],
            "createur": str(sondage["createur"]),
            "questions": SondageController.convertir_objectids_questions(sondage["questions"])
        }
        return sondage_json

    @staticmethod
    def convertir_objectids_questions(questions):
        for question in questions:
            if '_id' in question:
                question['_id'] = str(question['_id'])

            if 'reponses' in question and isinstance(question['reponses'], list):
                question['reponses'] = [str(rep['_id']) if isinstance(rep, dict) and '_id' in rep else rep for rep in question['reponses']]

            if 'questions' in question and isinstance(question['questions'], list):
                question['questions'] = SondageController.convertir_objectids_questions(question['questions'])

        return questions