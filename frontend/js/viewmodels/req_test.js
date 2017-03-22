/**
 * Created by luorui on 2017/3/17.
 */

var req_testViewModel = function (act) {
  var self = act || this;
  console.log('require 成功');

  self.count_times = ko.observable(0);
  self.require_click = function (data, event) {
    self.count_times(self.count_times() + 1);
  };

};

module.exports = req_testViewModel;