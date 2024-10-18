"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, FavCharacters, 
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():
    users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), users))

    return jsonify(all_users), 200



@app.route('/user', methods=['POST'])
def create_user():
    request_body_user = request.get_json()
    new_user = User(email=request_body_user["email"], password=request_body_user["pasword"], is_active=request_body_user["is_active"])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "usuario agregado con exito", "user": new_user.serialize()})


@app.route('/character', methods=['GET'])
def get_character():
    characters = Characters.query.all()
    all_characters = list(map(lambda x: x.serialize(), characters))

    return jsonify(all_characters), 200






@app.route('/favoritos', methods=['GET'])
def get_favoritos():
    favorite_character = FavCharacters.query.all()
    all_favorite_characters = list(map(lambda x: x.serialize(), favorite_character))

    return jsonify({"characters" : all_favorite_characters})


@app.route('/favoritos/character', methods=['POST'])
def add_favorite_character():
    request_body_favorite_character = request.get_json()
    new_favorite_character = FavCharacters(user_id=request_body_favorite_character["user_id"], character_id=request_body_favorite_character["character_id"])
    db.session.add
    db.session.commit()

    return jsonify({"msg": "personaje agregado a los favoritos"})

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
