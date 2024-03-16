from config.config import app
from routes.sondage_route import sondage_blueprint
from routes.utilisateur_route import util_blueprint
from routes.reponse_route import reponse_blueprint
from routes.connexion_route import connexion_blueprint

#Enregistrement des routes
app.register_blueprint(sondage_blueprint)
app.register_blueprint(reponse_blueprint)
app.register_blueprint(util_blueprint)
app.register_blueprint(connexion_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)