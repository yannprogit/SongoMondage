#Import
from pymongo import MongoClient
from bson import ObjectId

mongo_url = 'mongodb://localhost:27017/'

#Méthode
def create_database():
    client = MongoClient(mongo_url)
    
    try:
        database = client['songomondageDB']

        #Création des collections
        utilisateurs_collection = database['utilisateurs']
        sondages_collection = database['sondages']
        reponses_collection = database['reponses']

        #Données utilisateurs
        utilisateur_data = {
            "_id": ObjectId("5f3a3c1c1234567890123456"),
            "nom": "OuiMan",
            "mail": "ouiman@gmail.com",
            "mdp": "$2a$10$/waLFVGGYGQhjlP5X9XzMOPAWiWjfiRy2ZIfIvPzOPO8Cc1Uaqb1."
        }
        utilisateurs_collection.insert_one(utilisateur_data)

        #Données sondages
        sondage_data = {
            "_id": ObjectId("5f3a3c1c1234567890123456"),
            "nom": "Sondage Préférences Alimentaires",
            "createur": ObjectId("5f3a3c1b1234567890123456"),
            "questions": [
                {
                    "_id": ObjectId("5f3a3c1d1234567890123456"),
                    "intitule": "Quel est votre plat préféré ?",
                    "type": "ouverte"
                },
                {
                    "_id": ObjectId("5f3a3c1e1234567890123456"),
                    "intitule": "Quels types de cuisine préférez-vous ?",
                    "type": "qcm",
                    "reponses": ["Italienne", "Chinoise", "Mexicaine", "Indienne"]
                }
            ]
        }
        sondages_collection.insert_one(sondage_data)

        #Données réponses
        reponse_data = {
            "sondage_id": ObjectId("5f3a3c1c1234567890123456"),
            "utilisateur_id": ObjectId("5f3a3c1d1234567890123456"),
            "reponses": [
                {
                    "question_id": ObjectId("5f3a3c1d1234567890123456"),
                    "reponse": "Pizza"
                },
                {
                    "question_id": ObjectId("5f3a3c1e1234567890123456"),
                    "reponse": ["Italienne", "Indienne"]
                }
            ]
        }
        reponses_collection.insert_one(reponse_data)

        print('Base de données, collections et données créées avec succès.')
    finally:
        client.close()

if __name__ == "__main__":
    create_database()
