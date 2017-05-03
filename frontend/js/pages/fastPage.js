/**
 * Created by luorui on 2017/5/2.
 */

var fastPageViewModel = function () {
  var self = this;
  // $(document).ready(function () {
  //   $('#form').submit(function (data) {
  //     alert(data);
  //   });
  // });

  self.pic_submit = function (data, event) {
    $('#form').ajaxSubmit();
  };


};

ko.applyBindings(new fastPageViewModel());
module.exports = fastPageViewModel;