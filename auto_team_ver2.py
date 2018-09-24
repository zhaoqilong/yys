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

def tap_point(tap_area_dict, type, result):
    x_offset = int(abs(tap_area_dict['x1'] - tap_area_dict['x2']) / 2)
    y_offset = int(abs(tap_area_dict['y1'] - tap_area_dict['y2']) / 2)
    tap_x = (tap_area_dict['x1'] + tap_area_dict['x2']) / 2 + random.randint(-x_offset, x_offset)
    tap_y = (tap_area_dict['y1'] + tap_area_dict['y2']) / 2 + random.randint(-y_offset, y_offset)
    command = 'adb -s '+ constant.device_id +' shell input tap ' + str(int(tap_x)) + ' ' + str(int(tap_y))
    os.system(command)
    tap_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    log_str = tap_time + ' ' + type + ' ' + '(' + str(tap_x) + ',' + str(tap_y) + ') result:' + str(result) + '\n'
    print(log_str.strip('\n'))
    log_file = open('./yys_log/' + constant.device_id + 'auto_team.txt', 'a')
    log_file.write(log_str)
    log_file.close()

def close_yys():
    stop_command = 'adb -s ' + constant.device_id + ' shell am force-stop com.netease.onmyoji'
    os.system(stop_command)
    sys.exit(0)

#判断图片是否存在某位置图像，同时随机点按
def judge_pic_state(mark_pic, image, pic_size_dict, tap_area_dict , threshold, type):

    real_time_pic = get_picture_part(image, pic_size_dict)
    difference = cv.subtract(mark_pic, real_time_pic)
    result = np.mean(difference)
    # #
    # print("***************************************")
    # print(str(type) + "  " + str(result))
    # print("***************************************")

    if abs(result - threshold[0]) <= threshold[1]:
        if type == 'team_win_mark_drum':
            tap_point(tap_area_dict, type, result)
            tap_point(tap_area_dict, type, result)
        else:
            tap_point(tap_area_dict , type, result)
        return True
    else:
        return False



def start():

    team_start_fighting = cv.imread('./yys_mark/team_start_fighting_' + constant.device_id + '.jpg')
    team_win_mark_box = cv.imread('./yys_mark/team_win_mark_box_' + constant.device_id + '.jpg')
    team_win_mark_drum = cv.imread('./yys_mark/team_win_mark_drum_' + constant.device_id + '.jpg')
    reward = cv.imread('./yys_mark/reward_' + constant.device_id + '.jpg')
    later_btn = cv.imread('./yys_mark/later_btn_' + constant.device_id + '.jpg')
    damo = cv.imread('./yys_mark/damo_' + constant.device_id + '.jpg')
    net_lost = cv.imread('./yys_mark/net_lost_' + constant.device_id + '.jpg')
    buff_area = cv.imread('./yys_mark/buff_area_' + constant.device_id + '.jpg')
    buff_on = cv.imread('./yys_mark/buff_on_' + constant.device_id + '.jpg')
    buff_off = cv.imread('./yys_mark/buff_off_' + constant.device_id + '.jpg')
    stop_times_threshold = 0
    battle_times = 0
    battle_start_time = datetime.datetime.now()
    while True:
        time.sleep(0.2)
        image = save_screen_cap_with_minicap(constant.device_id + '_team', './yys_temp/')
        stop_times_threshold = stop_times_threshold + 1
        if stop_times_threshold >= 200:
            save_screen_cap_with_minicap(constant.device_id + "_" + "_exception", './yys_exception')
            print("游戏出现突发情况，已将游戏界面保存到./yys_exception 文件夹中")
            if judge_pic_state(buff_area, image, constant.buff_area, constant.buff_area,
                                   constant.buff_area_threshold, 'buff_area'):
                time.sleep(4)
            if judge_pic_state(buff_on, image, constant.buff_btn, constant.buff_btn,
                                       constant.buff_on_threshold, 'buff_on'):
                time.sleep(10)
                close_yys()

        if stop_times_threshold >= 300:
            close_yys()

        #判断是否出现了悬赏，自定点击不接受
        if judge_pic_state(reward, image, constant.reward, constant.reward_tap,
                           constant.reward_threshold, 'reward'):
            time.sleep(2)
            continue

        #判断是否出现了宠物或者其他对话框，这时候应该点击稍后
        if judge_pic_state(later_btn, image, constant.later_btn, constant.later_btn_tap,
                           constant.later_btn_threshold, 'later_btn'):
            time.sleep(2)
            continue

            # 判断是否出现网络错误
        if judge_pic_state(net_lost, image, constant.net_lost, constant.net_lost, constant.net_lost_threshold,
                               'net_lost'):
            time.sleep(2)
            continue

        #判断是否存在开始战斗按钮
        if judge_pic_state(team_start_fighting, image, constant.team_start_fighting,
                               constant.team_start_fighting , constant.team_start_fighting_threshold, 'team_start_fighting'):
            battle_end_time = datetime.datetime.now()
            battle_times = battle_times + 1
            battle_duration = battle_end_time - battle_start_time
            battle_start_time = battle_end_time
            times_log = "************ 第%s次御魂 用时%s************" % (str(battle_times), str(battle_duration))
            log_file = open('./yys_log/' + constant.device_id + 'auto_team.txt', 'a')
            log_file.write(times_log + '\n')
            log_file.close()
            time.sleep(2)
            continue


        # 判断是否出现达摩
        if judge_pic_state(damo, image, constant.team_damo, constant.team_damo_tap,
                               constant.damo_threshold, 'team_damo'):
            continue

        #判断是否战斗胜利
        if judge_pic_state(team_win_mark_drum, image, constant.team_win_mark_drum,
                           constant.team_win_mark_drum_tap, constant.team_win_mark_drum_threshold, 'team_win_mark_drum'):
            continue

        #判断是否到了宝箱出现的结束界面
        if judge_pic_state(team_win_mark_box, image, constant.team_win_mark_box,
                           constant.team_win_mark_box_tap, constant.team_win_mark_box_threshold ,'team_win_mark_box'):
            stop_times_threshold = 0
            continue


if __name__ == '__main__':
    #todo 多线程并发运行
    #todo 增加数据库，增加刷御魂次数的统计
    #todo 增加运行环境参数配置页面
    #todo 增加网络错误之后重新开启御魂
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--p', type=str, default='5')
    args = parser.parse_args()
    global constant
    constant = __import__('Constant_MI' + args.p)
    start()
