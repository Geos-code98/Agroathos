function enviaycerrar() {
    if (confirm('¿Estas seguro de enviar este formulario?')) {
       window.close();
       document.Produccionform.submit();
    }
     
}

