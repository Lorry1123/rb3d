/**
 * Created by luorui on 2017/5/2.
 */

var fastPageViewModel = function () {
  var self = this;
  self.loading = ko.observable(false);
  self.submitted = ko.observable(false);
  self.name = 0;

  $(document).ready(function () {
    var url = '../img_api/upload_pic/' + self.name;
    var success = function (res) {
      if (res.status != 0) {
        alert('请确认上传文件是否为图片');
      }
      $("#imgContainer").attr('src', res.src + '?t=' + Math.random());
      self.submitted(true);
    };
    var option = {
      url: url,
      success: success
    };
    $('#form').ajaxForm(option);


  });

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