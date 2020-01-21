var t0 = Date.now(); console.log("Started loading content JS.")

var titles = document.getElementsByClassName("title");
for (var i = 0; i < titles.length; ++i) {
    var selectedElement = titles[i];
    selectedElement.href = '#' + selectedElement.id;
    selectedElement.title = "Get the permanent link.";
    selectedElement.addEventListener("mouseout", function () { clearURL(); });
}

function showURL(element) {
    var whiteSpace = document.createElement("span");
    whiteSpace.innerHTML = " ";
    whiteSpace.classList.add("whiteSpace")
    var sub_el = document.createElement('i');
    sub_el.classList.add("im", "im-copy", "temp-ico")
    element.append(whiteSpace);
    element.append(sub_el);
}

function clearURL() {
    removeAll("temp-ico");
    removeAll("whiteSpace");
    function removeAll(item) {
        var itemList = document.getElementsByClassName(item);
        for (var i = 0; i < itemList.length; ++i) { itemList[i].remove(); }
    }
}

var t1 = Date.now(); console.log("It took " + Math.round((t1 - t0) * 100) / 100 + " millisecond(s) to load the content JS file.")
