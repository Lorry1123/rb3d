/**
 * Created by luorui on 2017/5/2.
 */

var imgContainerViewModel = require('../viewmodels/imgContainer.js');

var fastPageViewModel = function () {
  var self = this;

  self.loading = ko.observable(false);


  imgContainerViewModel(self);

  self.get_3d_pic = function (data, event) {
    if (!self.submitted()) {
      alert('请先上传图片');
      return;
    }
    self.loading(true);
    $("#3dimgContainer").removeAttr('src');
    $("#3dimgContainer").attr('src', '../img_api/get_3d_pic/' + self.name + '?t=' + Math.random());
  };

  self.remove_text = function () {
    console.log('load');
    self.loading(false);
    self.submitted(false);
  };

  self.init = function () {
    self.loading(false);
    self.submitted(false);
    self.name = Math.random();
    while (self.name < 10000) {
      self.name *= 10;
      console.log(self.name);
    }
    self.name = parseInt(self.name);
  };

  self.init();
};

// $("img_std_Test").load(function () {
//    self.loading(false);
//  });

ko.applyBindings(new fastPageViewModel());
module.exports = fastPageViewModel;