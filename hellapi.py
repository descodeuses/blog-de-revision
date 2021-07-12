from flask import Flask, render_template, url_for, redirect, jsonify, request

app = Flask(__name__)

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
list_billets = [premier_billet, deuxieme_billet]

@app.route("/")
def hello_world():
    return render_template('base_hellapi.html', js_file=url_for('static', filename='hellapi.js'))

@app.route("/billet/<id>")
def billet(id=None):
  return render_template("billet.html", id=id, js_file=url_for('static', filename='hellapi-billet.js'))

@app.route("/api/billet/<id>")
def api_billet(id=None):
  selectedBillet = None
  for billet in list_billets:
    if billet["id"] == int(id):
      selectedBillet = billet
  return jsonify(selectedBillet)

@app.route("/api/billets")
def billets():
  return jsonify(list_billets)


