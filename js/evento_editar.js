//console.log(location.search)

let argsUrl = location.search.substring(1).split('&');
console.log(argsUrl)

let data = [];
for(let i = 0; i < argsUrl.length; i++){
    data[i] = argsUrl[i].split('=');
}
console.log(data)

document.getElementById('id').value = decodeURIComponent(data[0][1]);
document.getElementById('fechaEvento').value = decodeURIComponent(data[1][1]);
document.getElementById('nombreApellido').value = decodeURIComponent(data[2][1]);
document.getElementById('numContacto').value = decodeURIComponent(data[3][1]);
document.getElementById('tipoEvento').value = decodeURIComponent(data[4][1]);
document.getElementById('valorSalon').value = decodeURIComponent(data[5][1]);
document.getElementById('cantInvitados').value = decodeURIComponent(data[6][1]);
document.getElementById('responsable').value = decodeURIComponent(data[7][1]);

function modificar(){
    // Actualizar el evento en la BBDD
    let id = document.getElementById('id').value;
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

    let url = 'http://127.0.0.1:5000/eventos/'+id;
    //'http://127.0.0.1:5000/eventos/'+id;
    //let url = 'http://sheiaguirrer.pythonanywhere.com/eventos/'+id;



    let options ={
        body: JSON.stringify(evento),
        method: 'PUT',
        headers: {'Content-Type': 'application/json'},
    };

    fetch(url, options)
    .then(function(){
        alert('Registro modificado exitosamente');
        window.location.href= './eventos.html';
    })
    .catch(err => {
        alert('No pudo modificarse el registro');
        console.error(err);
    })
}

