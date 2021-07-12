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

https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop

https://replit.com/