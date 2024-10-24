# src/controllers/authors.py
from flask import Blueprint, render_template

authorsCtrlr = Blueprint('authors', __name__)

@authorsCtrlr.route('/')
def list():
    return render_template("authors/list.html")

@authorsCtrlr.route('/<int:id>')
def getItem(id: int):
    return render_template("authors/detail.html", id=id)