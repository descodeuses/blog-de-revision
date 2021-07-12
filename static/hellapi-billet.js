/*
Affiche le contenu d'un billet à partir de son ID

http://monserveur/billet/<id>.json GET
*/

let splittedLocation = window.location.toString().split("/")
let id = splittedLocation[splittedLocation.length - 1]

httpRequest = new XMLHttpRequest();
httpRequest.open('GET', '/api/billet/' + id);
httpRequest.send();
httpRequest.onreadystatechange = function() {
  if (httpRequest.readyState === XMLHttpRequest.DONE) {
    // instructions de traitement de la réponse
    let billet = JSON.parse(httpRequest.responseText)

    let section = document.createElement("section")

    let title = document.createElement("h1")
    let textTitle = document.createTextNode(billet.title)
    title.appendChild(textTitle)
    section.appendChild(title)

    let texte = document.createElement("p")
    let texteContent = document.createTextNode(billet.text)
    texte.appendChild(texteContent)
    section.appendChild(texte)

    document.getElementsByTagName("body")[0].appendChild(section)

  }
};
