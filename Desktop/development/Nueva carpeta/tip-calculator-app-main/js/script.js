let numeroUsuario = document.getElementById("numero_user");
let numeroPersonas = document.getElementById("numero_personas")
let custom = document.getElementById("custom");
let grid = document.getElementById("grid");
let diverror = document.getElementById("personas_error");
let error = document.getElementById("error");

let cantidadDinero;
let cantidadPersonas;
let porcentaje;


// Damos estilos a los inputs
numeroUsuario.classList.add("estilos");
numeroUsuario.classList.add("text-preset-3");

numeroPersonas.classList.add("estilos");
numeroPersonas.classList.add("text-preset-3");

// Creamos mensaje de error
let p = document.createElement("p");
p.innerHTML = "Can't be zero";
p.classList.add("text-preset-5");
p.classList.add("color-text");

let mensaje_error = document.createElement("p");
mensaje_error.innerHTML = "Select a number";
mensaje_error.classList.add("text-preset-5");
mensaje_error.classList.add("color-text");


// Damos estilos al mensaje de error
document.addEventListener("input", (event) => {
    
    if (event.target == numeroUsuario && numeroPersonas.value == "") {
        numeroPersonas.classList.add("border-rojo");
        diverror.appendChild(p);
    } else {
        numeroPersonas.classList.remove("border-rojo");
        p.remove();
    }

    if (event.target == numeroPersonas && numeroUsuario.value == "") {
        numeroUsuario.classList.add("border-rojo");
        error.appendChild(mensaje_error);
    } else {
        numeroUsuario.classList.remove("border-rojo");
        mensaje_error.remove();
    }

    cantidadDinero = numeroUsuario.value;
    cantidadPersonas = numeroPersonas.value;
    calculo();
});



// Input costum
custom.addEventListener("click", () => {
    let input = document.createElement("input");
    input.type = "number";
    input.classList = "input-custom";
    input.placeholder = "0.00";
    input.classList.add("estilos");
    input.classList.add("text-preset-3");
    
    input.addEventListener("input", () => {
        porcentaje = input.value;
    })

    setTimeout(() => {
        input.focus();
      }, 0);
    

    custom.style.display = "none";
    grid.appendChild(input);

    input.addEventListener("blur", () => {
        input.remove();
        custom.style.display = "block";
    });

    calculo();
})

// Obtengo el valor del porcentaje personalizado
grid.addEventListener("click", (event) => {
    let texto = event.target.textContent;
    porcentaje = texto.replace('%', '');
    
    calculo();
})


let precio_persona = document.getElementById("cantidad-persona");
let precio_total = document.getElementById("cantidad-total");

// Creo esta funcion para realizar los calculos
function calculo() {
    let resultadoPersona;
    let resultadoTotal;
    let dinero = parseFloat(cantidadDinero);
    let porc = parseFloat(porcentaje);
    let personas = parseFloat(cantidadPersonas);

    if (!isNaN(dinero) && !isNaN(porc) && !isNaN(personas)) {
        resultadoPersona = (dinero * porc) / 100;
        resultadoTotal = (dinero / personas) + resultadoPersona;
        
        precio_persona.innerHTML = "$" + resultadoPersona.toFixed(2);
        precio_total.innerHTML = "$" + resultadoTotal.toFixed(2);
        
    }

    let reset = document.getElementById("reset");

    // Añadimos un evento al boton de reset
    reset.addEventListener("click", () => {
        cantidadDinero = null;
        porcentaje = null;
        cantidadPersonas = null;
        precio_persona.innerHTML = "$0.00";
        precio_total.innerHTML = "$0.00";
        document.getElementById("numero_user").value = '';
        document.getElementById("numero_personas").value = '';
    })
}

    
