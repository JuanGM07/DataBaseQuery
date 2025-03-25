function enviarConsulta() {
    // Obtener la consulta escrita por el usuario
    let query = document.getElementById("userQuery").value;

    // Enviar la consulta al servidor a través de una solicitud POST
    fetch('/consulta', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: query })  // Enviamos la consulta en formato JSON
    })
    .then(response => response.json())  // Esperamos la respuesta del servidor en formato JSON
    .then(data => {
        let resultado = document.getElementById("resultado");
        
        // Si la respuesta contiene un campo 'response', mostramos la respuesta generada
        if (data.response) {
            resultado.innerHTML = data.response;
        } else {
            // En caso de error, mostramos el error generado por el servidor
            resultado.innerHTML = 'Error: ' + data.error;
        }
    })
    .catch(error => {
        // Manejo de errores en caso de que la solicitud falle
        let resultado = document.getElementById("resultado");
        resultado.innerHTML = 'Error al realizar la consulta. ' + error.message;
    });
}
