from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from forms import UserInput
from encoder import encode_message, allowed_to_encode, allowed_to_decode, decode_message

# setup app
app = Flask(__name__)
app.config['SECRET_KEY'] = "default_secret_key"
Bootstrap(app)


@app.route("/", methods=["GET", "POST"])
def home():
    input_form = UserInput()
    if input_form.validate_on_submit():
        text = input_form.text_input.data
        if input_form.encode_button.data:
            if allowed_to_encode(text):
                encoded_text = encode_message(text)
                return render_template("home.html", form=input_form, result=encoded_text)
            else:
                input_form.text_input.errors.append("Unallowed letters for encoding used.")
        elif input_form.decode_button.data:
            words = text.split(" / ")
            if allowed_to_decode(words):
                decoded_text = decode_message(words)
                return render_template("home.html", form=input_form, result=decoded_text)
            else:
                input_form.text_input.errors.append("Unallowed symbols for decoding used.")
    return render_template("home.html", form=input_form, result="")


if __name__ == "__main__":
    app.run(debug=True)
