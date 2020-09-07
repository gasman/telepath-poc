document.addEventListener('DOMContentLoaded', event => {
    Array.from(document.getElementsByClassName('collage')).forEach(element => {
        var ctx = element.getContext('2d');
        var shapes = JSON.parse(element.dataset.shapes).map((shapeData) => {
            return telepath.unpack(shapeData);
        });

        setInterval(() => {
            var shape = shapes[Math.floor(Math.random() * shapes.length)];
            shape.draw(
                ctx,
                Math.random() * element.width, Math.random() * element.height
            )
        }, 100);
    });
});
