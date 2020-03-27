"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, flash, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet, add_pet_to_db, edit_pet_details
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "abcdef"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# debug = DebugToolbarExtension(app)
# app.debug = True


@app.route('/')
def show_homepage():
    """ Homepage listing pets """

    pets = Pet.query.all()

    return render_template('pet-list.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    "generate form to add pet and display on page, and accept new pet via POST"

    form = AddPetForm()

    if form.validate_on_submit():

        add_pet_to_db(form)
        name = form.name.data

        flash(f"Added {name}!")
        return redirect("/")

    else:
        return render_template("add-pet.html", form=form)


@app.route('/<int:pet_id>', methods=["GET", "POST"])
def pet_details(pet_id):
    "shows more info about a pet, and allows editing of details"

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():

        edit_pet_details(form, pet)
        name = pet.name

        flash(f"Edited {name}!")
        return redirect("/")

    else:
        return render_template("pet-details.html", form=form, pet=pet)