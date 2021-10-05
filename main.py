from flask import Flask, render_template, redirect, url_for,session
from flask_bootstrap import Bootstrap
from forms import UserInput
from encoder import Encoder

# setup app
app = Flask(__name__)
app.config['SECRET_KEY'] = "default_secret_key"
Bootstrap(app)
encoder = Encoder()


@app.route("/", methods=["GET", "POST"])
def home():
    input_form = UserInput()
    if input_form.validate_on_submit():
        text_to_encode = input_form.text_input.data
        if encoder.is_proper_message(text_to_encode):
            session['text_to_encode'] = text_to_encode
            return redirect(url_for('result'))
        else:
            input_form.text_input.errors.append("Not allowed symbols used")
    return render_template("home.html", form=input_form)


@app.route("/result")
def result():
    text = session.pop('text_to_encode', None)
    if text is None:
        return redirect(url_for('home'))
    encoded_text = encoder.encode_message(text)
    return render_template("result.html", text=text, encoded_text=encoded_text)


if __name__ == "__main__":
    app.run(debug=True)
