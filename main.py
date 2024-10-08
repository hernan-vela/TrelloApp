import os
from flask import Flask
from marshmallow.exceptions import ValidationError

from init import db, ma, bcrypt, jwt
from controllers.cli_controllers import db_commands
from controllers.auth_controller import auth_bp
from controllers.card_controller import cards_bp
print(__name__)
def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    print(os.environ.get("DATABASE_URL"))
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    @app.errorhandler(ValidationError)
    def validation_error(err):
        # This could be left as 'pass', but this time we will use it
        return {"error": err.messages}, 400

    app.register_blueprint(db_commands)
    app.register_blueprint(auth_bp)
    app.register_blueprint(cards_bp)
    return app