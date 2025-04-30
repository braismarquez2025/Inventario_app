const imagenes = [
  '../images/icon-work.svg',
  '../images/icon-play.svg',
  '../images/icon-study.svg',
  '../images/icon-exercise.svg',
  '../images/icon-social.svg',
  '../images/icon-self-care.svg',
]

const colors = [
  '#FF8B64',
  '#55C2E6',
  '#FF5E7D',
  '#4BCF82',
  '#7335D2',
  '#F1C75B',
]
    


fetch("data.json")
.then((response) => {
    if (!response.ok) {
      throw new Error("Error al cargar el archivo JSON");
    }
    return response.json();
  })
    .then((actividades) => {
        actividades.forEach((actividad, index) => {

          let contenedores = document.querySelectorAll(".item");

          // Comprobamos que existen los contenedores suficientes
          if (contenedores.length < actividades.length || imagenes.length < actividades.length) {
            console.warn("Hay más actividades que contenedores disponibles");
          }

          let contenedor = contenedores[index];

          // Iteramos por cada contenedor
          if (contenedor) {

            // Creamos el div con la clase head para cada actividad
            let div = document.createElement("div");
            div.className = "item_head";

            // Creamos el titulo con un p y lo añadimos al div
            let p = document.createElement("p");
            p.classList = "text-preset-5-medium";
            p.innerHTML = `${actividad.title}`;
            div.appendChild(p);

  
            let imagen = document.getElementById("img-puntos");

            if (imagen) {
              let imagenClonada = imagen.cloneNode(true);
              div.appendChild(imagenClonada); 
            }

            // Añadimos el div que acabamos de crear al contenedor correspondiente del html
            contenedor.appendChild(div);

            let divContent = document.createElement("div");
            divContent.className = "item_text"

            // Creamos el h1 y el p con las horas correspondientes
            let titulo = document.createElement("h1");
            titulo.className = "title text-preset-3";
            titulo.innerHTML = `${actividad.timeframes.daily.current}hrs`;

            let parrafo = document.createElement("p");
            parrafo.className = "subtitle text-preset-6";
            parrafo.innerHTML = `Last week - ${actividad.timeframes.daily.previous}hrs`;

            // Agregamos el texto al div
            divContent.appendChild(titulo);
            divContent.appendChild(parrafo);


            // Agregamos al item el div con el h1 y el p
            contenedor.appendChild(divContent);

            // Modificamos el before del item para cambiar la imagen
            contenedor.style.setProperty('--background-image', `url(${imagenes[index]})`);

            // También modificamos el color de fondo
            contenedor.style.setProperty('--bg-color', colors[index]);

             // Creamos los eventos para cambiar las horas segun el tiempo
            let dia = document.getElementById("dia");
            let semana = document.getElementById("semana");
            let mes = document.getElementById("mes");

            dia.addEventListener(('click'), function() {
              titulo.innerHTML = `${actividad.timeframes.daily.current}hrs`;
              parrafo.innerHTML = `Last week - ${actividad.timeframes.daily.previous}hrs`;
            })

            semana.addEventListener(('click'), function() {
              titulo.innerHTML = `${actividad.timeframes.weekly.current}hrs`;
              parrafo.innerHTML = `Last week - ${actividad.timeframes.weekly.previous}hrs`;
            })

            mes.addEventListener(('click'), function() {
              titulo.innerHTML = `${actividad.timeframes.monthly.current}hrs`;
              parrafo.innerHTML = `Last week - ${actividad.timeframes.monthly.previous}hrs`;
            })
          } 
        })
    })
    .catch((error) => console.error("Error:", error));

      

     
     

    
        



