/**
 * Created by luorui on 2017/3/17.
 */
var webpack = require('webpack');

var DEFAULT_PAGES_PATH = './frontend/js/pages/';

module.exports = {
  entry: {
    testPage: DEFAULT_PAGES_PATH + 'testPage.js',
    login: DEFAULT_PAGES_PATH + 'login.js',
    fastPage : DEFAULT_PAGES_PATH + 'fastPage.js',
    listPage: DEFAULT_PAGES_PATH + 'listPage.js',
    enhancedPage: DEFAULT_PAGES_PATH + 'enhancedPage.js'
  },
  output: {
    path: './img_deal/static/packed/js',
    filename : '[name].js'
  }
};