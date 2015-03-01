window.onload = function() {
    document.getElementById("mean").onclick = function(event) {
        document.getElementById("command-id").value = "mean";
        document.getElementById("form").submit();
    };

    document.getElementById("userLoc").onclick = function(event) {
        document.getElementById("command-id").value = "userLoc";
        document.getElementById("form").submit();
    };

    document.getElementById("userMean").onclick = function(event) {
        document.getElementById("command-id").value = "userMean";
        document.getElementById("form").submit();
    };
    document.getElementById("deleteUser").onclick = function(event) {
        document.getElementById("command-id").value = "deleteUser";
        document.getElementById("form").submit();
    };
};
