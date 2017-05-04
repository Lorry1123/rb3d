/**
 * Created by luorui on 2017/5/2.
 */

var fastPageViewModel = function () {
  var self = this;
  self.loading = ko.observable(false);

  $(document).ready(function () {
    var url = '../img_api/upload_pic';
    var success = function (res) {
      if (res.status != 0) {
        alert('请确认上传文件是否为图片');
      }
      $("#imgContainer").attr('src', '../img_api/get_pic');
    };
    var option = {
      url: url,
      success: success
    };
    $('#form').ajaxForm(option);
  });

  self.get_3d_pic = function (data, event) {
    self.loading(true);
    console.log('???');
    $("#3dimgContainer").removeAttr('src');
    // $("#3dimgContainer").attr('src', '../img_api/get_3d_pic?t=' + Math.random());
    $("#3dimgContainer").attr('src', './img?t=' + Math.random());
    console.log('出来了');
  };
};

ko.applyBindings(new fastPageViewModel());
module.exports = fastPageViewModel;