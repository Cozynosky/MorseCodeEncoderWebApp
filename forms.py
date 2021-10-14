from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError


class UserInput(FlaskForm):
    text_input = TextAreaField("Input", validators=[DataRequired()])
    text_output = TextAreaField("Output")
    encode_button = SubmitField("Encode")
    decode_button = SubmitField("Decode")
