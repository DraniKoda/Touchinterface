function $(id) {
    return document.getElementById(id);
}
dragula([$("1-defaults"), $("2-defaults"), $("3-defaults"), $("4-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);

    })
dragula([$("5-defaults"), $("6-defaults"), $("7-defaults"), $("8-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);

    })
dragula([$("9-defaults"), $("10-defaults"), $("11-defaults"), $("12-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);

    })
dragula([$("13-defaults"), $("14-defaults"), $("15-defaults"), $("16-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);

    })
dragula([$("17-defaults"), $("18-defaults"), $("19-defaults"), $("20-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);

    })
dragula([$("21-defaults"), $("22-defaults"), $("23-defaults"), $("24-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);

    })
dragula([$("25-defaults"), $("26-defaults"), $("27-defaults"), $("28-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);

    })
dragula([$("29-defaults"), $("30-defaults"), $("31-defaults"), $("32-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);

    })
dragula([$("33-defaults"), $("34-defaults"), $("35-defaults"), $("36-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);

    })
dragula([$("37-defaults"), $("38-defaults"), $("39-defaults"), $("40-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);

    })
dragula([$("41-defaults"), $("42-defaults"), $("43-defaults"), $("44-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);

    })
dragula([$("45-defaults"), $("46-defaults"), $("47-defaults"), $("48-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);

    })
dragula([$("49-defaults"), $("50-defaults"), $("51-defaults"), $("52-defaults")])
    .on("drop", function (el) {
        // console.log(el.parentElement.id + "-" + el.id);
        postToServer(el.parentElement.id + "-" + el.id);

    })


function postToServer(str) {
    xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this.responseText);
        }
    };
    xhttp.open("POST", "writetotxt.php?q=" + str, true);
    xhttp.send();
}
