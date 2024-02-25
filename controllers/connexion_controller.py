from config.config import db
from flask import jsonify, request
import jwt
from datetime import datetime, timedelta
#from dotenv import load_dotenv
import os
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

class ConnexionController:
    collection = db['utilisateurs']
    secret_key = os.environ.get('secretKey')
    token_blacklist = []

    @staticmethod
    def auth_middleware(func):
        def wrapper(*args, **kwargs):
            token = request.headers.get('Authorization')

            if not token:
                return jsonify({"success": False, "message": "Vous devez être connecté pour avoir accès à cette page !"}), 401
            
            if token in ConnexionController.token_blacklist:
                return jsonify({"success": False, "message": "La session est invalide"}), 401

            try:
                decoded_token = jwt.decode(token, ConnexionController.secret_key, algorithms=['HS256'])

                request.util_id = decoded_token.get('id')
                request.util_mail = decoded_token.get('mail')
                request.util_nom = decoded_token.get('nom')

            except jwt.ExpiredSignatureError:
                return jsonify({"success": False, "message": "La session a expiré, veuillez vous reconnecter"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"success": False, "message": "La session est invalide"}), 401
            
            return func(*args, **kwargs)

        return wrapper
    
    @staticmethod
    def connexion(data):

        mail = data["mail"]
        mdp = data["mdp"]

        util = ConnexionController.collection.find_one({'mail': mail}) 

        if util:
            if bcrypt.check_password_hash(util['mdp'], mdp):
                token = ConnexionController.generate_token(util)
                return jsonify({"success": True, "token": token}), 200
            else:
                return jsonify({"success": False, "message": "Le mail ou le mot de passe est incorrecte"}), 401
        else:
            return jsonify({"success": False, "message": "Le mail ou le mot de passe est incorrecte"}), 401
        
    @staticmethod
    def deconnexion():
        token = request.headers.get('Authorization')
        ConnexionController.token_blacklist.append(token)
        return jsonify({"success": True, "message": "Vous avez été déconnecté"}), 200
    
    @staticmethod
    def generate_token(util):
        payload = {
            'id': str(util['_id']), 
            'mail': util['mail'],
            'exp': datetime.utcnow() + timedelta(seconds=3600)
        }
        token = jwt.encode(payload, ConnexionController.secret_key, algorithm='HS256')
        return token