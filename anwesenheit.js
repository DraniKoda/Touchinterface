var position = { x: 0, y: 0 }

function dragMoveListener(event) {
    var target = event.target
    // keep the dragged position in the data-x/data-y attributes
    var x = (parseFloat(target.getAttribute('data-x')) || 0) + event.dx
    var y = (parseFloat(target.getAttribute('data-y')) || 0) + event.dy

    // translate the element
    target.style.webkitTransform =
        target.style.transform =
        'translate(' + x + 'px, ' + y + 'px)'

    // update the posiion attributes
    target.setAttribute('data-x', x)
    target.setAttribute('data-y', y)
}

interact('.draggable').draggable({
    // enable inertial throwing
    inertia: true,
    // keep the element within the area of it's parent
    modifiers: [
        interact.modifiers.restrictRect({
            restriction: 'parent',
            endOnly: true
        })
    ],
    // enable autoScroll
    autoScroll: true,

    // call this function on every dragmove event
    onmove: dragMoveListener,
    startAxis: 'x',
    lockAxis: 'x'
})
interact('.dropzone')
    .dropzone({
        ondrop: function (event) {
            event.target.setAttribute('data-x', event.dx)
            // alert(event.relatedTarget.id
            //     + ' was dropped into '
            //     + event.target.getAttribute('data-x'))
        },
        accept: '.draggable'
    })
    .on('dropactivate', function (event) {
        event.target.classList.add('drop-activated')
    })
