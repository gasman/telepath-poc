class BoundWidget {
    constructor(element, name) {
        var selector = ':input[name="' + name + '"]';
        this.input = element.find(selector).addBack(selector);  // find, including element itself
    }
    getValue() {
        return this.input.val();
    }
    getState() {
        return this.input.val();
    }
    setState(state) {
        this.input.val(state);
    }
}

class Widget {
    constructor(html, idForLabel) {
        this.html = html;
        this.idForLabel = idForLabel;
    }

    render(placeholder, name, id) {
        var html = this.html.replace(/__NAME__/g, name).replace(/__ID__/g, id);
        var dom = $(html);
        $(placeholder).replaceWith(dom);
        return new BoundWidget(dom, name);
    }
}
telepath.register('formfields.Widget', Widget);


class BoundRadioSelect {
    constructor(element, name) {
        this.element = element;
        this.name = name;
        this.selector = 'input[name="' + name + '"]:checked';
    }
    getValue() {
        return this.element.find(this.selector).val();
    }
    getState() {
        return this.element.find(this.selector).val();
    }
    setState(state) {
        this.element.find('input[name="' + this.name + '"]').val([state]);
    }
}

class RadioSelect extends Widget {
    render(placeholder, name, id) {
        var html = this.html.replace(/__NAME__/g, name).replace(/__ID__/g, id);
        var dom = $(html);
        $(placeholder).replaceWith(dom);
        return new BoundRadioSelect(dom, name);
    }
}
telepath.register('formfields.RadioSelect', RadioSelect);


class PageChooser {
    constructor(html, idForLabel, pageTypes, canChooseRoot, userPerms) {
        this.html = html;
        this.idForLabel = idForLabel;
        this.pageTypes = pageTypes;
        this.canChooseRoot = canChooseRoot;
        this.userPerms = userPerms;
    }

    render(placeholder, name, id) {
        var html = this.html.replace(/__NAME__/g, name).replace(/__ID__/g, id);
        var dom = $(html);
        $(placeholder).replaceWith(dom);
        return createPageChooser(id, this.pageTypes, null, this.canChooseRoot, this.userPerms);
    }
}
telepath.register('formfields.PageChooser', PageChooser);
