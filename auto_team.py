#coding:utf-8
import os
import time
import cv2 as cv
import Constant_MI8 as constant
import numpy as np
import random
import sys


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
def judge_pic_state(mark_pic, image, pic_size_dict, tap_area_dict ,sleep_time, threshold, type):

    real_time_pic = get_picture_part(image, pic_size_dict)
    difference = cv.subtract(mark_pic, real_time_pic)
    result = np.mean(difference)
    if result <= threshold:
        x_offset = int(abs(tap_area_dict['x1'] - tap_area_dict['x2']) / 2)
        y_offset = int(abs(tap_area_dict['y1'] - tap_area_dict['y2']) / 2)
        tap_x = (tap_area_dict['x1'] + tap_area_dict['x2']) / 2 + random.randint(-x_offset,x_offset)
        tap_y = (tap_area_dict['y1'] + tap_area_dict['y2']) / 2 + random.randint(-y_offset,y_offset)
        tap_point(tap_x, tap_y)
        tap_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_str = tap_time + ' ' +type + ' ' + '(' + str(tap_x) + ',' + str(tap_y) + ')\n'
        with open('./yys_log/' + constant.device_id + '_auto_team.txt' ,'a') as log_file:
            print("***********************************")
            print(log_str)
            print("***********************************")
            log_file.write(log_str)
        a = random.randint(1, 8)
        time.sleep(sleep_time + a / 10)
        return True
    else:
        return False

def start():

    start_fighting = cv.imread('./yys_mark/start_fighting_' + constant.device_id + '.png')
    win_mark_box = cv.imread('./yys_mark/team_win_mark_box_' + constant.device_id + '.png')
    win_mark_drum = cv.imread('./yys_mark/team_win_mark_drum_' + constant.device_id + '.png')
    team_failure = cv.imread('./yys_mark/team_failure_' + constant.device_id + '.png')
    stop_times_threshold = 0
    while True:
        image = save_screen_cap(constant.device_id + '_team', './yys_temp/')
        stop_times_threshold = stop_times_threshold + 1
        if stop_times_threshold >= 50:
            time.sleep(5)

        if stop_times_threshold >= 100:

            name = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
            save_screen_cap(name, './yys_pic_log')
            time.sleep(10)
            stop_command = 'adb -s '+ constant.device_id +' shell am force-stop com.netease.onmyoji'
            os.system(stop_command)
            sys.exit(0)

        #判断是否存在开始战斗按钮
        if judge_pic_state(start_fighting, image, constant.start_fighting, constant.start_fighting , 0, 0.01, 'start_fighting_'):
            continue

        #判断是否战斗胜利
        if judge_pic_state(win_mark_drum, image, constant.team_win_mark_drum, constant.win_mark_drum_tap, 0, 0.2, 'team_win_mark_drum'):
            continue

        #判断是否到了宝箱出现的结束界面
        if judge_pic_state(win_mark_box, image, constant.team_win_mark_box, constant.win_mark_box_tap, 0, 0.2 ,'team_win_mark_box'):
            stop_times_threshold = 0
            continue

        #判断是否战斗失败
        if judge_pic_state(team_failure, image, constant.team_failure, constant.single_failure_tap , 0, 2, 'team_failure'):
            stop_times_threshold = 0
            continue


if __name__ == '__main__':
    start()
