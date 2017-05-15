/**
 * Created by luorui on 2017/5/6.
 */

var imgContainerViewModel = require('../viewmodels/imgContainer.js');
var validator = require('../lib/validate.config.js');

var enhancedPageViewModel = function () {
  var self = this;

  self.inited = ko.observable(false);
  self.step = ko.observable(0);
  self.lov_calced = ko.observable(false);

  self.x_low = ko.observable(0);
  self.y_low = ko.observable(0);
  self.x_high = ko.observable(0);
  self.y_high = ko.observable(0);
  self.flag = 0;
  self.xy_append = ko.observable('');
  self.area_text = ko.observable('');

  self.size = ko.observable(3);

  self.screen_x = ko.observable(0);
  self.screen_y = ko.observable(0);
  self.screen_size = ko.observable(0);

  self.threshold = ko.observable(0.5);
  self.check_input = ko.computed(function () {
    try {
      var tmp = parseFloat(self.threshold());
    }
    catch (err) {
      return -1;
    }

    console.log(tmp);

    if (tmp < 0 || tmp > 1) {
      return -1;
    }

    return self.threshold();
  });


  imgContainerViewModel(self);

  self.switch_step = function (step) {
    self.step(step);
  };

  self.choose_area = function (data, event) {
    if (!self.submitted()) {
      alert('请先上传图片');
      return;
    }

    if (self.flag === 0) {
      $('button').attr('disabled', 'disabled');
      $('a').attr('disabled', 'disabled');
      $('input').attr('disabled', 'disabled');
      self.xy_append('请在图片中点击主体左上角');
      self.flag = 1;
    }
  };

  self.set_xy = function (data, event) {
    if (self.flag === 1) {
      self.x_low(event.offsetX);
      self.y_low(event.offsetY);
      console.log(self.x_low(), self.y_low());

      self.xy_append('请在图片中点击主体右下角');
      self.flag = 2;
    }
    else if (self.flag === 2) {
      self.x_high(event.offsetX);
      self.y_high(event.offsetY);
      console.log(self.x_high(), self.y_high());

      var s = '已选区域为：' + self.x_low() + ',' + self.y_low() + ' 至 ' + self.x_high() + ',' + self.y_high();
      self.area_text(s);

      self.flag = 0;
      self.xy_append('');
      $('button').removeAttr('disabled');
      $('a').removeAttr('disabled');
      $('input').removeAttr('disabled');
    }
  };

  self.calc_lov = function () {
    var api = '../img_api/make_lov';
    var data = {
      name: self.name,
      x_low: self.x_low() || 0,
      y_low: self.y_low() || 0,
      x_high: self.x_high() || 9999,
      y_high: self.y_high() || 9999,
      threshold: self.threshold() || 0.05,
      size: self.size()
    };
    $.post(api, data, function (res) {
      self.lov_calced(true);
      $('#step1_preview').removeAttr('src');
      var api = '../img_api/get_lov/' + self.name + '?t=' + Math.random();
      $('#step1_preview').attr('src', api);
    });
  };

  self.step1_preview = function (data, event) {
    if (!self.submitted()) {
      alert('请先上传图片');
      return;
    }

    self.calc_lov();
    // var api = '../img_api/make_lov';
    // var data = {
    //   name: self.name,
    //   x_low: self.x_low() || 0,
    //   y_low: self.y_low() || 0,
    //   x_high: self.x_high() || 9999,
    //   y_high: self.y_high() || 9999,
    //   threshold: self.threshold() || 0.05,
    //   size: self.size()
    // };
    // $.post(api, data, function (res) {
    //   self.lov_calced(true);
    //   $('#step1_preview').removeAttr('src');
    //   var api = '../img_api/get_lov/' + self.name + '?t=' + Math.random();
    //   $('#step1_preview').attr('src', api);
    // });
  };

  self.next_step = function (data, event) {
    if (self.step() == 1) {
      if (!self.submitted()) {
        alert('请先上传图片');
        return;
      }
      if (!self.lov_calced()) {
        self.calc_lov();
      }
      self.switch_step(2);
    }
    else if (self.step() == 2) {
      console.log('switch to step 3');
      $('#finish_img').attr('src', '../img_api/get_3d_pic/' + self.name + '?t=' + Math.random());
      self.switch_step(3);
    }
  };

  self.init = function () {
    self.set_image_name();
    self.name = 'test';

    self.switch_step(1);

    self.inited(true);
  };

  $().ready(function () {
    $("#threshold_input").validate();
    $("#screen_pixel").validate();
    $("#screen_size").validate();
  });

  self.init();
};

ko.applyBindings(new enhancedPageViewModel());
module.exports = enhancedPageViewModel;