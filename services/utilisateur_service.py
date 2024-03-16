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
    def get_util(id):
        try:
            return UtilService.collection.find_one({'_id': ObjectId(id)})
        except Exception:
            return None