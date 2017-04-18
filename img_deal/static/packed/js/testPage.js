/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId])
/******/ 			return installedModules[moduleId].exports;
/******/
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// identity function for calling harmony imports with the correct context
/******/ 	__webpack_require__.i = function(value) { return value; };
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, {
/******/ 				configurable: false,
/******/ 				enumerable: true,
/******/ 				get: getter
/******/ 			});
/******/ 		}
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 2);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ (function(module, exports) {

/**
 * Created by luorui on 2017/3/17.
 */

var new_test_js = function (act) {
  var self = act || this;

  self.get_random = function () {
    return Math.random();
  };

  console.log(self);
};

module.exports = new_test_js;

/***/ }),
/* 1 */
/***/ (function(module, exports) {

/**
 * Created by luorui on 2017/3/17.
 */

var req_testViewModel = function (act) {
  var self = act || this;
  console.log('require 成功');

  self.count_times = ko.observable(0);
  self.require_click = function (data, event) {
    self.count_times(self.count_times() + 1);
  };

};

module.exports = req_testViewModel;

/***/ }),
/* 2 */
/***/ (function(module, exports, __webpack_require__) {

/**
 * Created by luorui on 2017/3/18.
 */
var req_test = __webpack_require__(1);

var layoutViewModel = function () {
  var self = this;

  req_test(self);

  self.input_text = ko.observable('');
  self.show_text = ko.computed(function () {
    return '你好， ' + self.input_text() + '!';
  });

  self.show_target = function (data, event) {
    console.log(event.target);
    alert('target:' + event.target + '\nposition:' + event.clientX + ',' + event.clientY);
  };

  self.req_a_new_js = function (data, event) {
    var new_js = __webpack_require__(0);
    self.son1 = {};
    new_js(self.son1);
    console.log('in father', self.son1.get_random());
    alert('随机数为:' + self.son1.get_random());
  };

  self.pic_geted = ko.observable(false);
  self.get_pic_text = ko.computed(function () {
    return self.pic_geted() ? '点击移除图片' : '点击获取图片';
  });
  self.request_pic = function (data, event) {
    var url = '../img_api/get_pic';
    if (!self.pic_geted()) {
      $("#img_container").attr("src", url);
    }
    else {
      $("#img_container").removeAttr("src");
    }
    self.pic_geted(!self.pic_geted());
  };

  self.ret_msg = ko.observable('');
  self.phone = ko.observable('');
  self.obj = ko.observable('');
  self.detail = ko.observable('');
  self.name = ko.observable('');
  self.send_msg = function (data, event) {
    $.post('/img_api/send_msg_yunpian',{
      phone: self.phone,
      obj: self.obj,
      detail: self.detail,
      name: self.name
    }, function (res) {
      self.ret_msg(res);
      console.log(res);
    });
  };

  self.send_msg_dayu = function (data, event) {
    $.post('/img_api/send_msg_alidayu',{
      phone: self.phone,
      obj: self.obj,
      detail: self.detail,
      name: self.name
    }, function (res) {
      self.ret_msg(res);
      console.log(res);
    });
  }

};


ko.applyBindings(new layoutViewModel());
module.exports = layoutViewModel;

$(document).ready(function () {
  $("#submit").click(function () {
    var text = $("#text").val();
    console.log(text);
    $("#show").text(text);
  });
});

/***/ })
/******/ ]);