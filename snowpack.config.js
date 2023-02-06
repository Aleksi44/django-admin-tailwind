const httpProxy = require('http-proxy');
const proxy = httpProxy.createServer({target: 'http://127.0.0.1:8000'});
const { version } = require('./package.json');

module.exports = {
    routes: [
        {
            match: "routes",
            src: '.*',
            dest: (req, res) => proxy.web(req, res),
        },
        {
            src: '/media/.*',
            dest: (req, res) => proxy.web(req, res),
        },
        {
            src: '/static/.*',
            dest: (req, res) => proxy.web(req, res),
        },
    ],
    mount: {
        "assets": `/django_admin_tailwind/${version}`,
    },
    plugins: [
        "@snowpack/plugin-postcss"
    ],
};
