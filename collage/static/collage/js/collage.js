document.addEventListener('DOMContentLoaded', event => {
    canvas = document.getElementById('collage');
    var ctx = canvas.getContext('2d');
    var shapes = JSON.parse(canvas.dataset.shapes).map((shapeData) => {
        return telepath.unpack(shapeData);
    });

    setInterval(() => {
        var shape = shapes[Math.floor(Math.random() * shapes.length)];
        shape.draw(
            ctx,
            Math.random() * canvas.width, Math.random() * canvas.height
        )
    }, 100);
});
