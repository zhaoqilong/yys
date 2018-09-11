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

    #save_screen_cap_v1('test')
    #save_screen_cap_with_minicap('Mi8_continue_join','./yys_screenshots')
    #save_screen_cap_with_minicap('Mi5_continue_team','./yys_screenshots')
#

    #show_pic('Mi5_continue_team.jpg')
    show_pic('Mi5_later_btn.jpg')
    # show_pic('Mi5_team_change.jpg')
    # show_pic('Mi8_team_win_mark_drum.jpg')
    # show_pic('Mi8_team_win_mark_drum.jpg')

    #cut_picture('Mi8_damo.jpg','damo',constant.team_damo)


    # cut_picture('Mi8_team_start_fighting.jpg', 'start_fighting', constant.start_fighting2)
    # cut_picture('Mi8_later_btn.jpg', 'later_btn', constant.later_btn)


    #cut_picture('Mi5_reward.jpg', 'reward', constant.reward)
    # cut_picture('Mi5_win_mark_box.jpg','win_mark_box',constant.win_mark_box)
    # cut_picture('Mi5_win_mark_drum.jpg','win_mark_drum',constant.win_mark_drum)
    # cut_picture('Mi5_challenge_btn.jpg','challenge_btn',constant.challenge_btn)
