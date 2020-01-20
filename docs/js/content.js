var titles = document.getElementsByClassName("title");
for (var i = 0; i < titles.length; ++i) {
    var selectedElement = titles[i];
    selectedElement.href = window.location.href + '#' + selectedElement.id;
    selectedElement.addEventListener("mouseover", function () { showURL(selectedElement); });
    selectedElement.addEventListener("mouseout", function () { clearURL(selectedElement); });
}

function showURL(element) {
    var sub_el = document.createElement('i');
    sub_el.classList.add("im", "im-copy", "temp-ico")
    var el = element.append(sub_el);
}

function clearURL(element) {
    var i_list = document.getElementsByClassName("temp-ico")
    for (var i = 0; i < i_list.length; ++i) {
        i_list[i].remove();
    }
}
