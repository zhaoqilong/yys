#coding:utf-8
import os
import time
import cv2 as cv
import numpy as np
import random
import sys
import datetime
import argparse



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


#判断图片是否存在某位置图像，同时随机点按
def judge_pic_state(mark_pic, image, pic_size_dict, tap_area_dict , threshold, type):

    real_time_pic = get_picture_part(image, pic_size_dict)
    # cv.imshow('reward', real_time_pic)
    # cv.waitKey(0)
    difference = cv.subtract(mark_pic, real_time_pic)
    result = np.mean(difference)

    print("***************************************")
    print(str(type) + "  " + str(result))
    print("***************************************")


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

    image = cv.imread("./yys_debug/" + "reward_bug" + '.jpg')

    if judge_pic_state(reward, image, constant.reward, constant.reward_tap,constant.reward_threshold, 'reward'):
        pass

    if judge_pic_state(later_btn, image, constant.later_btn, constant.later_btn_tap,constant.later_btn_threshold, 'later_btn'):
        pass

    if judge_pic_state(team_start_fighting, image, constant.team_start_fighting, constant.team_start_fighting , constant.team_start_fighting_threshold, 'team_start_fighting'):
        pass

    if judge_pic_state(team_win_mark_drum, image, constant.team_win_mark_drum, constant.team_win_mark_drum_tap, constant.team_win_mark_drum_threshold, 'team_win_mark_drum'):
        pass

    if judge_pic_state(team_win_mark_box, image, constant.team_win_mark_box, constant.team_win_mark_box_tap, constant.team_win_mark_box_threshold ,'team_win_mark_box'):
        pass



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--phone', type=str, default='MI5')
    args = parser.parse_args()
    global constant
    constant = __import__('Constant_' + args.phone)
    start()
