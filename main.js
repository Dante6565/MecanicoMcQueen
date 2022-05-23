//Get Btn And Create Function
document.getElementById('myBtn').addEventListener('click', getData);

function getData() {

    fetch('https://randomuser.me/api/?results=100')
        .then(res => res.json())
        .then(data => {

            let author = data.results;

            let output = "<h2><center>Listado de las ultimas personas registradas</center></h2>";

            author.forEach(function (lists) {
                output += `
                <div class="container">
                    <div class="card mt-4 bg-light">
                        <ul class="list-group">
                            <li class="list-group-item"><h2>Nombre: ${lists.name.first}</h2></li>
                            <li class="list-group-item"><img src="${lists.picture.large}"></li>
                            <li class="list-group-item">Numero de telefono: ${lists.cell}</li>
                            <li class="list-group-item">DOB: ${lists.dob.date}</li>
                            <li class="list-group-item">Edad: ${lists.dob.age}</li>
                            <li class="list-group-item">Correo Electronico: ${lists.email}</li>
                            <li class="list-group-item">Genero: ${lists.gender}</li>
                            <li class="list-group-item">Ciudad: ${lists.location.city}</li>
                            <li class="list-group-item">Pais: ${lists.location.country}</li>
                            <li class="list-group-item">Codigo Postal: ${lists.location.postcode}</li>
                        </ul>
                    </div>
                </div> `;
            });

            document.getElementById('output').innerHTML = output;

        });
};

