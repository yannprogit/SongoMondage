from bson import ObjectId
from config.config import db

class SondageService:
    collection = db['sondages']

    @staticmethod
    def get_sondages():
        return SondageService.collection.find({})
    
    @staticmethod
    def get_mes_sondages(util_id):
        return SondageService.collection.find({'createur': ObjectId(util_id)})
    
    @staticmethod
    def get_sondage(id):
        try:
            return SondageService.collection.find_one({'_id': ObjectId(id)})
        except Exception:
            return None
    
    @staticmethod
    def add_sondage(sondage):
        try:
            SondageService.collection.insert_one(sondage)
            return True 
        except Exception:
            return False 
        
    @staticmethod
    def del_sondage(id):
        try:
            sondage_id = ObjectId(id)
            db['reponses'].delete_many({'sondage_id': sondage_id})
            SondageService.collection.delete_one({'_id': sondage_id})
            return True 
        except Exception:
            return False 
        
    @staticmethod
    def upd_sondage(id, nouveau_sondage):
        try:
            SondageService.collection.update_one({'_id': ObjectId(id)}, nouveau_sondage)
            return True 
        except Exception as e:
            print(f"Erreur lors de l'ajout de l'utilisateur : {e}")
            return False 
        
    @staticmethod
    def name_exists(id, nom):
        filtre = {"$and": [{"nom": nom}]}
        if id:
            filtre["$and"].append({"_id": {"$ne": ObjectId(id)}})

        return SondageService.collection.find_one(filtre)