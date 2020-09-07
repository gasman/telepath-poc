class Rectangle {
    constructor(width, height, colour) {
        this.width = width;
        this.height = height;
        this.colour = colour;
    }

    draw(ctx, x, y) {
        ctx.fillStyle = this.colour;
        ctx.fillRect(x, y, this.width, this.height);
    }
}
