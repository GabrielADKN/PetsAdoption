from flask import Flask, render_template, request, redirect, url_for, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

app.config["SECRET_KEY"] = "secret"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def home():
    """Redirect to /pets."""

    return redirect(url_for("list_pets"))


@app.route("/pets")
def list_pets():
    """Show all pets."""

    pets = Pet.all_pets()
    return render_template("pets.html", pets=pets)


@app.route("/pets/add", methods=["GET", "POST"])
def add_pet():
    """Add a pet."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        Pet.find_or_create_pet(name, species, photo_url, age, notes, True)

        flash(f"Added {name} the {species}!", "success")
        return redirect(url_for("list_pets"))
    else:
        return render_template("add_pet.html", form=form)


@app.route("/pets/<int:id>", methods=["GET", "POST"])
def show_pet(id):
    """Show a pet."""

    pet = Pet.get_by_id(id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data

        db.session.commit()

        flash(f"Updated {pet.name} the {pet.species}!", "success")
        return redirect(url_for("list_pets"))
    else:
        return render_template("show_pet.html", pet=pet, form=form)
