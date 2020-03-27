"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL, NumberRange
from models import Pet, DEFAULT_PHOTO_URL


class AddPetForm(FlaskForm):
    "form for adding pets"

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Pet Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', "Porcupine")])
    photo_url = StringField("Image URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes")


class EditPetForm(FlaskForm):
    "form for editing an existing pet"

    photo_url = StringField("Image URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes")
    available = BooleanField("Available")
