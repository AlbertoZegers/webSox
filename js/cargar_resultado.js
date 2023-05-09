$("#enviar").click(function(event) {
    event.preventDefault();
  
    var palabra = $("#palabra").val();
    if (!isNaN(palabra)) {
      //alert("Por favor ingrese una palabra válida");
      var $errorTipo = $("<h2>").text("Por favor ingrese una palabra válida");
      $("#resultado").empty();
      $('#resultado').append($errorTipo);
      return;
  }
    var url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + palabra;
  
    fetch(url)
      .then(response => response.json())
      .then(data => {
        var $palabra = $("<h2>").text(data[0].word);
        var $tipo = $("<p>").text(data[0].meanings[0].partOfSpeech);
        var $definicion = $("<p>").text(data[0].meanings[0].definitions[0].definition);
        var $ejemplo = $("<p>").text(data[0].meanings[0].definitions[0].example);
  
        $("#resultado").empty();
        $('#resultado')
          .append($palabra)
          .append($tipo)
          .append($definicion)
          .append($ejemplo);
  
      })
      .catch(error => {
        //alert("Palabra no encontrada");
        console.error(error);
        var $errorFound = $("<h2>").text("Palabra no encontrada");
        $("#resultado").empty();
        $('#resultado').append($errorFound);
      });
  });