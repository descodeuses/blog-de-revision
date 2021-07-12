# blog-de-revision

## Intention

Créer un blog avec 
- une interface graphique avec du javascript
- un serveur en python
- une petite base de donnée

L'idée sera de réviser l'architecture multicouche (organisation d'une application web).


## Developpement

Utilisation de Python3

`python3 -m venv venv` pour initialiser un environnement virtuel python de travail.

`pip install Flask` pour installer le framework Flask


Pour lancer le serveur

```bash
. venv/bin/activate
export FLASK_APP=hello
flask run --reload
```

Pour lancer l'application API

```bash
. venv/bin/activate # si nécessaire
export FLASK_APP=hellapi
flask run --reload
```


## Notes

La page [des codes retour HTTP sur Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

Page wikipédia sur les api [REST](https://fr.wikipedia.org/wiki/Representational_state_transfer)

Nous parlons du REPL (Read Eval Print Loop)
- https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop
- https://replit.com/


En débrief, nous parlons de l'utilsation de l'API Fetch en JavaScript, plutôt que d'utiliser XMLHttpRequest.

https://developer.mozilla.org/fr/docs/Web/API/Fetch_API/Using_Fetch

[OWASP The Open Web Application Security Project](https://owasp.org/)



Ce qui est fait ici n'est pas un exemple des meilleurs choix d'implémentation d'un moteur de blog. C'est plus pour l'exercice.


La construction de l'interface graphique en JS et pseudo HTML ajoute de la complexité à l'exercice.

Pour explorer les API, le serveur FLASK est des requêtes avec Curl auraient suffit.
`curl http://localhost:9999/api/billets`
`curl http://localhost:9999/api/billet/1`

L'api est à partir de la ligne 25 du fichier hellapi.py. Tous le JS et le HTML qui a été ajouté sont là pour « tester » l'API.


