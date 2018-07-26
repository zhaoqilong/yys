#coding:utf-8

import os
import time
import cv2 as cv
import Constant_MI8 as constant
import numpy as np



def save_screen_cap_v1(pic_name):
    screencap = 'adb -s '+ constant.device_id +' shell /system/bin/screencap -p /sdcard/' + pic_name + '.png'
    save_picture = 'adb -s '+ constant.device_id +' pull /sdcard/' + pic_name + '.png ' + './yys_screenshots'
    delete_picture = 'adb -s '+ constant.device_id +' shell rm /sdcard/' + pic_name + '.png'
    os.system(screencap)
    os.system(save_picture)
    os.system(delete_picture)
    #image = cv.imread('./yys_temp/' +pic_name+'.png')
    #cv.imshow("Image", image)
    #cv.waitKey(0)

def save_screen_cap_with_minicap(pic_name, path):
    screencap = 'adb -s '+ constant.device_id + ' shell \"LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P ' + constant.size + '@'+ constant.size  + '/0 -s > /mnt/sdcard/yys/' + pic_name + '.jpg\"'
    save_picture = 'adb -s ' + constant.device_id + ' pull /mnt/sdcard/yys/'+ pic_name +'.jpg ' + path + ' > /dev/null'
    os.system(screencap)
    os.system(save_picture)
    image = cv.imread(path + pic_name+'.jpg')
    return image

def show_pic(name):
    image = cv.imread('./yys_screenshots/' + name)
    cv.imshow("Image", image)
    cv.waitKey(0)

def cut_picture(name,out_name,coordinate):
    image = cv.imread('./yys_screenshots/' + name)
    image = image[coordinate['y1']:coordinate['y2'], coordinate['x1']:coordinate['x2']]
    cv.imwrite('./yys_mark/' + out_name + "_" + constant.device_id +'.jpg' ,image)

if __name__ == '__main__':
    # save_screen_cap_v1('test')
    save_screen_cap_with_minicap('Mi8_reward','./yys_screenshots')

    # show_pic('MI5_net_lost.jpg')
    # show_pic('Mi8_team_start_fighting.jpg')
    # show_pic('Mi8_team_win_mark_box.jpg')
    # show_pic('Mi8_team_win_mark_drum.jpg')
    # show_pic('Mi8_team_win_mark_drum.jpg')

    # cut_picture('Mi8_team_failure.jpg','team_failure',constant.team_failure2)
    # cut_picture('Mi8_team_start_fighting.jpg', 'start_fighting', constant.start_fighting2)
    #cut_picture('Mi8_invite.jpg', 'net_lost', constant.net_lost)


    # cut_picture('Mi5_single_failure.jpg', 'single_failure', constant.single_failure)
    # cut_picture('Mi5_win_mark_box.jpg','win_mark_box',constant.win_mark_box)
    # cut_picture('Mi5_win_mark_drum.jpg','win_mark_drum',constant.win_mark_drum)
    # cut_picture('Mi5_challenge_btn.jpg','challenge_btn',constant.challenge_btn)
