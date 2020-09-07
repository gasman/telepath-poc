class Circle {
    constructor(radius, colour) {
        this.radius = radius;
        this.colour = colour;
    }

    draw(ctx, x, y) {
        ctx.fillStyle = this.colour;
        ctx.beginPath();
        ctx.arc(x, y, this.radius, 0, 2 * Math.PI);
        ctx.fill();
    }
}
