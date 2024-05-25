function validacion() {
    /* Asignación de variables (campos del formulario) */

    ValorMotivo = document.getElementById("motivo").selectedIndex;
    valorNombre = document.getElementById("nombre").value;
    valorApellido = document.getElementById("apellido").value;
    valorEmail = document.getElementById("email").value;
    valorMensaje = document.getElementById("mensaje").value;
    valorTerminos = document.getElementById("terminos");

    /*Validación de campos por orden de aparición*/

    if (ValorMotivo == 0) {
        document.getElementById('error_validacion').innerHTML = "* Por favor, seleccione un motivo de contacto *";
        elemento = document.getElementById('motivo');
        elemento.focus();
        return false;
    }

    else if (valorNombre.length == 0) {
        document.getElementById('error_validacion').innerHTML = "* Por favor, ingrese su nombre *";
        elemento = document.getElementById('nombre');
        elemento.focus();
        return false;
    }

    else if (valorApellido.length == 0) {
        document.getElementById('error_validacion').innerHTML = "* Por favor, ingrese su apellido *";
        elemento = document.getElementById('apellido');
        elemento.focus();
        return false;
    }

    else if (valorEmail.length == 0) {
        document.getElementById('error_validacion').innerHTML = "* Por favor, ingrese su e-mail *";
        elemento = document.getElementById('email');
        elemento.focus();
        return false;
    }

    else if (valorMensaje.length == 0) {
        document.getElementById('error_validacion').innerHTML = "* Por favor, ingrese el mensaje a enviar *";
        elemento = document.getElementById('mensaje');
        elemento.focus();
        return false;
    }

    else if (!valorTerminos.checked) {
        document.getElementById('error_validacion').innerHTML = "* Debe aceptar los términos y condiciones para continuar *";
        elemento = document.getElementById('terminos');
        elemento.focus();
        return false;
    }

    return true;
}
