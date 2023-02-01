from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired, URL, Optional

class AddCupcakeForm(FlaskForm):
    flavor=StringField("Flavor", validators=[InputRequired()],)
    size=StringField("Size", validators=[InputRequired()],)
    rating=SelectField("Rating", choices=[("1", "1"),("2", "2"),("3", "3"),("4", "4"),("5", "5"),("6", "6"),("7", "7"),("8", "8"),("9", "9"),("10", "10"),],)
    image=StringField("Image", validators=[Optional(), URL()],)
