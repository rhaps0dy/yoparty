window.onload = function() {
    document.getElementById("group").onsubmit = function(event) {
        text = document.getElementById("group").children[1];
        text.value = text.value.toUpperCase();
    };
};
