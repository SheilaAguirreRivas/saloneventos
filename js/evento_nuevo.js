function guardar(){
    let f = document.getElementById('fechaEvento').value;
    let n = document.getElementById('nombreApellido').value;
    let c = document.getElementById('numContacto').value;
    let t = document.getElementById('tipoEvento').value;
    let v = document.getElementById('valorSalon').value;
    let i = document.getElementById('cantInvitados').value;
    let r = document.getElementById('responsable').value;

    let evento = {
        fechaEvento: f,
        nombreApellido: n,
        numContacto: c,
        tipoEvento: t,
        valorSalon: v,
        cantInvitados: i,
        responsable: r
    }

    let url = 'https://sheiaguirrer.pythonanywhere.com/eventos';
    //'http://127.0.0.1:5000/eventos'
    //'http://sheiaguirrer.pythonanywhere.com/eventos',

    let options ={
        body: JSON.stringify(evento),
        method: 'POST',
        headers: {'Content-Type': 'application/json'}
    };

    fetch(url, options)
        .then(function(){
            alert('Evento guardado exitosamente');
            window.location.href = './eventos.html';
        })
        .catch((error)=>{
            alert('No pudo guardarse el nuevo evento');
            console.error(error);
        })
}
