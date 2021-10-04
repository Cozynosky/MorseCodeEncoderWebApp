from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms import UserInput

# setup app
app = Flask(__name__)
app.config['SECRET_KEY'] = "default_secret_key"
Bootstrap(app)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.route("/encoding", methods=["GET", "POST"])
def encoding():
    input_form = UserInput()
    return render_template("encoding.html", form=input_form)


if __name__ == "__main__":
    app.run(debug=True)
