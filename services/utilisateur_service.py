from config.config import db
from bson import ObjectId

class UtilService:
    collection = db['utilisateurs']

    @staticmethod
    def add_util(utilisateur):
        try:
            UtilService.collection.insert_one(utilisateur)
            return True 
        except Exception as e:
            print(f"Erreur lors de l'ajout de l'utilisateur : {e}")
            return False 
        
    @staticmethod
    def mail_exists(mail):
        return UtilService.collection.find_one({"mail": mail})
    
    @staticmethod
    def nom_exists(nom):
        return UtilService.collection.find_one({"nom": nom})
    
    @staticmethod
    def get_utils():
        try:
            return UtilService.collection.find({}, {"_id": 1, "nom": 1})
        except Exception:
            return None