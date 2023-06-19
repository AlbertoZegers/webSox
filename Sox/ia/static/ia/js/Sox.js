$(document).ready(function() {
      function modulo(texto) {
        var lista_saludos = ["hola", "buenas", "buenos días", "buenos dias", "buenas tardes", "buenas noches"];
        if (lista_saludos.includes(texto)) {
          var resultado = "Sox: " + texto + " ¿En qué puedo ayudarte?";
          return resultado;
        } else if (texto === "help") {
          var resultado = "<pre>\tManual de usuario\nSaludos aceptados:\n-hola\n-buenas\n-buenos días\n-buenas tardes\n-buenas noches</pre>";
          return resultado;
        } else {
          var resultado = "Sox: ...";
          return resultado;
        }
      }

      $("#btnEnviar").click(function(event) {
        event.preventDefault()
        var texto = $("#campoTexto").val();
        var resultado = modulo(texto);
        $("#resultadoDiv").html(resultado);
      });
    });
