function logToConsole(message) {
    var consoleDiv = document.getElementById("console");
    consoleDiv.innerHTML += message + "<br>";
    consoleDiv.scrollTop = consoleDiv.scrollHeight;
  }

  // Capturar los mensajes de la consola y redirigirlos a la función logToConsole
  (function() {
    var originalConsoleLog = console.log;
    console.log = function(message) {
      originalConsoleLog.apply(console, arguments);
      logToConsole(message);
    };
  })();