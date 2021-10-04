from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField
from wtforms.validators import DataRequired


class UserInput(FlaskForm):
    text_input = TextAreaField("Your message", validators=[DataRequired()])
    submit_button = SubmitField("Encode message")