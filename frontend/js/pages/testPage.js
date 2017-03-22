/**
 * Created by luorui on 2017/3/18.
 */
var req_test = require('../viewmodels/req_test.js');

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
    var new_js = require('../viewmodels/new_test_js.js');
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