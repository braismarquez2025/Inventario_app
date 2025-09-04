// Menu lateral
const menu = document.querySelector(".menu_desplegable");
const menuIcono = document.querySelector(".menu_icon");

menuIcono.addEventListener("click", () => {
  menu.classList.toggle("activo");
})

// Menu perfil
const menu_perfil = document.querySelector(".menu_perfil");
const foto_perfil = document.querySelector(".header_perfil");

foto_perfil.addEventListener("click", () => {
  menu_perfil.classList.toggle("active");
})


// Filtramos los ultimos movimientos por entrada, salida o todos
window.addEventListener("DOMContentLoaded", () => {
  function mostrarBloques(tipo) {
    const movimientos  = document.querySelectorAll(".movimiento");

    movimientos.forEach(mov => {
      if (tipo === 'todo') {
          mov.style.display = mov.classList.contains('todo') ? 'block' : 'none';
      } else {
          mov.style.display = mov.classList.contains(tipo) ? 'block' : 'none';
      }
    });
  }

  // Listeners de los botones
  const botones = document.querySelectorAll(".btn-filtro");
  botones.forEach(boton => {
    boton.addEventListener("click", () => {
      botones.forEach(b => b.classList.remove("active"));
      boton.classList.add("active");

      const tipo = boton.dataset.tipo; // "entrada" | "salida" | "todo"
      mostrarBloques(tipo);
    });
  });

  // Estado inicial: mostrar SOLO Entradas
  const activo = document.querySelector(".btn-filtro.active");
  const tipoInicial = activo ? activo.dataset.tipo : "entrada";
  mostrarBloques(tipoInicial);
});


// Ajustamos algun tamaño
const botones = [
  document.querySelector(".btn-productos_all"),
  document.querySelector(".product_delete-buttons-eliminar"),
  document.querySelector(".product_delete-buttons-volver"),
  document.querySelector(".editar_button"),
].filter(boton => boton !== null);

const esGrande = window.innerWidth > 1024;

botones.forEach(boton => {
  boton.classList.toggle("btn-lg", esGrande);
  boton.classList.toggle("btn-sm", !esGrande);
});


// Menu perfil
document.addEventListener("DOMContentLoaded", () => {
  const botones = document.querySelectorAll(".btn-perfil");
  const contenidos = document.querySelectorAll(".tab-contenido");

  botones.forEach(boton => {
    boton.addEventListener("click", () => {
      const tipo = boton.dataset.tipo;

      // Quitar activo de todos los botones
      botones.forEach(b => b.classList.remove("activo"));
      boton.classList.add("activo");

      // Ocultar todos los contenidos
      contenidos.forEach(c => c.classList.remove("activo"));

      // Mostrar solo el seleccionado
      document.getElementById(tipo).classList.add("activo");
    });
  });
});

// Campo imagen editar perfil form
document.addEventListener("DOMContentLoaded", () => {
  const inputFile = document.getElementById("id_profile_picture");
  const btnCambiar = document.getElementById("btn-cambiar");
  const btnEliminar = document.getElementById("btn-eliminar");
  const img = document.getElementById("profile-img");
  const eliminarImagen = document.getElementById("id_eliminar_imagen");

  // Abrir selector al hacer click en "Cambiar foto"
  btnCambiar.addEventListener("click", () => {
    console.log("Click en cambiar");
      inputFile.click();
  });

  // Previsualizar nueva imagen
  inputFile.addEventListener("change", () => {
      const file = inputFile.files[0];
      if (file) {
          const reader = new FileReader();
          reader.onload = (e) => {
              img.src = e.target.result;
              // Si estaba marcado para eliminar, desmarcar
              eliminarImagen.checked = false;
          };
          reader.readAsDataURL(file);
      }
  });

  // Marcar para eliminar imagen al pulsar "Eliminar foto"
  btnEliminar.addEventListener("click", () => {
    console.log("Click en eliminar");
      img.src = "https://via.placeholder.com/150"; // imagen por defecto
      inputFile.value = ""; // limpiar input
      eliminarImagen.checked = true; // marcar hidden field
  });
});
