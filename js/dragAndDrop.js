/*
***************************************************
  Universidad CENFOTEC invierte tiempo y recursos en el desarrollo de 
  contenidos Open Source.  Apoye las actividades de la Universidad,
  y cualqueir modificación compártla de forma abierta

  Desarrollado por Jeffry Valverde
  MIT license, all text above must be included in any redistribution
 ****************************************************
*/

var stringInter = "";
var lists = document.getElementsByClassName("list");
var dropArea = document.querySelector(".dropArea");
var btnPlay = document.querySelector("#btnPlay");
var btnFlotante = document.querySelector(".btnFlotante");
var selectedElement = null;
var touchClone = null;
var hostname = window.location.hostname;
var port = window.location.port;

for (var list of lists) {
  list.addEventListener("dragstart", function (e) {
    selectedElement = e.target;
  });

  list.addEventListener("touchstart", function (e) {
    selectedElement = e.target;
    touchClone = selectedElement.cloneNode(true);
    touchClone.style.position = "absolute";
    touchClone.style.pointerEvents = "none";
    document.body.appendChild(touchClone);
  });
}

dropArea.addEventListener("dragover", function (e) {
  e.preventDefault();
});

dropArea.addEventListener("drop", function (e) {
  e.preventDefault();
  if (selectedElement !== null) {
    this.appendChild(selectedElement.cloneNode(true));
    selectedElement = null;
  }
});

document.addEventListener("touchmove", function (e) {
  if (touchClone) {
    var touch = e.touches[0];
    touchClone.style.left = touch.clientX + "px";
    touchClone.style.top = touch.clientY + "px";
  }
});

document.addEventListener("touchend", function (e) {
  if (touchClone) {
    var touch = e.changedTouches[0];
    var element = document.elementFromPoint(touch.clientX, touch.clientY);
    if (element === dropArea) {
      dropArea.appendChild(selectedElement.cloneNode(true));
    }
    document.body.removeChild(touchClone);
    touchClone = null;
    selectedElement = null;
  }
});

btnPlay.addEventListener("click", function () {
  var count = 0;
  stringInter = "";
  var divs = dropArea.querySelectorAll("div");
  divs.forEach(function (div) {
    if (count !== divs.length - 1) {
      stringInter += div.getAttribute("data-value") + ":";
      count += 1;
    } else {
      stringInter += div.getAttribute("data-value");
    }
  });
  var data = { dato: stringInter };

  fetch(`http://${hostname}:${port}/data`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  }).catch((error) => {
    console.error("Error:", error);
  });
});

btnFlotante.addEventListener("click", function () {
  dropArea.innerHTML = "";
});
