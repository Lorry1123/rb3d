/**
 * Created by luorui on 2017/4/27.
 */

var LoginViewModel = function () {
  self.inited = ko.observable(false);
  self.login_switch = ko.observable(1);

  self.uid = ko.observable('');
  self.psw = ko.observable('');

  self.r_uid = ko.observable('');
  self.r_psw = ko.observable('');
  self.r_psw_repeat = ko.observable('');
  self.r_mobile = ko.observable('');

  self.clean = ko.computed(function () {
    self.uid('');
    self.psw('');
    self.r_uid('');
    self.r_psw('');
    self.r_psw_repeat('');
    self.r_mobile('');

    return self.login_switch();
  });

  self.set_error_log = function (str) {
    alert(str);
  };

  self.login = function (data, event) {
    var api = '/img_deal/login_check';
    var data = {uid: self.uid(), psw: self.psw()};
    if (self.uid() == '' || self.psw() == '') {
      self.set_error_log('用户名或密码为空');
      return;
    }

    $.post(api, data, function (res) {
      if (res.status == 0) {
        window.location.href = '/img_deal/index';
      }
      else {
        self.set_error_log('用户名或密码不正确');
      }
    });
  };

  self.regist = function (data, event) {
    if (self.r_psw() != self.r_psw_repeat()) {
      alert('密码不一致');
    }
    var api = '/img_deal/regist';
    var data = {uid: self.r_uid(), psw: self.r_psw(), mobile: self.r_mobile()};
    $.post(api, data, function (res) {
      if (res.status == 0) {
        self.login_switch(-1 * self.login_switch());
        alert('注册成功');
      }
      else {
        alert('注册失败');
      }
    });

  };

  self.init = function () {
    self.login_switch(1);

    self.inited(true);
  };

  self.init();
};

ko.applyBindings(new LoginViewModel());
module.exports = LoginViewModel;
