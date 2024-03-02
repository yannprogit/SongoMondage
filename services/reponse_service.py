from bson import ObjectId
from config.config import db

class ReponseService:
    collection = db['reponses']

    @staticmethod
    def add_reponse(sondage_id, util_id, reponse):
        try:
            existing_reponse = ReponseService.collection.find_one({'sondage_id': ObjectId(sondage_id), 'utilisateur_id': ObjectId(util_id)})
            if existing_reponse:
                ReponseService.collection.update_one({'_id': ObjectId(existing_reponse['_id'])}, {'$set': {'reponses': reponse['reponses']}})
            else :
                ReponseService.collection.insert_one(reponse)
            return True 
        except Exception as e:
            print(f"Erreur lors de l'ajout de l'utilisateur : {e}")
            return False 