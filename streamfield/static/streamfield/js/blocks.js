class FieldBlock {
    constructor(field) {
        this.field = telepath.unpack(field);
    }

    render(placeholder, prefix) {
        var html =$(`
        <div>
            <div class="field-content">
                <div class="input">
                    <div data-streamfield-widget></div>
                    <span></span>
                </div>
                <p class="help"></p>
                <p class="error-message"></p>
            </div>
        </div>
        `);
        var dom = $(html);
        $(placeholder).replaceWith(dom);
        var fieldElement = dom.find('[data-streamfield-widget').get(0);
        var widget = this.field.render(fieldElement, prefix, prefix);
        return widget;
    }
}
telepath.register('streamfield.FieldBlock', FieldBlock);
