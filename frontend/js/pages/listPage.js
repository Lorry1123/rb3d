/**
 * Created by luorui on 2017/5/5.
 */

var ListPageViewModel = function () {
  var self = this;
  self.inited = ko.observable(false);

  self.show_fast_make = ko.observable(false);
  self.img_list = ko.observableArray([]);

  self.init = function () {
    $.post('./img_list', {}, function (res) {
      if (res.status) {
        self.show_fast_make(true);
      }
      else {
        var tmp = [];
        $.each(res.img_list, function (index, element) {
          tmp.push(element.name);
        });
        self.img_list(tmp);
      }

      var list_container = $("#image_list");
      $.each(self.img_list(), function (index, element) {
        var div1 = $('<div>');
        var img1 = $('<img>').attr('src', '../img_api/get_pic/' + element + '?t=' + Math.random());
        var img2 = $('<img>').attr('src', '../img_api/get_pic/' + element + '_3d?t=' + Math.random());
        var a1 = $('<a>').attr('href', '../img_api/get_pic/' + element + '_3d').append('查看原图');
        div1.append(img1).append(img2).append(a1);
        list_container.append(div1);
      });
    });

    self.inited(true);
  };

  self.init();
};

ko.applyBindings(new ListPageViewModel());
module.exports = ListPageViewModel;