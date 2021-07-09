from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('hello.html')

@app.route("/nouveau_billet")
def nouveau_billet():
    return render_template('formulaire_billet.html')

@app.route("/ajoute_billet", methods=['POST', 'GET'])
def ajoute_billet():
    return redirect(url_for('hello_world'))
