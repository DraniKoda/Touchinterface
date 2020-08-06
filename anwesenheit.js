function $(id) {
    return document.getElementById(id);
}
dragula([$("1-defaults"), $("2-defaults"), $("3-defaults"), $("4-defaults"), $("5-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("6-defaults"), $("7-defaults"), $("8-defaults"), $("9-defaults"), $("10-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("11-defaults"), $("12-defaults"), $("13-defaults"), $("14-defaults"), $("15-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("16-defaults"), $("17-defaults"), $("18-defaults"), $("19-defaults"), $("20-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("21-defaults"), $("22-defaults"), $("23-defaults"), $("24-defaults"), $("25-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("26-defaults"), $("27-defaults"), $("28-defaults"), $("29-defaults"), $("30-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("31-defaults"), $("32-defaults"), $("33-defaults"), $("34-defaults"), $("35-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("36-defaults"), $("37-defaults"), $("38-defaults"), $("39-defaults"), $("40-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("41-defaults"), $("42-defaults"), $("43-defaults"), $("44-defaults"), $("45-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("46-defaults"), $("47-defaults"), $("48-defaults"), $("49-defaults"), $("50-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("51-defaults"), $("52-defaults"), $("53-defaults"), $("54-defaults"), $("55-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("56-defaults"), $("57-defaults"), $("58-defaults"), $("59-defaults"), $("60-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);
        changeColor(el);

    })
dragula([$("61-defaults"), $("62-defaults"), $("63-defaults"), $("64-defaults"), $("65-defaults")])
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
    var numberarray = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61]
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
