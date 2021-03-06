// Website Header Generation:
var header = document.getElementsByTagName("header")[0];
var hamburger = document.createElement("button");
hamburger.id = "hamburger";
hamburger.classList.add("hamburger", "hamburger--slider");
hamburger.type = "button";
var hamburgerBox = document.createElement("span");
hamburgerBox.classList.add("hamburger-box");
var hamburgerInner = document.createElement("span")
hamburgerInner.classList.add("hamburger-inner");
hamburgerBox.append(hamburgerInner);
hamburger.append(hamburgerBox);
var home = document.createElement("a");
home.href = "index";
var img = document.createElement("img");
img.src = dark ? "assets/mySE-Light.svg" : "assets/mySE-Dark.svg";
img.alt = "mySE Icon";
home.append(img);
header.append(hamburger)
header.append(home);

// Navigation Bar Generation:
var navigation = document.getElementsByTagName("nav")[0];
var ul = document.createElement("ul");
var user = localStorage.getItem("user");
addNavBarItem("https://arthurdw.github.io/mySE/", "Home", dark ? "assets/homeLight.svg" : "assets/homeDark.svg", "Home");
addNavBarItem("https://github.com/Arthurdw/mySE", "Github", dark ? "assets/githubLight.svg" : "assets/githubDark.svg", "Github", null, "_blanc");
addNavBarItem("documentation", "Documentation", dark ? "assets/documentationLight.svg" : "assets/documentationDark.svg", "Documentation");
addNavBarItem("support", "Support", dark ? "assets/supportLight.svg" : "assets/supportDark.svg", "Support server");
addNavBarItem(user == null ? "login" : "profile", user == null ? "Login" : user, dark ? "assets/userLight.svg" : "assets/userDark.svg", "Login", "loginHeader");
function addNavBarItem(href, text, src, alt, id=null, target="_self") {
    var li = document.createElement("li");
    var a = document.createElement("a");
    a.href = href;
    a.innerText = text;
    if (id != null) a.id = id;
    a.target = target
    var img = document.createElement("img");
    img.src = src;
    img.alt = alt;
    a.append(img);
    li.append(a);
    ul.append(li);
}
navigation.append(ul);

// When a person clicks on a hamburger:
$("#hamburger").click(function () {
    $(this).toggleClass("is-active");
    $('nav').toggleClass('active');
})