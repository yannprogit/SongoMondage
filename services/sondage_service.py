from config.config import db

class SondageService:
    collection = db['sondages']

    @staticmethod
    def get_sondages():
        return SondageService.collection.find({})