/**
 * Created by luorui on 2017/5/6.
 */

var imgContainerViewModel = require('../viewmodels/imgContainer.js');

var enhancedPageViewModel = function () {
  var self = this;
  imgContainerViewModel(self);

  self.inited = ko.observable(false);
  self.step = ko.observable(0);


  self.switch_step = function (step) {
    self.step(step);
  };

  self.init = function () {

    self.switch_step(1);

    self.inited(true);
  };

  self.init();
};

ko.applyBindings(new enhancedPageViewModel());
module.exports = enhancedPageViewModel;