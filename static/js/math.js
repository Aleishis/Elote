// Evento que se dispara cuando se termina de cargar el DOM
// DOM: Document Object Model
document.addEventListener("DOMContentLoaded", function(){

    // Declaramos una variable en JS que representa el "btn-ok" en el HTML
    var btnSumar = document.getElementById("btn-sumar");

    // Declaramos un evento "click" a ese boton
    btnSumar.addEventListener("click", function(){
        // Declaramos una variable que representa el input del HTML
        var value1Number = parseFloat(document.getElementById("input-value1").value);
        
        var value2Number = parseFloat(document.getElementById("input-value2").value)


        // isNaN = is not a number
        if (isNaN(value1Number) || isNaN(value2Number)){
            alert("Estas estupido")
        }

        var resultado = value1Number + value2Number
        // Mostamos alerta del navegador con el contenido del input
        alert("El resultado es: " + resultado)

    })

    var btnRestar = document.getElementById("btn-restar");

    btnRestar.addEventListener("click", function(){
        // Declaramos una variable que representa el input del HTML
        var value1Number = parseFloat(document.getElementById("input-value1").value);
        
        var value2Number = parseFloat(document.getElementById("input-value2").value)


        // isNaN = is not a number
        if (isNaN(value1Number) || isNaN(value2Number)){
            alert("Estas estupido")
        }

        var resultado = value1Number - value2Number
        // Mostamos alerta del navegador con el contenido del input
        alert("El resultado es: " + resultado)
    })

    var btnMultiplicar = document.getElementById("btn-multiplicar");

    btnMultiplicar.addEventListener("click", function(){
        // Declaramos una variable que representa el input del HTML
        var value1Number = parseFloat(document.getElementById("input-value1").value);
        
        var value2Number = parseFloat(document.getElementById("input-value2").value)


        // isNaN = is not a number
        if (isNaN(value1Number) || isNaN(value2Number)){
            alert("Estas estupido")
        }

        var resultado = value1Number * value2Number
        // Mostamos alerta del navegador con el contenido del input
        alert("El resultado es: " + resultado)
    })

    var btnDividir = document.getElementById("btn-dividir");

    btnDividir.addEventListener("click", function(){
        // Declaramos una variable que representa el input del HTML
        var value1Number = parseFloat(document.getElementById("input-value1").value);
        
        var value2Number = parseFloat(document.getElementById("input-value2").value)


        // isNaN = is not a number
        if (isNaN(value1Number) || isNaN(value2Number)){
            alert("Estas estupido")
        }

        var resultado = value1Number / value2Number
        // Mostamos alerta del navegador con el contenido del input
        alert("El resultado es: " + resultado)
    })
    
})