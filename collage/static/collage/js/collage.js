document.addEventListener('DOMContentLoaded', event => {
    canvas = document.getElementById('collage');
    var shapes = JSON.parse(canvas.dataset.shapes).map((shapeData) => {
        return telepath.unpack(shapeData);
    });

    var ctx = canvas.getContext('2d');
    setInterval(() => {
        var shape = shapes[Math.floor(Math.random() * shapes.length)];
        shape.draw(
            ctx,
            Math.random() * canvas.width, Math.random() * canvas.height
        )
    }, 100);
});
