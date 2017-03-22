/**
 * Created by luorui on 2017/3/17.
 */
var webpack = require('webpack');

module.exports = {
  // entry: {
  //   testPage: './img_deal/static/js/viewmodels/testPage.js'
  // },
  entry: {
    testPage: './frontend/js/pages/testPage.js'
  },
  output: {
    path: './img_deal/static/packed/js',
    filename : '[name].js'
  }
};