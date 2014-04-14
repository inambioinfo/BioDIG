var deps = ['jquery', 'underscore', 'text!biodig/tmpl/taggable.html'];

define(deps, function($, _, TaggableTmpl) {

    function TaggableImage(selector, opts) {
        // check to see if features were directly requested
        // otherwise use the "mode" to determine the feature set
        this.image = selector;
        this.$image = $(selector);
        this.$image_id = this.$image.data('image-id') || opts.image_id;
        if (!this.$image_id) {
            throw {
                'detail' : "No image_id given for the TaggableImage interface"
            };
        }

        // sets up the UI for the taggable plugin initially
        this.$container = this.$image.parent();
        this.$contents = $(_.template(TaggableTmpl)());

        // define the three sections of the UI
        this.$left = this.$container.children('.taggable-left');
        this.$right = this.$container.children('.taggable-right');
        this.$toolbar = this.$container.children('.toolbar-container');

        this.features = [];

        if (opts.features) {
            throw {
                detail: "TaggableImage: Individual features not implemented at this time."
            };
        }
        else {
            if (!accepted_modes[opts.mode]) opts.mode = 'registered';

        }

        this.$container.empty().append(this.$contents);
        // relocate the image to the left side
        this.$left.append(this.$image);
    }

    return {
        create: function(selector, opts) {
            var defaults = {
                'mode': 'registered' // registered or public
            };

            $.extends(defaults, opts);

            return new TaggableImage(selector, defaults);
        },
        MODES: {
            REGISTERED: 'registered',
            PUBLIC: 'public'
        }
    }
});