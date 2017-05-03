/**
 * Created by luorui on 2017/3/17.
 */
var webpack = require('webpack');

module.exports = {
  // entry: {
  //   testPage: './img_deal/static/js/viewmodels/testPage.js'
  // },
  entry: {
    testPage: './frontend/js/pages/testPage.js',
    login: './frontend/js/pages/login.js',
    fastPage : './frontend/js/pages/fastPage.js'
  },
  output: {
    path: './img_deal/static/packed/js',
    filename : '[name].js'
  }
};