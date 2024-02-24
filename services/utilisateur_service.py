from config.config import db

class UtilService:
    collection = db['utilisateurs']

    @staticmethod
    def add_util(utilisateur):
        try:
            UtilService.collection.insert_one(utilisateur)
            return True  # L'ajout a réussi
        except Exception as e:
            print(f"Erreur lors de l'ajout de l'utilisateur : {e}")
            return False  # L'ajout a échoué