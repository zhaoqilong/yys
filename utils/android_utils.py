# coding:utf-8
import cv2 as cv
import os
import sys

__all__ = ['AndroidUtil']

'''工具类，主要用于截图和点击操作，截图使用的minicap，安装较为繁琐'''
class AndroidUtil(object):

    def __init__(self, device_info):
        self.config = device_info
        self.device_id = device_info.get('device_id')
        self.device_size = device_info.get('device_size')


    '''使用minicap进行截图, 并获取到图片实例'''
    def get_screen_cap_with_mini_cap(self):
        save_path = './picture/yys_temp/'
        self.save_screen_cap_with_mini_cap(save_path)
        image = cv.imread(save_path + self.device_id + '.jpg')
        return image

    ''' 安卓系统自带的截图方法，并获取到图片实例'''
    def get_screen_cap_with_android_sys(self):
        save_path = './picture/yys_temp/'
        self.save_screen_cap_with_android_sys(save_path)
        image = cv.imread(save_path + self.device_id + '.png')
        return image

    '''使用minicap进行截图，并将截图存储到save_path里'''
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

    '''使用android系统自带的方式截图并存储到save_path里'''
    def save_screen_cap_with_android_sys(self, save_path):
        screen_cap = 'adb -s ' + self.device_id + ' shell /system/bin/screencap -p /sdcard/' + self.device_id + '.png'
        save_picture = 'adb -s ' + self.device_id + ' pull /sdcard/yys/' + \
                        self.device_id + '.png ' + save_path + ' > /dev/null'
        delete_picture = 'adb -s ' + self.device_id + ' shell rm /sdcard/yys/' + self.device_id + '.png'
        os.system(screen_cap)
        os.system(save_picture)
        os.system(delete_picture)

    '''点击坐标'''
    def tap_point(self, x, y):
        command = 'adb -s ' + self.device_id + ' shell input tap ' + str(int(x)) + ' ' + str(int(y))
        os.system(command)

    '''停止阴阳师'''
    def stop_yys(self):
        stop_command = 'adb -s ' + self.device_id + ' shell am force-stop com.netease.onmyoji'
        os.system(stop_command)

if __name__ == '__main__':
    str = 'adb -s emulator-5554 shell \"$LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P 1280x720@1280x720/0& LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P 1280x720@1280x720/0 -s > /sdcard/haha.jpg\" '
    os.system(str)