class BoundWidget {
    constructor(id) {
        this.id = id;
    }
    getValue() {
        // FIXME: getElementById won't work for radio buttons / checkboxes
        return document.getElementById(this.id).value;
    }
    getState() {
        return document.getElementById(this.id).value;
    }
    setState(state) {
        document.getElementById(this.id).value = state;
    }
}

class Widget {
    constructor(html, idForLabel) {
        this.html = html;
        this.idForLabel = idForLabel;
    }

    render(container, name, id) {
        var html = this.html.replace(/__NAME__/g, name).replace(/__ID__/g, id);
        var dom = $(html);
        $(container).append(dom);
        return new BoundWidget(id);
    }
}
telepath.register('formfields.Widget', Widget);


class PageChooser {
    constructor(html, idForLabel, pageTypes, canChooseRoot, userPerms) {
        this.html = html;
        this.idForLabel = idForLabel;
        this.pageTypes = pageTypes;
        this.canChooseRoot = canChooseRoot;
        this.userPerms = userPerms;
    }

    render(container, name, id) {
        var html = this.html.replace(/__NAME__/g, name).replace(/__ID__/g, id);
        var dom = $(html);
        $(container).append(dom);
        return createPageChooser(id, this.pageTypes, null, this.canChooseRoot, this.userPerms);
    }
}
telepath.register('formfields.PageChooser', PageChooser);
