var myIndex = 0;
var check = 0;
carousel();
function nextStep() {
    myIndex++;
    check = 1;
    carousel();
}
function prevStep() {
    myIndex--;
    check = 1;
    carousel();
    if (myIndex <= 1) myindex = 1;
}

function carousel() {
    var i;
    var x = document.getElementsByClassName("embedded");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";

    }
    if (myIndex <= 0) myIndex = x.length;
    if (check == 0) {
        myIndex++;
        setTimeout(carousel, 5000);

    }
    if (myIndex > x.length) { myIndex = 1 }
    x[myIndex - 1].style.display = "block";
    if (check == 1) {
        check = 0;
        return
    }
}
