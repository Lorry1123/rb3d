/**
 * Created by luorui on 2017/5/6.
 */

var imgContainerViewModel = require('../viewmodels/imgContainer.js');

var enhancedPageViewModel = function () {
  var self = this;

  self.inited = ko.observable(false);
  self.step = ko.observable(0);

  imgContainerViewModel(self);

  self.switch_step = function (step) {
    self.step(step);
  };

  self.init = function () {
    self.set_image_name();
    self.switch_step(1);

    self.inited(true);
  };

  self.init();
};

ko.applyBindings(new enhancedPageViewModel());
module.exports = enhancedPageViewModel;