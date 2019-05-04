# coding:utf-8
from utils.device_config import DeviceConfig
from utils.picture_utils import PictureUtil
from utils.android_utils import AndroidUtil
from utils.log_utils import LogUtils
import time
import cv2 as cv
import numpy as np
import random

__all__ = ['GameOperator']


class GameOperator(object):

    def __init__(self, device_config: DeviceConfig):

        self.device_config = device_config
        self.device_info = device_config.device_info
        self.picture_info = device_config.picture_info
        self.operator_config = device_config.operator_config

        self.android_utils = AndroidUtil(self.device_info)
        self.device_name = self.device_info.get('device_name')
        self.device_id = self.device_info.get('device_id')
        self.sleep_after_start = self.operator_config.get('sleep_after_start')

        self.buff = cv.imread('./picture/yys_mark/' + self.device_name + '_buff.jpg')
        self.challenge_btn = cv.imread('./picture/yys_mark/' + self.device_name + '_challenge_btn.jpg')
        self.fight_data = cv.imread('./picture/yys_mark/' + self.device_name + '_fight_data.jpg')
        self.xuanshang = cv.imread('./picture/yys_mark/' + self.device_name + '_xuanshang.jpg')
        self.xuanshang2 = cv.imread('./picture/yys_mark/' + self.device_name + '_xuanshang2.jpg')
        self.win_box = cv.imread('./picture/yys_mark/' + self.device_name + '_win_box.jpg')
        self.prepare = cv.imread('./picture/yys_mark/' + self.device_name + '_prepare.jpg')

        # todo 网络错误

        # 点击位置
        self.buff_coor = self.picture_info.get('buff')
        self.challenge_btn_coor = self.picture_info.get('challenge_btn')
        self.fight_data_coor = self.picture_info.get('fight_data')
        self.end_tap = self.picture_info.get('end_tap')
        self.xuanshang_coor = self.picture_info.get('xuanshang')
        self.xuanshang2_coor = self.picture_info.get('xuanshang2')
        self.xuanshang_tap = self.picture_info.get('xuanshang_tap')
        self.win_box_coor = self.picture_info.get('win_box')
        self.prepare_coor = self.picture_info.get('prepare')
        self.prepare_tap = self.picture_info.get('prepare_tap')

        self.phone_picture = None
        self.log_utils = LogUtils(device_config)
        self.picture_utils = PictureUtil

    def get_phone_picture(self):
        self.phone_picture = self.android_utils.get_screen_cap()

    def judge_pic_state(self, mark, coor):
        if self.phone_picture is None:
            print('Error')
            return False
        image_crop = PictureUtil.get_picture_part(image=self.phone_picture, coordinate=coor)
        difference = cv.subtract(mark, image_crop)
        result = np.mean(difference)
        return abs(result - coor['threshold']) < coor['offset'], result

    def is_fight_end(self):
        is_match, result = self.judge_pic_state(self.fight_data, self.fight_data_coor)
        if is_match:
            self.log_utils.log('is_fight_end ', result)
        return is_match

    def tap_after_fight_end(self):
        tap_coor = self.random_tap(self.end_tap)
        self.android_utils.tap_point(tap_coor[0], tap_coor[1])

    def is_win_box(self):
        is_match, result = self.judge_pic_state(self.win_box, self.win_box_coor)
        if is_match:
            self.log_utils.log('is_win_box ', result)
        return is_match

    def is_challenge_btn(self):
        is_match, result = self.judge_pic_state(self.challenge_btn, self.challenge_btn_coor)
        if is_match:
            self.log_utils.log('is_challenge_btn ', result)
        return is_match

    def tap_after_challenge_btn(self):
        tap_coor = self.random_tap(self.challenge_btn_coor)
        self.android_utils.tap_point(tap_coor[0], tap_coor[1])

    def is_prepare(self):
        is_match, result = self.judge_pic_state(self.prepare, self.prepare_coor)
        if is_match:
            self.log_utils.log('is_prepare ', result)
        return is_match

    def tap_after_prepare(self):
        tap_coor = self.random_tap(self.prepare_tap)
        self.android_utils.tap_point(tap_coor[0], tap_coor[1])

    def is_buff(self):
        return self.judge_pic_state(self.buff, self.buff_coor)

    def tap_after_buff(self):
        tap_coor = self.random_tap(self.buff_coor)
        self.android_utils.tap_point(tap_coor[0], tap_coor[1])

    def is_xuanshang(self):
        is_match, result = self.judge_pic_state(self.xuanshang, self.xuanshang_coor)
        if is_match:
            self.log_utils.log('is_xuanshang ', result)
        return is_match

    def is_xuanshang2(self):
        is_match, result = self.judge_pic_state(self.xuanshang2, self.xuanshang2_coor)
        if is_match:
            self.log_utils.log('is_xuanshang2 ', result)
        return is_match


    def tap_after_xuanshang(self):
        tap_coor = self.random_tap(self.xuanshang_tap)
        self.android_utils.tap_point(tap_coor[0], tap_coor[1])

    def random_tap(self, coor):
        x_offset = int(abs(coor['x1'] - coor['x2']) / 2)
        y_offset = int(abs(coor['y1'] - coor['y2']) / 2)
        tap_x = (coor['x1'] + coor['x2']) / 2 + random.randint(-x_offset, x_offset)
        tap_y = (coor['y1'] + coor['y2']) / 2 + random.randint(-y_offset, y_offset)
        return [tap_x, tap_y]

    def stop(self):
        self.android_utils.save_screen_cap('./picture/yys_exception')
        time.sleep(10)
        self.android_utils.stop_yys()
