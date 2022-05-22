const form = document.querySelector("form"),
        nextBtn = form.querySelector(".nextBtn"),
        backBtn = form.querySelector(".backBtn"),
        allInput = form.querySelectorAll(".first input");


nextBtn.addEventListener("click", ()=> {
    allInput.forEach(input => {
        if(input.value != ""){
            form.classList.add('secActive');
        }else{
            form.classList.remove('secActive');
        }
    })
})
backBtn.addEventListener("click", () => form.classList.remove('secActive'));

function buscar()
{
    var valor_a_buscar=document.getElementById('barrabuscadora').value;
    valor_a_buscar = valor_a_buscar.toUpperCase();
    var lista_palabras= ['JAVIER GONZALES','RODRIGO SANCHEZ','GONZALO PEÑALOZA']
    if(lista_palabras.includes(valor_a_buscar))
    {
        if(valor_a_buscar==lista_palabras[0])
        {
            window.open("JavierGonzales.html")
        }
        else if(valor_a_buscar==lista_palabras[1])
        {
            window.open("RodrigoSanchez.html")
        }
        else if(valor_a_buscar==lista_palabras[2])
        {       
            window.open("GonzaloPeñaloza.html")
        }
    }
    else
    {
        alert("No se encontro la palabra o oración buscada");
    }
}

function login (){
    var user, pass;
    user= document.getElementById("user_email").value;
    pass= document.getElementById("password-toggle-input-88cd08fd").value;
    if(user =="javgon@mec.cl" && pass=="1234"){
        window.location="loginsucessmec.html"
    }
}