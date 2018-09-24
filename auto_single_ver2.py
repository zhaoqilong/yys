#coding:utf-8
import os
import time
import cv2 as cv
import argparse
import numpy as np
import random
import sys
from WeChatUtils import WechatUtils

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

def stop_yys():
    stop_command = 'adb -s ' + constant.device_id + ' shell am force-stop com.netease.onmyoji'
    os.system(stop_command)
    sys.exit(0)

#判断图片是否存在某位置图像，同时随机点按
def judge_pic_state(mark_pic, image, pic_size_dict, tap_area_dict, threshold, type):

    real_time_pic = get_picture_part(image, pic_size_dict)
    difference = cv.subtract(mark_pic, real_time_pic)
    result = np.mean(difference)

    if abs(result - threshold[0]) < threshold[1]:
        x_offset = int(abs(tap_area_dict['x1'] - tap_area_dict['x2']) / 2)
        y_offset = int(abs(tap_area_dict['y1'] - tap_area_dict['y2']) / 2)
        tap_x = (tap_area_dict['x1'] + tap_area_dict['x2']) / 2 + random.randint(-x_offset,x_offset)
        tap_y = (tap_area_dict['y1'] + tap_area_dict['y2']) / 2 + random.randint(-y_offset,y_offset)
        tap_point(tap_x, tap_y)
        tap_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_str = tap_time + ' ' +type + ' ' + '(' + str(tap_x) + ',' + str(tap_y) + ')  result=' + str(result) + '\n'
        with open('./yys_log/' + constant.device_id + '_auto_single_player.txt' ,'a') as log_file:
            log_file.write(log_str)
        return True
    else:
        return False

def start(use_wechat):

    friend_name = 'main'
    if use_wechat==True:
        wechat = WechatUtils(friend_name)
    challenge_btn = cv.imread('./yys_mark/challenge_btn_' + constant.device_id + '.jpg')
    win_mark_box = cv.imread('./yys_mark/win_mark_box_' + constant.device_id + '.jpg')
    net_lost = cv.imread('./yys_mark/net_lost_' + constant.device_id + '.jpg')
    single_failure = cv.imread('./yys_mark/single_failure_' + constant.device_id + '.jpg')
    reward = cv.imread('./yys_mark/reward_' + constant.device_id + '.jpg')
    later_btn = cv.imread('./yys_mark/later_btn_' + constant.device_id + '.jpg')
    stop_times = 0
    battle_times = 0

    while True:
        image = save_screen_cap_with_minicap(constant.device_id, './yys_temp/')
        stop_times = stop_times + 1

        if stop_times >= 3000:
            if use_wechat == True:
                wechat.send_question('游戏因为异常退出！！')
            stop_yys()

        #判断是否存在挑战按钮
        if judge_pic_state(challenge_btn, image, constant.challenge_btn, constant.challenge_btn , constant.single_challenge_btn_threshold, 'challenge_btn'):
            continue

        #判断是否到了宝箱出现的结束界面
        if judge_pic_state(win_mark_box, image, constant.win_mark_box, constant.win_mark_box_tap, constant.single_win_mark_box_threshold ,'win_mark_box'):
            stop_times = 0
            battle_times = battle_times + 1
            continue

        #判断是否战斗失败
        if judge_pic_state(single_failure, image, constant.single_failure, constant.single_failure_tap, constant.single_failure_threshold, 'single_failure'):
            stop_times = 0
            continue

        #判断是否出现网络错误
        if judge_pic_state(net_lost, image, constant.net_lost, constant.net_lost, constant.net_lost_threshold, 'net_lost'):
            stop_times = 0
            continue

        # 判断是否出现了悬赏，自定点击不接受
        if judge_pic_state(reward, image, constant.reward, constant.reward_tap,
                               constant.reward_threshold, 'reward'):
            time.sleep(2)
            continue

        # 判断是否出现了宠物或者其他对话框，这时候应该点击稍后
        if judge_pic_state(later_btn, image, constant.later_btn, constant.later_btn_tap,
                               constant.later_btn_threshold, 'later_btn'):
            time.sleep(2)
            continue



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--phone', type=str, default='MI5')
    parser.add_argument('--wechat', type=bool, default=False)
    args = parser.parse_args()
    global constant
    constant = __import__('Constant_single_' + args.phone)
    start(False)
