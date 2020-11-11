
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index ():
    return render_template("index.html", title="Corner Coffee")

@app.route("/coffee")
def coffee ():
    return render_template("coffee.html", title="Our coffee")

@app.route("/sweets")
def sweets():
    return render_template("sweets.html", title="Sweets")

@app.route("/lemonade")
def lemonade():
    return render_template("lemonade.html", title="Lemonade")


if __name__ == "__main__":
    app.run()