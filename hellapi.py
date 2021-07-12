from flask import Flask, render_template, url_for, redirect, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('base_hellapi.html', js_file=url_for('static', filename='hellapi.js'))

@app.route("/nouveau_billet")
def nouveau_billet():
    return render_template('hellapi_formulaire.html')

@app.route("/ajoute_billet", methods=['POST'])
def ajoute_billet():
    return redirect(url_for('hello_world'))

@app.route("/billets")
def billets():
  premier_billet = {
    "id": 1,
    "title": "Mon Super premier titre",
    "text": "blablbla super long blablabla super long"
  }
  deuxieme_billet = {
    "id": 2,
    "title": "Deuxieme titre",
    "text": "blablbla super long blablabla super long blablbla super long blablabla super long blablbla super long blablabla super long blablbla super long blablabla super long"
  }  
  billets = [premier_billet, deuxieme_billet]
  return jsonify(billets)


