// const config = require('./config.json')
var container = document.getElementById("container");

function showLogin() {
    var h1 = document.createElement("h1");
    h1.innerText = "Login";
    var form = document.createElement("div");
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
    button.onclick = function () {
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;
        if (email.includes("@") && password.length > 0) {
            $.post("http://127.0.0.1:5000/user/", {
                email: email,
                password: password
            }, function (result) {
                if (result.statusCode == 200) {
                    localStorage.setItem("user", result.user_name);
                    var a = document.getElementById("loginHeader");
                    var img = document.createElement("img");
                    img.src = dark ? "assets/userLight.svg" : "assets/userDark.svg";
                    img.alt = "Login";
                    a.id = "loginHeader";
                    a.href = "profile"
                    a.innerHTML = result.user_name;
                    container.innerHTML = null;
                } else {
                    var state = document.createElement("p");
                    state.classList.add("no-access");
                    state.innerHTML = "Invalid password or username!"
                    if (document.getElementsByClassName("no-access").length == 0) document.getElementsByClassName("extra")[0].append(state);
                }
            });
        }
    }
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
    var form = document.createElement("div");
    var labelUsername = document.createElement("label");
    labelUsername.innerText = "Username:";
    var inputUsername = document.createElement("input");
    inputUsername.id = inputUsername.name = inputUsername.type = "username";
    inputUsername.required = true;
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
    button.onclick = function () {
        const username = document.getElementById("username").value;
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;
        const password2 = document.getElementById("password2").value;
        const serverToken = document.getElementById("serverToken").value;
        if (password != password2) {
            var state = document.createElement("p");
            state.classList.add("no-access");
            state.innerHTML = "Passwords don't match!"
            if (document.getElementsByClassName("no-access").length != 0) document.getElementsByClassName("no-access") = null;
            else document.getElementsByClassName("extra")[0].append(state);
        } else if (email.includes("@") && username.length > 0 && password.length > 0) {
            $.post("http://127.0.0.1:5000/user/add/", {
                username: username,
                email: email,
                password: password,
                serverSecret: serverToken
            }, function (result) {
                if (result.statusCode == 200) {
                    localStorage.setItem("user", result.user_name);
                    var a = document.getElementById("loginHeader");
                    var img = document.createElement("img");
                    img.src = dark ? "assets/userLight.svg" : "assets/userDark.svg";
                    img.alt = "Login";
                    a.id = "loginHeader";
                    a.href = "profile"
                    a.innerHTML = result.user_name;
                    container.innerHTML = null;
                } else {
                    var state = document.createElement("p");
                    state.classList.add("no-access");
                    state.innerHTML = "Invalid server token!"
                    if (document.getElementsByClassName("no-access").length == 0) document.getElementsByClassName("extra")[0].append(state);
                }
            });
        }
    }
    extra.append(p);
    extra.append(button);
    form.append(labelUsername);
    form.append(inputUsername);
    form.append(labelEmail);
    form.append(inputEmail);
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