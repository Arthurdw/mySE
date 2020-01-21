var t0 = Date.now(); console.log("Started loading content JS.")

var titles = document.getElementsByClassName("title");
for (var i = 0; i < titles.length; ++i) {
    var selectedElement = titles[i];
    selectedElement.href = '#' + selectedElement.id;
    selectedElement.title = "Get the permanent link.";
    selectedElement.addEventListener("mouseover", function () { showURL(selectedElement); });
<<<<<<< HEAD
    selectedElement.addEventListener("mouseout", function () { clearURL(); });
=======
    selectedElement.addEventListener("mouseout", function () { clearURL(selectedElement); });
>>>>>>> 0379c86e30d86dbf8c4ee029f0c38e247929e6f7
}

function showURL(element) {
    var sub_el = document.createElement('i');
    sub_el.classList.add("im", "im-copy", "temp-ico")
    element.append(sub_el);
}

function clearURL() {
    var i_list = document.getElementsByClassName("temp-ico")
    for (var i = 0; i < i_list.length; ++i) {
        i_list[i].remove();
    }
}
<<<<<<< HEAD

var t1 = Date.now(); console.log("It took " + Math.round((t1 - t0) * 100) / 100 + " millisecond(s) to load the content JS file.")
=======
>>>>>>> 0379c86e30d86dbf8c4ee029f0c38e247929e6f7
