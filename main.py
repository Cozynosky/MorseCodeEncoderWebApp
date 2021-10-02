from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = "default_secret_key"


@app.route("/")
def home_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
