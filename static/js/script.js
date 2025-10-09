// Evento que se dispara cuando se termina de cargar el DOM
// DOM: Document Object Model
document.addEventListener("DOMContentLoaded", function(){

    // Declaramos una variable en JS que representa el "btn-ok" en el HTML
    var btnOk = document.getElementById("btn-ok");

    // Declaramos un evento "click" a ese boton
    btnOk.addEventListener("click", function(){
        // Declaramos una variable que representa el input del HTML
        var name = document.getElementById("input-name");
        
        // Mostamos alerta del navegador con el contenido del input
        alert("Hello world " + name.value);
        console.log("Se imprimio el hola mundo");
        console.error("Este es un error simulado");
    })
    
})