#Import #/65db7144c89726ca773e5a69
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
        utilisateurs_data = [
            {
                "_id": ObjectId("65e37e0f91f54aab5df94dc4"),
                "nom": "OuiMan",
                "mail": "ouiman@gmail.com",
                "mdp": "$2a$10$/waLFVGGYGQhjlP5X9XzMOPAWiWjfiRy2ZIfIvPzOPO8Cc1Uaqb1."
            },
            {
                "_id": ObjectId("65e37e1e91f54aab5df94dc5"),
                "nom": "NonMan",
                "mail": "nonman@gmail.com",
                "mdp": "$2a$10$/waLFVGGYGQhjlP5X9XzMOPAWiWjfiRy2ZIfIvPzOPO8Cc1Uaqb1."  
            }
        ]

        utilisateurs_collection.insert_many(utilisateurs_data)

        #Données sondages
        sondages_data = [
            {
                "_id": ObjectId("65e37e4b91f54aab5df94dc8"),
                "nom": "Sondage Préférences Alimentaires",
                "createur": ObjectId("65e37e0f91f54aab5df94dc4"),
                "questions": [
                    {
                        "_id": ObjectId("65e37e4b91f54aab5df94dc6"),
                        "intitule": "Quel est votre plat préféré ?",
                        "type": "ouverte"
                    },
                    {
                        "_id": ObjectId("65e37e4b91f54aab5df94dc7"),
                        "intitule": "Quels types de cuisine préférez-vous ?",
                        "type": "qcm",
                        "reponses": ["Italienne", "Chinoise", "Mexicaine", "Indienne"]
                    }
                ]
            },
            {
                "_id": ObjectId("65e37efa91f54aab5df94dca"),  
                "nom": "Sondage Couleurs Préférées",
                "createur": ObjectId("65e37e1e91f54aab5df94dc5"), 
                "questions": [
                    {
                        "_id": ObjectId("65e37efa91f54aab5df94dc9"),
                        "intitule": "Quelle est votre couleur préférée ?",
                        "type": "ouverte"
                    }
                ]
            }
        ]
        sondages_collection.insert_many(sondages_data)

        #Données réponses
        reponse_data = {
            "sondage_id": ObjectId("65e37e4b91f54aab5df94dc8"),
            "utilisateur_id": ObjectId("65e37e0f91f54aab5df94dc4"),
            "reponses": [
                {
                    "question_id": ObjectId("65e37e4b91f54aab5df94dc6"),
                    "reponse": "Pizza"
                },
                {
                    "question_id": ObjectId("65e37e4b91f54aab5df94dc7"),
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
