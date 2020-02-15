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
home.href = "#";
var img = document.createElement("img");
img.src = "assets/mySE-Light.svg";
img.alt = "mySE Icon";
home.append(img);
header.append(hamburger)
header.append(home);

// Navigation Bar Generation:
var navigation = document.getElementsByTagName("nav")[0];
var ul = document.createElement("ul");
addNavBarItem("#", "Home", "assets/homeLight.svg", "Home");
addNavBarItem("docs/", "Documentation", "assets/documentationLight.svg", "Documentation");
addNavBarItem("support", "Support", "assets/supportLight.svg", "Support server");
addNavBarItem("login", "Login", "assets/userLight.svg", "Login");
function addNavBarItem(href, text, src, alt) {
    var li = document.createElement("li");
    var a = document.createElement("a");
    a.href = href;
    a.innerText = text;
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