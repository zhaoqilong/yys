# -*- coding: UTF-8 -*-
import cv2 as cv
import os
from PIL import Image

import sys

__all__ = ['AndroidUtil']


class AndroidUtil(object):

    def __init__(self, device_info):
        self.config = device_info
        self.device_id = device_info.get('device_id')
        self.device_size = device_info.get('device_size')
        self.device_cap_type = device_info.get('device_cap_type')

    def get_screen_cap(self):
        save_path = '../picture/yys_temp/'
        self.save_screen_cap(save_path)
        image = cv.imread(save_path + self.device_id + '.jpg')
        return image

    def save_screen_cap_with_mini_cap(self, save_path):
        screen_cap = 'adb -s ' + self.device_id + \
                     ' shell \"LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P ' + \
                     self.device_size + \
                     '@' + self.device_size + \
                     '/0 -s > /mnt/sdcard/yys/' + \
                     self.device_id + '.jpg\" 1>/dev/null 2>/dev/null'
        save_picture = 'adb -s ' + self.device_id + ' pull /mnt/sdcard/yys/' + \
                       self.device_id + '.jpg ' + save_path + ' > /dev/null'
        os.system(screen_cap)
        os.system(save_picture)

    def save_screen_cap_with_android_sys(self, save_path):
        screen_cap = 'adb -s ' + self.device_id + ' shell /system/bin/screencap -p /sdcard/yys/' + self.device_id + '.png'
        save_picture = 'adb -s ' + self.device_id + ' pull /sdcard/yys/' + \
                        self.device_id + '.png ' + save_path + ' > /dev/null'
        os.system(screen_cap)
        os.system(save_picture)
        im = Image.open(save_path + self.device_id + '.png')
        rgb_im = im.convert('RGB')
        rgb_im.save(save_path + self.device_id + '.jpg')

    def save_screen_cap(self, save_path):
        if self.device_cap_type == 'minicap':
            self.save_screen_cap_with_mini_cap(save_path)
        elif self.device_cap_type == 'screencap':
            self.save_screen_cap_with_android_sys(save_path)

    def tap_point(self, x, y):
        command = 'adb -s ' + self.device_id + ' shell input tap ' + str(int(x)) + ' ' + str(int(y))
        os.system(command)

    def stop_yys(self):
        stop_command = 'adb -s ' + self.device_id + ' shell am force-stop com.netease.onmyoji'
        os.system(stop_command)
