# coding: utf8

from img_deal.img_api import ImageReader

DEFAULT_IMAGE_PATH = 'img_deal/img_api/img/'


def make_3d_pic(name):
    # print '开始', 'name=', name
    # img = ImageReader(path=DEFAULT_IMAGE_PATH, name=name)
    # print 'init done'
    # img.calc_lov(size=3)
    # print 'lov done'
    # img.calc_deep_map(debug_mode=True)
    # print 'deep done'
    # img.red_blue_translation()
    # print 'merge done'
    #
    # ret = file(DEFAULT_IMAGE_PATH + name + '_3d.jpg')

    img = ImageReader(path=DEFAULT_IMAGE_PATH, name=name)
    img.calc_lov(size=3)
    img.show_lov(show=False)
    img.calc_deep_map()
    img.red_blue_translation()

    ret = file(DEFAULT_IMAGE_PATH + 'img_upload_3d' + '.jpg')
    return ret
