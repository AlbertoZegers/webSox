$(document).ready(function() {
    $('#login-form').submit(function(event) {
      // Validar el nombre de usuario
      var username = $('#username').val();
      if (username.length < 6) {
        event.preventDefault();
        $('#username').after('<div class="error">El nombre de usuario debe tener al menos 6 caracteres.</div>');
      }
      
      // Validar la contraseña
      var password = $('#password').val();
      var passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{6,}$/;
      if (!passwordRegex.test(password)) {
        event.preventDefault();
        $('#password').after('<div class="error">La contraseña debe tener al menos 6 caracteres, incluyendo al menos una letra mayúscula, una letra minúscula y un número.</div>');
      }
    });
  });  