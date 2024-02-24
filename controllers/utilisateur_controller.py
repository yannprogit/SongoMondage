from services.utilisateur_service import UtilService
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

class UtilController:

    @staticmethod
    def add_util(data):
        utilisateur = {
            'nom': data['nom'],
            'mail': data['mail'],
            'mdp': bcrypt.generate_password_hash(data['mdp']).decode('utf-8')
        }
        resultat = UtilService.add_util(utilisateur)
        return {"sucess": resultat}
    
    
