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
      console.log(list_container);
      $.each(self.img_list(), function (index, element) {
        var tr1 = $('<tr>');
        var td1 = $('<td>');
        var td2 = $('<td>');
        var td3 = $('<td>');
        var img1 = $('<img>').attr('src', '../img_api/get_pic/' + element + '?t=' + Math.random());
        var img2 = $('<img>').attr('src', '../img_api/get_pic/' + element + '_3d?t=' + Math.random());
        var a1 = $('<a>').attr('href', '../img_api/get_pic/' + element + '_3d').append('查看大图');
        td1.append(img1);
        td2.append(img2);
        td3.append(a1).attr('style','padding-top: 150px');
        tr1.append(td1).append(td2).append(td3);
        list_container.append(tr1);
      });
    });

    self.inited(true);
  };

  self.init();
};

ko.applyBindings(new ListPageViewModel());
module.exports = ListPageViewModel;