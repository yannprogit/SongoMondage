from services.utilisateur_service import UtilService
from flask_bcrypt import Bcrypt
from flask import jsonify
bcrypt = Bcrypt()

class UtilController:

    @staticmethod
    def add_util(data):
        if not UtilService.mail_exists(data['mail']) :
            utilisateur = {
                'nom': data['nom'],
                'mail': data['mail'],
                'mdp': bcrypt.generate_password_hash(data['mdp']).decode('utf-8')
            }
            resultat = UtilService.add_util(utilisateur)
            return jsonify({"sucess": resultat}), 200
        else :  
            return jsonify({"sucess": False, "message": "Ce mail est déjà utilisé, veuillez en utiliser un autre"}), 422
    
