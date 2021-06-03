const path = require('path');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const BrowserSyncPlugin = require('browser-sync-webpack-plugin');
const {version} = require('./package.json');

module.exports = ({mode = 'development'} = {}) => {
    const isProductionBuild = mode === 'production';
    const defaultPlugins = [];
    const productionPlugins = [
        new CleanWebpackPlugin(['build']),
    ];
    const devPlugins = [
        new BrowserSyncPlugin({
            proxy: '127.0.0.1:4243',
            port: 3009,
            files: [
                'static/django_admin_tailwind/src/scss/**/*.scss',
            ],
            reloadDelay: 0,
            notify: false,
            open: false,
        }),
    ];

    return {
        entry: {
            base: path.resolve(__dirname, 'static/django_admin_tailwind/src/scss/base.scss'),
        },
        output: {
            filename: `static/django_admin_tailwind/dist/js/[name]-${version}.js`,
            chunkFilename: `static/django_admin_tailwind/dist/js/[name]-${version}.js`,
            path: path.resolve(__dirname, '.'),
            publicPath: '/',
        },
        module: {
            rules: [
                {
                    test: /\.s[ac]ss$/i,
                    use: [
                        {
                            loader: 'file-loader',
                            options: {
                                name: `static/django_admin_tailwind/dist/css/[name]-${version}.css`,
                            },
                        },
                        {
                            loader: 'extract-loader',
                        },
                        {
                            loader: 'css-loader',
                        },
                        {
                            loader: 'sass-loader',
                        },
                        {
                            loader: 'postcss-loader',
                        },
                    ],
                },
            ],
        },
        plugins: [
            ...defaultPlugins,
            ...isProductionBuild ? productionPlugins : devPlugins,
        ],
        devtool: isProductionBuild ? 'source-map' : false,
        devServer: {
            open: true,
            disableHostCheck: true,
            proxy: {
                '/': {
                    target: 'http://127.0.0.1:4243',
                },
            },
        },
    };
};
