#coding:utf-8

import os
import time
import cv2 as cv
import Constant_MI5 as constant
import numpy as np
import random
import sys
from WeChatUtils import WechatUtils


def save_screen_cap(pic_name, path):
    screencap = 'adb -s '+ constant.device_id +' shell /system/bin/screencap -p /sdcard/' + pic_name + '.png'
    save_picture = 'adb -s '+ constant.device_id +' pull /sdcard/' + pic_name + '.png ' + path
    delete_picture = 'adb -s '+ constant.device_id +' shell rm /sdcard/' + pic_name + '.png'
    os.system(screencap)
    os.system(save_picture)
    os.system(delete_picture)
    image = cv.imread(path + pic_name+'.png')
    return image

def get_picture_part(image, coordinate):
    return image[coordinate['y1']:coordinate['y2'], coordinate['x1']:coordinate['x2']]

def tap_point(x,y):
    command = 'adb -s '+ constant.device_id +' shell input tap ' + str(int(x)) + ' ' + str(int(y))
    os.system(command)

#判断图片是否存在某位置图像，同时随机点按
def judge_pic_state(mark_pic, image, pic_size_dict ,sleep_time, threshold, type):

    real_time_pic = get_picture_part(image, pic_size_dict)
    difference = cv.subtract(mark_pic, real_time_pic)
    result = np.mean(difference)
    if result <= threshold:
        print(type, result)
        x_offset = int(abs(pic_size_dict['x1'] - pic_size_dict['x2']) / 2)
        y_offset = int(abs(pic_size_dict['y1'] - pic_size_dict['y2']) / 2)

        tap_point((pic_size_dict['x1'] + pic_size_dict['x2']) / 2 + random.randint(-x_offset,x_offset),
                  (pic_size_dict['y1'] + pic_size_dict['y2']) / 2 + random.randint(-y_offset,y_offset))
        a = random.randint(1, 10)
        time.sleep(sleep_time + a / 10)
        return True
    else:
        return False

def start(use_wechat):

    friend_name = 'main'
    if use_wechat==True:
        wechat = WechatUtils(friend_name)
    challenge_btn = cv.imread('./yys_mark/challenge_btn_' + constant.device_id + '.png')
    win_mark_box = cv.imread('./yys_mark/win_mark_box_' + constant.device_id + '.png')
    win_mark_drum = cv.imread('./yys_mark/win_mark_drum_' + constant.device_id + '.png')
    single_failure = cv.imread('./yys_mark/single_failure_' + constant.device_id + '.png')
    stop_times_threshold = 0
    while True:
        image = save_screen_cap(constant.device_id, './yys_temp/')
        print('stop_times_threshold', stop_times_threshold)
        stop_times_threshold = stop_times_threshold + 1
        if stop_times_threshold >= 50:
            if use_wechat == True:
                wechat.send_question('your single_player_auto.py is down')
            name = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            save_screen_cap(name, './yys_pic_log')
            time.sleep(10)
            sys.exit(0)

        if stop_times_threshold >= 100:
            if use_wechat == True:
                wechat.send_question('your single_player_auto.py will shut')
            stop_command = 'adb -s '+ constant.device_id +' shell am force-stop com.netease.onmyoji'
            os.system(stop_command)
            sys.exit(0)
        #判断是否存在挑战按钮
        if judge_pic_state(challenge_btn, image, constant.challenge_btn, 0, 0.01, 'challenge_btn'):
            continue

        #判断是否战斗胜利，存在误触影响，不考虑
        # if judge_pic_state(win_mark_drum, image, constant.win_mark_drum, 1, 0.2, 'win_mark_drum'):
        #     continue

        #判断是否到了宝箱出现的结束界面
        if judge_pic_state(win_mark_box, image, constant.win_mark_box, 1, 0.2 ,'win_mark_box'):
            stop_times_threshold = 0
            continue

        #判断是否战斗失败
        if judge_pic_state(single_failure, image, constant.single_failure, 0, 2, 'single_failure'):
            continue

        time.sleep(0.3)


if __name__ == '__main__':
    start(use_wechat=False)
