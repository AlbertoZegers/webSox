$(document).ready(function() {
    $("#registro-form").submit(function(event) {
      var nombre = $("#nombre").val();
      var apellido = $("#apellido").val();
      var email = $("#email").val();
      var username = $("#username").val();
      var password = $("#password").val();
      var confirm_password = $("#confirm_password").val();
  
      // Validar primer nombre y primer apellido
      if (nombre.length < 1 || apellido.length < 1) {
        alert("El primer nombre y primer apellido son obligatorios.");
        event.preventDefault();
      }
  
      // Validar email
      if (email.length < 1) {
        alert("El email es obligatorio.");
        event.preventDefault();
      }
  
      // Validar nombre de usuario
      if (username.length < 7) {
        alert("El nombre de usuario debe tener al menos 7 caracteres.");
        event.preventDefault();
      }
  
      // Validar contraseña
      var password_regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{7,}$/;
      if (!password_regex.test(password)) {
        alert("La contraseña debe tener al menos 7 caracteres y contener al menos una letra mayúscula, una letra minúscula y un número.");
        event.preventDefault();
      }
  
      // Validar confirmación de contraseña
      if (password !== confirm_password) {
        alert("La confirmación de contraseña no coincide.");
        event.preventDefault();
      }
    });
  });  