class FieldBlock {
    constructor(name, widget, meta) {
        this.name = name;
        this.widget = telepath.unpack(widget);
        this.meta = meta;
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
        var widgetElement = dom.find('[data-streamfield-widget]').get(0);
        var boundWidget = this.widget.render(widgetElement, prefix, prefix);
        return {
            'setState': function(state) {
                boundWidget.setState(state);
            },
            'getState': function() {
                boundWidget.getState();
            },
            'getValue': function() {
                boundWidget.getValue();
            },
        };
    }
}
telepath.register('streamfield.FieldBlock', FieldBlock);


class StructBlock {
    constructor(name, childBlocks, meta) {
        this.name = name;
        this.childBlocks = childBlocks.map((child) => {return telepath.unpack(child);});
        this.meta = meta;
    }

    render(placeholder, prefix) {
        var html = $(`
            <div class="{{ classname }}">
                <span>
                    <div class="help">
                        <span class="icon-help-inverse" aria-hidden="true"></span>
                    </div>
                </span>
            </div>
        `);
        var dom = $(html);
        $(placeholder).replaceWith(dom);

        var boundBlocks = {};
        this.childBlocks.forEach(childBlock => {
            var childHtml = $(`
                <div class="field">
                    <label class="field__label"></label>
                    <div data-streamfield-block></div>
                </div>
            `);
            var childDom = $(childHtml);
            dom.append(childDom);
            var label = childDom.find('.field__label');
            label.text(childBlock.meta.label);
            var childBlockElement = childDom.find('[data-streamfield-block]').get(0);
            var boundBlock = childBlock.render(childBlockElement, prefix + '-' + childBlock.name);
            
            boundBlocks[childBlock.name] = boundBlock;
        });

        return {
            'setState': function(state) {
                for (name in state) {
                    boundBlocks[name].setState(state[name]);
                }
            },
            'getState': function() {
                var state = {};
                for (name in boundBlocks) {
                    state[name] = boundBlocks[name].getState();
                }
                return state;
            },
            'getValue': function() {
                var value = {};
                for (name in boundBlocks) {
                    value[name] = boundBlocks[name].getValue();
                }
                return value;
            },
        };
    }
}
telepath.register('streamfield.StructBlock', StructBlock);
