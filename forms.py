from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine"), ("pig", "Pig")])
    photo_url = StringField("Photo URL", validators=[URL(), InputRequired(message="Photo URL is required")])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30), InputRequired(message="Age is required and must be between 0 and 30")])
    notes = TextAreaField("Comments", validators=[Optional()])