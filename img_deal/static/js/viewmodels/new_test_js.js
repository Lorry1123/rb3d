/**
 * Created by luorui on 2017/3/17.
 */

var new_test_js = function (act) {
  var self = act || this;

  self.get_random = function () {
    return Math.random();
  };

  console.log(self);
};

module.exports = new_test_js;