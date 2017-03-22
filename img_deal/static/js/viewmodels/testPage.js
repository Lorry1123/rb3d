/**
 * Created by luorui on 2017/3/17.
 */
var req_test = require('./req_test.js');

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
    var new_js = require('./new_test_js.js');
    self.son1 = {};
    new_js(self.son1);
    console.log('in father', self.son1.get_random());
    alert('随机数为:' + self.son1.get_random());
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