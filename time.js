// local Date and Time
var myVar = setInterval(setTime, 10000);

function setTime() {
    var dt = new Date();
    document.getElementById("time").innerHTML = (("0" + dt.getDate()).slice(-2)) + "." + (("0" + (dt.getMonth() + 1)).slice(-2)) + "." + (dt.getFullYear()) + " " + (("0" + dt.getHours()).slice(-2)) + ":" + (("0" + dt.getMinutes()).slice(-2));
}

setTime()