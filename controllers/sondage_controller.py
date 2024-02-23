from services.sondage_service import SondageService

class SondageController:
    @staticmethod
    def get_sondages():
        sondages = SondageService.get_sondages()
        sondages_json = [SondageController.convertir_sondage_json(sondage) for sondage in sondages]
        return {"sondages": sondages_json}

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