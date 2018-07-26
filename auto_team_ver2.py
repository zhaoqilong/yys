#coding:utf-8
import os
import time
import cv2 as cv
import numpy as np
import random
import sys
import datetime
import argparse


def save_screen_cap_with_minicap(pic_name, path):
    screencap = 'adb -s '+ constant.device_id + ' shell \"LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P ' + constant.size + '@'+ constant.size  + '/0 -s > /mnt/sdcard/yys/' + pic_name + '.jpg\" '
    save_picture = 'adb -s ' + constant.device_id + ' pull /mnt/sdcard/yys/'+ pic_name +'.jpg ' + path + ' > /dev/null'
    os.system(screencap)
    os.system(save_picture)
    image = cv.imread(path + pic_name+'.jpg')
    return image

def get_picture_part(image, coordinate):
    return image[coordinate['y1']:coordinate['y2'], coordinate['x1']:coordinate['x2']]

def tap_point(x,y):
    command = 'adb -s '+ constant.device_id +' shell input tap ' + str(int(x)) + ' ' + str(int(y))
    os.system(command)


def exception():
    exception_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    save_screen_cap_with_minicap(constant.device_id + "_" + str(exception_time) + "_exception", './yys_exception' )
    print("游戏出现突发情况，已将游戏界面保存到./yys_exception 文件夹中")
    time.sleep(5)
    stop_command = 'adb -s ' + constant.device_id + ' shell am force-stop com.netease.onmyoji'
    os.system(stop_command)
    sys.exit(0)

#判断图片是否存在某位置图像，同时随机点按
def judge_pic_state(mark_pic, image, pic_size_dict, tap_area_dict , threshold, type):

    real_time_pic = get_picture_part(image, pic_size_dict)
    difference = cv.subtract(mark_pic, real_time_pic)
    result = np.mean(difference)

    print("***************************************")
    print(type + " " + str(result))
    print("***************************************")


    if abs(result - threshold[0]) <= threshold[1]:
        x_offset = int(abs(tap_area_dict['x1'] - tap_area_dict['x2']) / 2)
        y_offset = int(abs(tap_area_dict['y1'] - tap_area_dict['y2']) / 2)
        tap_x = (tap_area_dict['x1'] + tap_area_dict['x2']) / 2 + random.randint(-x_offset,x_offset)
        tap_y = (tap_area_dict['y1'] + tap_area_dict['y2']) / 2 + random.randint(-y_offset,y_offset)
        if type == 'team_win_mark_drum':
            tap_point(tap_x, tap_y)
            time.sleep(0.2)
            tap_x = (tap_area_dict['x1'] + tap_area_dict['x2']) / 2 + random.randint(-x_offset, x_offset)
            tap_y = (tap_area_dict['y1'] + tap_area_dict['y2']) / 2 + random.randint(-y_offset, y_offset)
            tap_point(tap_x, tap_y)
        else:
            tap_point(tap_x, tap_y)
        tap_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_str = tap_time + ' ' +type + ' ' + '(' + str(tap_x) + ',' + str(tap_y) + ') result:'+ str(result) + '\n'
        print(log_str.strip('\n'))
        log_file = open('./yys_log/' + constant.device_id + 'auto_team.txt', 'a')
        log_file.write(log_str)
        log_file.close()

        return True
    else:
        return False

def start(leader):

    team_start_fighting = cv.imread('./yys_mark/team_start_fighting_' + constant.device_id + '.jpg')
    team_win_mark_box = cv.imread('./yys_mark/team_win_mark_box_' + constant.device_id + '.jpg')
    team_win_mark_drum = cv.imread('./yys_mark/team_win_mark_drum_' + constant.device_id + '.jpg')
    stop_times_threshold = 0
    battle_times = 0
    battle_start_time = datetime.datetime.now()
    sleep_time_per_cap = 0.3
    while True:
        time.sleep(sleep_time_per_cap)
        image = save_screen_cap_with_minicap(constant.device_id + '_team', './yys_temp/')
        stop_times_threshold = stop_times_threshold + 1
        if stop_times_threshold >= 300:
            exception()
            pass

        #判断是否存在开始战斗按钮
        if leader == True:
            if judge_pic_state(team_start_fighting, image, constant.team_start_fighting, constant.team_start_fighting , constant.team_start_fighting_threshold, 'team_start_fighting'):
                battle_end_time = datetime.datetime.now()
                battle_duration = battle_end_time - battle_start_time
                battle_start_time = battle_end_time
                battle_times = battle_times + 1
                times_log = "************ 第%s次御魂 用时%s************" % (str(battle_times), str(battle_duration))
                log_file = open('./yys_log/' + constant.device_id + 'auto_team.txt', 'a')
                log_file.write(times_log + '\n')
                log_file.close()
                continue

        # if leader == False:
        #     pass
        #     #todo 增加点击同意组队的按钮
        #


        #判断是否战斗胜利
        if judge_pic_state(team_win_mark_drum, image, constant.team_win_mark_drum, constant.team_win_mark_drum_tap, constant.team_win_mark_drum_threshold, 'team_win_mark_drum'):
            continue

        #判断是否到了宝箱出现的结束界面
        if judge_pic_state(team_win_mark_box, image, constant.team_win_mark_box, constant.team_win_mark_box_tap, constant.team_win_mark_box_threshold ,'team_win_mark_box'):
            stop_times_threshold = 0
            continue



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--phone', type=str, default='MI8')
    parser.add_argument('--leader', type=bool, default=False)
    args = parser.parse_args()
    global constant
    constant = __import__('Constant_' + args.phone)
    start(args.leader)
