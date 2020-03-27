"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_PHOTO_URL = 'https://www.austinpetsalive.org/assets/images/_gallery/default_dog.png'


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)


def add_pet_to_db(form_data):
    "take submitted pet data and add to DB"

    name = form_data.name.data
    species = form_data.species.data
    photo_url = form_data.photo_url.data
    age = form_data.age.data
    notes = form_data.notes.data

    new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

    db.session.add(new_pet)
    db.session.commit()


def edit_pet_details(form_data, pet):
    "edit existing details of pet and update DB"

    if not form_data.photo_url:
        form_data.photo_url = None
    
    pet.photo_url = form_data.photo_url.data
    pet.notes = form_data.notes.data
    pet.available = form_data.available.data

    db.session.commit()


class Pet(db.Model):
    "Pet"

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    photo_url = db.Column(db.String, default=DEFAULT_PHOTO_URL)
    age = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String)
    available = db.Column(db.Boolean, nullable=False, default=True)

# def make_fake_pets():
#     " dummy data for test "
#     fluffy = Pet(name='Fluffy', species='poodle', age='young', available=True)
#     Jesse = Pet(name='Jesse', species='asshole', age='senior', available=True)
#     Bob = Pet(name='Bob', species='Zelda', age='adult', available=True)

#     db.session.add(Bob)
#     db.session.commit()

