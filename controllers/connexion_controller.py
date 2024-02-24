from config.config import db
from flask import jsonify
import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

class ConnexionController:
    collection = db['utilisateurs']
    secret_key = os.environ.get('secretKey')

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
    def generate_token(util):
        payload = {
            'id': str(util['_id']), 
            'mail': util['mail'],
            'exp': datetime.utcnow() + timedelta(seconds=3600)
        }
        token = jwt.encode(payload, ConnexionController.secret_key, algorithm='HS256')
        return token