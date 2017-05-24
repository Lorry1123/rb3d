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
      self.img_width(res.width);
      self.img_height(res.height);
      self.submitted(true);
    };
    var option = {
      url: url,
      success: success
    };
    $('#form').ajaxForm(option);
  });

  self.set_image_name = function () {
    self.name = Math.random();
    while (self.name < 10000) {
      self.name *= 10;
    }
    self.name = parseInt(self.name);
    console.log('name:', self.name);
  };
};

module.exports = imgContainerViewModel;
