let flecha = document.getElementById("flecha");
let contenido = document.getElementById("contenido");

flecha.addEventListener('click', function() {
  if (contenido.style.display === "flex") {
    contenido.style.display = "none";  
  } else {
    contenido.style.display = "flex";  
  }
});