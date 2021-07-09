from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('hello.html')

@app.route("/nouveau_billet")
def nouveau_billet():
    return render_template('formulaire_billet.html')
