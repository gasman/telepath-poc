class Widget {
    constructor(html, idForLabel) {
        this.html = html;
        this.idForLabel = idForLabel;
    }

    render(container, name, id, value) {
        var div = document.createElement('div');
        container.appendChild(div);
        var html = this.html.replace('__NAME__', name).replace('__ID__', id);
        div.innerHTML = html;
        document.getElementById(id).value = value;
    }
}
telepath.register('formfields.Widget', Widget);
