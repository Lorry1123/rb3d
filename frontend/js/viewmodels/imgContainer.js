/**
 * Created by luorui on 2017/5/6.
 */

var imgContainerViewModel = function (parent) {
  var self = parent || this;

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
};

module.exports = imgContainerViewModel;
