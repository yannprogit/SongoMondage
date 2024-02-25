from bson import ObjectId
from config.config import db

class SondageService:
    collection = db['sondages']

    @staticmethod
    def get_sondages():
        return SondageService.collection.find({})
    
    @staticmethod
    def get_sondage(id):
        return SondageService.collection.find_one({'_id': ObjectId(id)})
    
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
        except Exception:
            return False 
        
    @staticmethod
    def name_exists(id, nom):
        filtre = {"$and": [{"nom": nom}]}
        if id:
            filtre["$and"].append({"_id": {"$ne": object(id)}})

        return SondageService.collection.find_one(filtre)