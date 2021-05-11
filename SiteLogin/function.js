let sen = 1234
let us = "kauã"

function senha(){
    let senha = window.document.getElementById("pass")
    if(senha.type=="password") {
        senha.type="text"
    } else {
        senha.type="password"
    }
}
function entrou(){
    let bot = window.document.getElementById("logar")
    bot.style.backgroundColor="rgba(0, 0, 0, 0.2)"
}
function saiu(){
    let bot = window.document.getElementById("logar")
    bot.style.backgroundColor="rgba(0, 0, 0, 0.116)"
}

function logar(){
    let domuser = window.document.getElementById("user")
    let dompass = window.document.getElementById("pass")
    let senha = window.document.getElementById("pass")
    let user = window.document.getElementById("user")
    if(senha.value == "" || user.value == ""){
        domuser.style.borderColor = "rgba(255, 0, 0, .4)"
        dompass.style.borderColor = "rgba(255, 0, 0, .4)"
        let lab = document.getElementById("label")
        lab.innerHTML = "Verifique os dados e Tente Novamente"
        domuser.value=""
        dompass.value=""    
    }
    if(senha.value != sen || user.value != us){
        domuser.style.borderColor = "rgba(255, 0, 0, .4)"
        dompass.style.borderColor = "rgba(255, 0, 0, .4)"
        let lab = document.getElementById("label")
        lab.innerHTML = "Verifique os dados e Tente Novamente"
        domuser.value=""
        dompass.value=""
    }
    if(senha.value == sen && user.value == us){
        window.location.href = './logado/logado.html';
    }
}