function $(id) {
    return document.getElementById(id);
}
dragula([$("1-defaults"), $("2-defaults"), $("3-defaults"), $("4-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("5-defaults"), $("6-defaults"), $("7-defaults"), $("8-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("9-defaults"), $("10-defaults"), $("11-defaults"), $("12-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("13-defaults"), $("14-defaults"), $("15-defaults"), $("16-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("17-defaults"), $("18-defaults"), $("19-defaults"), $("20-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("21-defaults"), $("22-defaults"), $("23-defaults"), $("24-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("25-defaults"), $("26-defaults"), $("27-defaults"), $("28-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("29-defaults"), $("30-defaults"), $("31-defaults"), $("32-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("33-defaults"), $("34-defaults"), $("35-defaults"), $("36-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("37-defaults"), $("38-defaults"), $("39-defaults"), $("40-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("41-defaults"), $("42-defaults"), $("43-defaults"), $("44-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("45-defaults"), $("46-defaults"), $("47-defaults"), $("48-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("49-defaults"), $("50-defaults"), $("51-defaults"), $("52-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })


function postToServer(str) {
    xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            // console.log(this.responseText);
        }
    };
    xhttp.open("POST", "writetotxt.php?q=" + str, true);
    xhttp.send();
}
var d = new Date();
DayofWeek = d.getDay();
function changeColor(element) {
    //element.parentElement.id ist 1-defaults müsste noch auf die zahl gesplittet werden um einfacher zu werden
    var numberarray = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49]
    var check = 0;
    var number = element.parentElement.id.split("-");
    // console.log(number);
    for (i = 0; i < numberarray.length; i++) {
        if (number[0] == numberarray[i]) {
            //user will be displayed blue

            if (document.getElementById(element.id).classList.contains("DO") && DayofWeek == "4" || document.getElementById(element.id).classList.contains("FR") && DayofWeek == "2") {
                console.log("orange");
                document.getElementById(element.id).classList.remove("userblue");
                document.getElementById(element.id).classList.remove("userred");
                document.getElementById(element.id).classList.add("userorange");
            } else {
                console.log("blue");
                document.getElementById(element.id).classList.remove("userorange");
                document.getElementById(element.id).classList.remove("userred");
                document.getElementById(element.id).classList.add("userblue");

            }
            check = 1;

        }
    }
    if (check == 0) {
        console.log("red");
        document.getElementById(element.id).classList.remove("userorange");
        document.getElementById(element.id).classList.remove("userblue");
        document.getElementById(element.id).classList.add("userred");
    }

}
