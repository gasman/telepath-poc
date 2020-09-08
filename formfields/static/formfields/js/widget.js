class Widget {
    constructor(html, idForLabel) {
        this.html = html;
        this.idForLabel = idForLabel;
    }

    render(container, name, id) {
        var html = this.html.replace('__NAME__', name).replace('__ID__', id);
        var dom = $(html);
        $(container).append(dom);
        return {
            getValue: function() {
                return document.getElementById(id).value;
            },
            getState: function() {
                return document.getElementById(id).value;
            },
            setState: function(state) {
                document.getElementById(id).value = state;
            },
        }
    }
}
telepath.register('formfields.Widget', Widget);
