from services.utilisateur_service import UtilService
from flask_bcrypt import Bcrypt
from flask import jsonify
bcrypt = Bcrypt()

class UtilController:

    @staticmethod
    def add_util(data):
        if 'mail' in data and data['mail'] is not None and 'mdp' in data and data['mdp'] is not None and 'nom' in data and data['nom'] is not None and data['mail'].strip()!='' and data['mdp'].strip()!='' and data['nom'].strip()!='':
            if UtilService.nom_exists(data['nom']) :
                return jsonify({"sucess": False, "message": "Ce nom est déjà utilisé, veuillez en utiliser un autre"}), 422
            elif not UtilService.mail_exists(data['mail']) :
                utilisateur = {
                    'nom': data['nom'],
                    'mail': data['mail'],
                    'mdp': bcrypt.generate_password_hash(data['mdp']).decode('utf-8')
                }
                resultat = UtilService.add_util(utilisateur)
                return jsonify({"sucess": resultat}), 200
            else :  
                return jsonify({"sucess": False, "message": "Ce mail est déjà utilisé, veuillez en utiliser un autre"}), 422
        else:
            return jsonify({"success": False, "message": "Vous devez remplir tous les champs"}), 400
        
    @staticmethod
    def get_utils_names():
        utilisateurs = UtilService.get_utils()
        utilisateurs_json = [UtilController.convertir_util_json(utilisateur) for utilisateur in utilisateurs]
        return jsonify({"success": True, "utils": utilisateurs_json}), 200

    @staticmethod
    def convertir_util_json(utilisateur):
        utilisateur_json = {
            "_id": str(utilisateur['_id']),
            "nom": utilisateur['nom']
        }
        return utilisateur_json
    
