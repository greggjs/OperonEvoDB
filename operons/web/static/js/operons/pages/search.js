require.config({
    shim: {
        jquery: {
            init: function() {
                return $;
            }
        },
        bootstrap: ['jquery'],
        jquery_ui: ['jquery'],
        underscore : {
            exports : '_'
        }
    },
    paths: {
        jquery: 'lib/jquery-1.11.0.min',
        underscore: 'lib/underscore.min',
        bootstrap: 'lib/bootstrap.min',
        //jquery_ui: 'lib/jquery-ui-1.10.4.min',
        text: 'lib/require-text'
    }
});


var deps = ['jquery', 'underscore', 'settings'];

require(deps, function($, _, settings) {

});
