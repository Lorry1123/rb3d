# coding: utf8

from PIL import Image
import os
import math


class ImageReader:
    def __init__(self, path=None, name='test'):
        if not path:
            return
        self.img = Image.open(path + name + '.jpg')
        self.img_array = self.img.load()
        self.sum_map = []
        self.sos_map = []
        self.lov_map = []
        self.h, self.w = self.img.size

    def decode(self, path):
        self.img = Image.open(path + 'lena.jpg')
        self.img_array = self.img.load()
        self.h, self.w = self.img.size
        print self.img_array
        print '==========='
        print self.img.size

    def save(self, path, name):
        self.img.save(path + name + '.jpg', 'jpeg', quality=50)

    def calc_lov(self, size=5):
        print 'calc_lov started----------'
        self.calc_sos(size)

        max_lov = 0
        for data in self.sos_map:
            if math.sqrt(data) > max_lov:
                max_lov = math.sqrt(data)
            self.lov_map.append(min(255, int(math.sqrt(data) / 0.05)))

        print 'length of lov_map: %d' % len(self.lov_map)
        print 'max lov:', max_lov

        print 'calc_lov ended------------'

    def calc_sos(self, size=5):
        print 'calc_sos started-----------'
        self.calc_mean(size=size)
        print 'sum map length:', len(self.sum_map)
        self.calc_variance(size=size)
        print 'sos map length:', len(self.sos_map)

        print 'calc_sos ended-----------'

    def calc_variance(self, size=5):
        print 'calc_variance started-----------'
        for i in range(self.h):
            for j in range(self.w):
                self.sos_map.append(self.calc_area_variance(i, j, size))
        print 'calc_variance ended---------'

    def calc_mean(self, size=5):
        print 'calc_mean started------------'
        for i in range(self.h):
            for j in range(self.w):
                self.sum_map.append(self.calc_area_mean(i, j, size))
        print 'calc_mean ended-----------'

    def calc_area_variance(self, x, y, size=5):
        low_x, high_x, low_y, high_y = x - size, x + size, y - size, y + size
        if low_x < 0:
            low_x = 0
        if high_x >= self.h:
            high_x = self.h
        if low_y < 0:
            low_y = 0
        if high_y >= self.w:
            high_y = self.w

        tot = [0, 0, 0]
        num = (high_x - low_x) * (high_y - low_y)
        for i in range(low_x, high_x):
            for j in range(low_y, high_y):
                # print 'index: %d, %d' % (x, y)
                tot[0] += math.pow((self.sum_map[(x - 1) * self.w + y][0] - self.img_array[i, j][0]), 2)
                tot[1] += math.pow((self.sum_map[(x - 1) * self.w + y][1] - self.img_array[i, j][1]), 2)
                tot[2] += math.pow((self.sum_map[(x - 1) * self.w + y][2] - self.img_array[i, j][2]), 2)

        tot[0] /= num
        tot[1] /= num
        tot[2] /= num

        return max(tot[0], tot[1], tot[2])

    def calc_area_mean(self, x, y, size=5):
        low_x, high_x, low_y, high_y = x - size, x + size, y - size, y + size
        if low_x < 0:
            low_x = 0
        if high_x >= self.h:
            high_x = self.h
        if low_y < 0:
            low_y = 0
        if high_y >= self.w:
            high_y = self.w

        tot = [0, 0, 0]
        num = (high_x - low_x) * (high_y - low_y)
        for i in range(low_x, high_x):
            for j in range(low_y, high_y):
                tot[0] += self.img_array[i, j][0]
                tot[1] += self.img_array[i, j][1]
                tot[2] += self.img_array[i, j][2]

        tot[0] /= num
        tot[1] /= num
        tot[2] /= num

        return tot

    def show_lov(self, path=None, name='test'):
        print 'show_lov started----------'
        img = Image.new(self.img.mode, self.img.size)
        img_array = img.load()
        for i in range(self.h):
            for j in range(self.w):
                img_array[i, j] = (self.lov_map[(i - 1) * self.w + j], 0, 0)

        img = img.convert('L')

        print img
        img.show()

        img.save(path + name + '_lov.jpg', 'jpeg')

        print 'show_lov ended----------'



