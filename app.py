from config.config import app
from routes.sondage_route import sondage_blueprint
#from routes.sondage_routes import sondage_blueprint

#Enregistrement des routes
app.register_blueprint(sondage_blueprint)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)