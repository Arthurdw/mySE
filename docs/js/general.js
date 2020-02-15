// localStorage.setItem("mode", "light");
// localStorage.setItem("mode", "dark");
// localStorage.removeItem("mode");

// Theme:
const dark = localStorage.getItem("mode") !== "dark"

// Load The icon:
var head = document.getElementsByTagName("head")[0];
var icon = document.createElement("link");
icon.rel = "shortcut icon";
icon.href = dark ? "assets/mySE-Light.ico" : "assets/mySE-Dark.ico";
icon.type = "image/x-icon";
head.append(icon);
