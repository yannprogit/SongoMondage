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
            },
            {
                "_id": ObjectId("660090d69693b88f2c4e8600"),
                "nom": "Yann",
                "mail": "yann@gmail.com",
                "mdp": "$2b$12$95j0LCRBCCKXjEQPj2Msye0zSGa7kAfFlALlq5XuUa3mEjds6xabe"
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
            },
                        {
                "_id": ObjectId("66008d31dda40b4fd59c9196"),
                "nom": "Sondaj2Fou",
                "createur": ObjectId("65e37e0f91f54aab5df94dc4"),
                "questions": [
                    {
                        "_id": ObjectId("66008d31dda40b4fd59c9193"),
                        "intitule": "Vous aimez ce sondage ?",
                        "type": "ouverte"
                    },
                    {
                        "_id": ObjectId("66008d31dda40b4fd59c9194"),
                        "intitule": "Question 2",
                        "type": "qcm",
                        "reponses": ["Oui ?", "Peut être ?", "Jsp", "Pourquoi cette question ?"]
                    },
                    {
                        "_id": ObjectId("66008d31dda40b4fd59c9195"),
                        "intitule": "Aurevoir",
                        "type": "ouverte"
                    }
                ]
            },
            {
                "_id": ObjectId("66008ddbdda40b4fd59c9199"),
                "nom": "Consommation des réseaux sociaux",
                "createur": ObjectId("65e37e0f91f54aab5df94dc4"),
                "questions": [
                    {
                        "_id": ObjectId("66008ddbdda40b4fd59c9197"),
                        "intitule": "Quel est votre réseau préféré ?",
                        "type": "ouverte"
                    },
                    {
                        "_id": ObjectId("66008ddbdda40b4fd59c9198"),
                        "intitule": "Sélectionnez vos réseaux préférés ",
                        "type": "qcm",
                        "reponses": ["Instagram", "Youtube", "Snapchat", "Discord", "What's app", "Facebook", "X (ou twitter pour les anciens)", "Messenger", "Les sms téléphone"]
                    }
                ]
            },
            {
                "_id": ObjectId("66008fb4dda40b4fd59c919e"),
                "nom": "Voyages",
                "createur": ObjectId("65e37e1e91f54aab5df94dc5"),
                "questions": [
                    {
                        "_id": ObjectId("66008fb4dda40b4fd59c919a"),
                        "intitule": "Quel serait votre prochaine destination ?",
                        "type": "ouverte"
                    },
                    {
                        "_id": ObjectId("66008fb4dda40b4fd59c919b"),
                        "intitule": "Parmis ces zones géographiques, lesquelles vous font envie ?",
                        "type": "qcm",
                        "reponses": ["Caraibes", "Maghreb", "Asie du sud est", "Europe du nord", "Europe du sud", "Pays scandinaves", "Afrique subsaharienne", "Amérique du nord", "Amérique du sud", "Aucune cité ici"]
                    },
                    {
                        "_id": ObjectId("66008fb4dda40b4fd59c919c"),
                        "intitule": "Qu'est ce que vous aimez dans les voyages",
                        "type": "qcm",
                        "reponses": ["Découvrir de nouvelle culture", "Découvrir de nouvelle personne", "Faire la fête", "être dépaysé", "Découvrir de nouvelle cuisine"]
                    },
                    {
                        "_id": ObjectId("66008fb4dda40b4fd59c919d"),
                        "intitule": "Avec qui aimez vous voyager ?",
                        "type": "qcm",
                        "reponses": ["Seul", "Familles", "Amis", "Conjoint/Conjointe", "Collègues"]
                    },
                    {
                        "_id": ObjectId("66008fcddda40b4fd59c919f"),
                        "intitule": "Quel est le voyage que vous avez le moins aimé ?",
                        "type": "ouverte"
                    }
                ]
            },
            {
                "_id": ObjectId("660092859693b88f2c4e8605"),
                "nom": "Animes",
                "createur": ObjectId("660090d69693b88f2c4e8600"),
                "questions": [
                    {
                        "_id": ObjectId("660092859693b88f2c4e8601"),
                        "intitule": "Quel l'anime que vous aimez le plus ?",
                        "type": "ouverte"
                    },
                    {
                        "_id": ObjectId("660092859693b88f2c4e8602"),
                        "intitule": "Celui que vous aimez le moins ?",
                        "type": "ouverte"
                    },
                    {
                        "_id": ObjectId("660092859693b88f2c4e8603"),
                        "intitule": "Qui est le vrai big 3 ?",
                        "type": "qcm",
                        "reponses": ["One piece/Naruto/Bleach", "One piece/Naruto/Dragon ball"]
                    },
                    {
                        "_id": ObjectId("660092859693b88f2c4e8604"),
                        "intitule": "Vous validez l'adaptation de solo leveling en anime ?",
                        "type": "ouverte"
                    }
                ]
            },
            {
                "_id": ObjectId("660094199693b88f2c4e860b"),
                "nom": "Frameworks dev",
                "createur": ObjectId("660090d69693b88f2c4e8600"),
                "questions": [
                    {
                        "_id": ObjectId("660094199693b88f2c4e8609"),
                        "intitule": "Framework front préférés",
                        "type": "qcm",
                        "reponses": ["Vue js", "Angular", "React js", "Svelte", "Ember.js"]
                    },
                    {
                        "_id": ObjectId("660094199693b88f2c4e860a"),
                        "intitule": "Back ?",
                        "type": "qcm",
                        "reponses": ["Laravel", "Symfony", "Ruby on rails", "Express.js", "Flask", "Django", "Spring boot"]
                    }
                ]
            }
        ]
        sondages_collection.insert_many(sondages_data)

        #Données réponses
        reponse_data = [
            {
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
            },
            {
                "_id": ObjectId("660094b39693b88f2c4e860f"),
                "sondage_id": ObjectId("660092859693b88f2c4e8605"),
                "utilisateur_id": ObjectId("65e37e0f91f54aab5df94dc4"),
                "reponses": [
                    {
                        "_id": ObjectId("660092859693b88f2c4e8601"),
                        "reponse": "One piece"
                    },
                    {
                        "_id": ObjectId("660092859693b88f2c4e8602"),
                        "reponse": "Naruto"
                    },
                    {
                        "_id": ObjectId("660092859693b88f2c4e8603"),
                        "reponse": ["One piece/Naruto/Dragon ball"]
                    },
                    {
                        "_id": ObjectId("660092859693b88f2c4e8604"),
                        "reponse": "Non j'aime pas"
                    }
                ]
            },
            {
                "_id": ObjectId("660094be9693b88f2c4e8610"),
                "sondage_id": ObjectId("660094199693b88f2c4e860b"),
                "utilisateur_id": ObjectId("65e37e0f91f54aab5df94dc4"),
                "reponses": [
                    {
                        "_id": ObjectId("660094199693b88f2c4e8609"),
                        "reponse": ["Vue js", "Svelte", "Ember.js"]
                    },
                    {
                        "_id": ObjectId("660094199693b88f2c4e860a"),
                        "reponse": ["Laravel", "Ruby on rails", "Django"]
                    }
                ]
            },
            {
                "_id": ObjectId("660094f49693b88f2c4e8611"),
                "sondage_id": ObjectId("65e37e4b91f54aab5df94dc8"),
                "utilisateur_id": ObjectId("65e37e1e91f54aab5df94dc5"),
                "reponses": [
                    {
                        "_id": ObjectId("65e37e4b91f54aab5df94dc6"),
                        "reponse": "Pâtes"
                    },
                    {
                        "_id": ObjectId("65e37e4b91f54aab5df94dc7"),
                        "reponse": ["Italienne", "Chinoise", "Mexicaine", "Indienne"]
                    }
                ]
            }
        ]
        reponses_collection.insert_many(reponse_data)

        print('Base de données, collections et données créées avec succès.')
    finally:
        client.close()

if __name__ == "__main__":
    create_database()
