var myIndex = 0;
var check = 0;
var timeperpage = 10000000;

carousel();
function nextStep() {
    myIndex++;
    check = 1;
    clearTimeout(timeout)
    carousel();
}
function prevStep() {
    myIndex--;
    check = 1;
    clearTimeout(timeout)
    carousel();
}
function stop() {
    clearTimeout(timeout)
    timeout = setTimeout(carousel, timeperpage * 10);

}

function carousel() {
    var i;
    var x = document.getElementsByClassName("embedded");
    if (check == 0) {
        myIndex++;
        timeout = setTimeout(carousel, timeperpage);


    }
    //following statements check what number has to come next if below 0 and over max number
    if (myIndex <= 0) myIndex = x.length;
    if (myIndex > x.length) { myIndex = 1 }
    //following statements are the ones who display
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";

    }
    x[myIndex - 1].style.display = "flex";

    if (check == 1) {
        check = 0;
        timeout = setTimeout(carousel, timeperpage);
        return;
    }
}
