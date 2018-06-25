#coding:utf-8

import os
import time
import cv2 as cv
import Constant_MI5 as constant
import numpy as np
import random

sleep_time = 0.8

def save_screen_cap(pic_name):
    screencap = 'adb -s '+ constant.device_id +' shell /system/bin/screencap -p /sdcard/' + pic_name + '.png'
    save_picture = 'adb -s '+ constant.device_id +' pull /sdcard/' + pic_name + '.png ' + './yys_temp'
    delete_picture = 'adb -s '+ constant.device_id +' shell rm /sdcard/' + pic_name + '.png'
    os.system(screencap)
    os.system(save_picture)
    os.system(delete_picture)
    image = cv.imread('./yys_temp/' +pic_name+'.png')
    return image

def get_picture_part(image, coordinate):
    return image[coordinate['y1']:coordinate['y2'], coordinate['x1']:coordinate['x2']]


def start_yuhun():

    # show_picture('./yys_screenshots/yuhun_end_win2.png')
    # cut_picture('./yys_screenshots/yuhun_end_win2.png', './yys_mark/win_mark_box.png',constant.win_mark_box)
    start_fighting = cv.imread('./yys_mark/start_fighting_'+constant.device_id+ '.png')
    win_mark_box = cv.imread('./yys_mark/win_mark_box_'+constant.device_id+ '.png')
    win_mark_drum = cv.imread('./yys_mark/win_mark_drum_'+constant.device_id+ '.png')
    while True:

        image = save_screen_cap('yuhun')
        start_fighting_test = get_picture_part(image, constant.start_fighting)
        win_mark_box_test = get_picture_part(image, constant.win_mark_box)
        win_mark_drum_test = get_picture_part(image, constant.win_mark_drum)

        fighting_difference = cv.subtract(start_fighting_test, start_fighting)
        fighting_result = np.mean(fighting_difference)
        if fighting_result <= 0.001:
            print('************************************************')
            print('fighting_result', fighting_result)

            x_offset = int(abs(constant.start_fighting['x1'] - constant.start_fighting['x2'])/2)
            y_offset = int(abs(constant.start_fighting['y1'] - constant.start_fighting['y2'])/2)

            tap_point((constant.start_fighting['x1'] + constant.start_fighting['x2']) / 2 + random.randint(-x_offset,x_offset ),
                      (constant.start_fighting['y1'] + constant.start_fighting['y2']) / 2 + random.randint(-y_offset,y_offset ))
            #time.sleep(sleep_time)
            continue

        box_difference = cv.subtract(win_mark_box_test, win_mark_box)
        box_result = np.mean(box_difference)
        if box_result <= 2:
            print('************************************************')
            print('box_result', box_result)
            x_offset = int(abs(constant.win_mark_box['x1'] - constant.win_mark_box['x2']) / 2)
            y_offset = int(abs(constant.win_mark_box['y1'] - constant.win_mark_box['y2']) / 2)

            tap_point((constant.win_mark_box['x1'] + constant.win_mark_box['x2']) / 2 + random.randint(-x_offset,
                                                                                                         x_offset),
                      (constant.win_mark_box['y1'] + constant.win_mark_box['y2']) / 2 + random.randint(-y_offset,
                                                                                                           y_offset))
            #time.sleep(0.3)
            continue

        drum_difference = cv.subtract(win_mark_drum_test, win_mark_drum)
        drum_result = np.mean(drum_difference)
        print('drum_result', drum_result)

        if drum_result <= 2:
            print('************************************************')
            print('drum_result', drum_result)

            x_offset = int(abs(constant.win_mark_drum['x1'] - constant.win_mark_drum['x2']) / 2)
            y_offset = int(abs(constant.win_mark_drum['y1'] - constant.win_mark_drum['y2']) / 2)

            tap_point((constant.win_mark_drum['x1'] + constant.win_mark_drum['x2']) / 2 + random.randint(-x_offset,
                                                                                                       x_offset),
                      (constant.win_mark_drum['y1'] + constant.win_mark_drum['y2']) / 2 + random.randint(-y_offset,
                                                                                                       y_offset))
            #time.sleep(sleep_time)
            continue



def test_fun():
    start_fighting = cv.imread('./yys_mark/start_fighting_'+constant.device_id+ '.png')
    win_mark_box = cv.imread('./yys_mark/win_mark_box_' + constant.device_id + '.png')
    win_mark_drum = cv.imread('./yys_mark/win_mark_drum_' + constant.device_id + '.png')

    image = cv.imread('./yys_screenshots/' + 'yuhun_mi8_end_win'+'.png')
    start_fighting_test = get_picture_part(image, constant.start_fighting)
    win_mark_box_test = get_picture_part(image, constant.win_mark_box)
    win_mark_drum_test = get_picture_part(image, constant.win_mark_drum)

    drum_difference = cv.subtract(win_mark_drum_test, win_mark_drum)
    drum_result = np.mean(drum_difference)
    print('drum_result', drum_result)
    if drum_result <= 1:
        # todo random
        print('drum_result')
        tap_point((constant.win_mark_drum['x1'] + constant.win_mark_drum['x2']) / 2 + random.randint(0, abs(
            constant.win_mark_drum['x1'] - constant.win_mark_drum['x2'])),
                  (constant.win_mark_drum['y1'] + constant.win_mark_drum['y2']) / 2 + random.randint(0, abs(
                      constant.win_mark_drum['x1'] - constant.win_mark_drum['x2'])))
        time.sleep(sleep_time)



def tap_point(x,y):
    command = 'adb -s '+ constant.device_id +' shell input tap ' + str(int(x)) + ' ' + str(int(y))
    os.system(command)

if __name__ == '__main__':
    start_yuhun()
        #cv.imshow("Image", image)