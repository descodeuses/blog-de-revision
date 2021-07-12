

/*
Appeler le serveur, via l'API, 
pour obtenir la liste des billets de blog

http://monserveur/billets GET
*/

// https://developer.mozilla.org/fr/docs/Web/Guide/AJAX/Getting_Started
httpRequest = new XMLHttpRequest();
httpRequest.open('GET', '/api/billets');
httpRequest.send();
httpRequest.onreadystatechange = function() {
  if (httpRequest.readyState === XMLHttpRequest.DONE) {
    // instructions de traitement de la réponse
    let billets = JSON.parse(httpRequest.responseText)

    let ol = document.createElement("ol")
    billets.forEach(function(billet) {
      let li = document.createElement("li")
      let link = document.createElement("a")
      link.setAttribute("href", "/billet/" + billet.id)
      let content = document.createTextNode(billet.title)
      link.appendChild(content)
      li.appendChild(link)
      ol.appendChild(li)
    })
    document.getElementById("list-billets").appendChild(ol)
  }
};
