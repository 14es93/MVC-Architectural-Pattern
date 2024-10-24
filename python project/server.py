# server.py
from flask import Flask, render_template
from src.controllers.books import booksCtrlr
from src.controllers.authors import authorsCtrlr

app = Flask(__name__)

@app.route('/')
def index():

    return render_template("home.html")

app.register_blueprint(booksCtrlr, url_prefix="/books")
app.register_blueprint(authorsCtrlr, url_prefix="/authors")

app.run(host="127.0.0.1", port=5000, debug=True)