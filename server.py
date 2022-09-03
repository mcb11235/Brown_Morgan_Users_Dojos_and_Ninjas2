from flask_app import app
from flask_app.models.user import User
from flask_app.controllers import users
from flask_app.models.dojo import Dojo
from flask_app.controllers import dojos
if __name__ == "__main__":
    app.run(debug=True)