from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.db.Column(db.db.Integer, primary_key=True)
    email = db.db.Column(db.db.String(120), unique=True, nullable=False)
    password = db.db.Column(db.db.String(80), unique=False, nullable=False)
    is_active = db.db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    lastname = db.Column(db.String(250), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    birth_year = db.Column(db.String(250), nullable=True)
    planets = db.Column(db.String(250), db.ForeignKey('planets.id'))
    starships = db.Column(db.String(250), db.ForeignKey('starships.id'))

    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "age": self.age,
            "birth_year": self.birth_year,
            # do not serialize the password, its a security breach
        }

class FavCharacters(db.Model):
    __tablename__ = 'favcharacters'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    character = db.relationship(Characters)

    def __repr__(self):
        return '<FavCharacters %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    gravity = db.Column(db.Integer, nullable=True)
    rotation_period = db.Column(db.String(250), nullable=True)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    character = db.relationship(Characters)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "gravity": self.gravity,
            "rotation_period": self.rotation_period,
            # do not serialize the password, its a security breach
        }


class FavPlanets(db.Model):
    __tablename__ = 'favplanets'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planet = db.relationship(Planets)

    def __repr__(self):
        return '<FavPlanets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.character_id,
            # do not serialize the password, its a security breach
        }

        

class Starships(db.Model):
    __tablename__ = 'starships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    passengers = db.Column(db.Integer, nullable=True)
    speed = db.Column(db.String(250), nullable=True)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    character = db.relationship(Characters)

    def __repr__(self):
        return '<Starships %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "passengers": self.passengers,
            "speed": self.speed,
            # do not serialize the password, its a security breach
        }