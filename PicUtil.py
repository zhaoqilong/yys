#coding:utf-8

import os
import time
import cv2 as cv
import Constant_MI5 as constant
import numpy as np



def save_screen_cap(pic_name):
    screencap = 'adb -s '+ constant.device_id +' shell /system/bin/screencap -p /sdcard/' + pic_name + '.png'
    save_picture = 'adb -s '+ constant.device_id +' pull /sdcard/' + pic_name + '.png ' + './yys_screenshots'
    delete_picture = 'adb -s '+ constant.device_id +' shell rm /sdcard/' + pic_name + '.png'
    os.system(screencap)
    os.system(save_picture)
    os.system(delete_picture)
    #image = cv.imread('./yys_temp/' +pic_name+'.png')
    #cv.imshow("Image", image)
    #cv.waitKey(0)

def show_pic(name):
    image = cv.imread('./yys_screenshots/' + name)
    cv.imshow("Image", image)
    cv.waitKey(0)

def cut_picture(name,out_name,coordinate):
    image = cv.imread('./yys_screenshots/' + name + '.png')
    image = image[coordinate['y1']:coordinate['y2'], coordinate['x1']:coordinate['x2']]
    cv.imwrite('./yys_mark/' + out_name + "_" + constant.device_id +'.png' ,image)

if __name__ == '__main__':
    #save_screen_cap('yuhun_single_win')
    show_pic('yuhun_end_win.png')
    #cut_picture('yuhun_single_win','win_mark_drum',constant.win_mark_drum)