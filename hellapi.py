from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('base_hellapi.html')

@app.route("/nouveau_billet")
def nouveau_billet():
    return render_template('hellapi_formulaire.html')

@app.route("/ajoute_billet", methods=['POST'])
def ajoute_billet():
    return redirect(url_for('hello_world'))
