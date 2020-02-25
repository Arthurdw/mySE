// const config = require('./config.json')
var container = document.getElementById("container");

function showLogin() {
    var h1 = document.createElement("h1");
    h1.innerText = "Login";
    var form = document.createElement("form");
    form.method = "POST";
    form.onsubmit = "redirHome()";
    var labelEmail = document.createElement("label");
    labelEmail.innerText = "Email:";
    var inputEmail = document.createElement("input");
    inputEmail.id = inputEmail.name = inputEmail.type = "email";
    inputEmail.required = true;
    var labelPassword = document.createElement("label");
    labelPassword.innerText = "Password:";
    var inputPassword = document.createElement("input");
    inputPassword.id = inputPassword.type = inputPassword.name = "password";
    inputPassword.required = true;
    var extra = document.createElement("div");
    extra.classList.add("extra");
    var p = document.createElement("p");
    p.innerHTML = 'Don\'t have an account?<br><span onclick="createAcc();" class="url" id="createAccount">Create an account</span>';
    var button = document.createElement("button");
    button.id = "login";
    button.type = "submit";
    button.classList.add("submit");
    button.innerText = "Login";
    extra.append(p);
    extra.append(button);
    form.append(labelEmail);
    form.append(inputEmail);
    form.append(labelPassword);
    form.append(inputPassword);
    form.append(extra);
    container.append(h1);
    container.append(form);
}

function createAccount() {
    var h1 = document.createElement("h1");
    h1.innerText = "Create account";
    var form = document.createElement("form");
    var labelEmail = document.createElement("label");
    labelEmail.innerText = "Email:";
    var inputEmail = document.createElement("input");
    inputEmail.id = inputEmail.name = inputEmail.type = "email";
    inputEmail.required = true;
    var labelPassword = document.createElement("label");
    labelPassword.innerText = "Password:";
    var inputPassword = document.createElement("input");
    inputPassword.id = inputPassword.type = inputPassword.name = "password";
    inputPassword.required = true;
    var labelPassword2 = document.createElement("label");
    labelPassword2.innerText = "Retype password:";
    var inputPassword2 = document.createElement("input");
    inputPassword2.id = inputPassword2.name = "password2";
    inputPassword2.type = "password";
    inputPassword2.required = true;
    var labelServerToken = document.createElement("label");
    labelServerToken.innerText = "Server token:";
    var inputServerToken = document.createElement("input");
    inputServerToken.id = inputServerToken.type = inputServerToken.name = "serverToken";
    inputServerToken.required = true;
    var extra = document.createElement("div");
    extra.classList.add("extra");
    var p = document.createElement("p");
    p.innerHTML = 'Already have an account?<br><span onclick="showLog();" class="url" id="loginAccount">Login to your account</span>';
    var button = document.createElement("button");
    button.id = "createAcount";
    button.classList.add("submit");
    button.innerText = "Create account";
    extra.append(p);
    extra.append(button);
    form.append(labelEmail);
    form.append(inputEmail);
    form.append(labelPassword);
    form.append(inputPassword);
    form.append(labelPassword2);
    form.append(inputPassword2);
    form.append(labelServerToken);
    form.append(inputServerToken);
    form.append(extra);
    container.append(h1);
    container.append(form);
}

function createAcc() {
    container.innerHTML = null;
    createAccount();
}

function showLog() {
    container.innerHTML = null;
    showLogin();
}

showLogin();

function redirHome() {
    window.location.replace('index');
}

redirHome();

// config.serverUrl
$("#login").click(function(){
    const email = document.getElementById("email");
    console.log(email.innerText);
    $.post("127.0.0.1:5000", function(data, status){
        alert("Data: " + data + "\nStatus: " + status);
    });
  });