# coding:utf-8

from yys.utils.device_config import DeviceConfig
from yys.game.game_operator import GameOperator
import cv2 as cv

__init__ = ['DoujiGameOperator']


class DoujiGameOperator(GameOperator):

    def __init__(self, device_config: DeviceConfig):
        super(DoujiGameOperator, self).__init__(device_config)
        self.douji_start = cv.imread('../picture/yys_mark/' + self.device_name + '_douji_start.jpg')
        self.douji_auto_choose = cv.imread('../picture/yys_mark/' + self.device_name + '_douji_auto_choose.jpg')
        self.douji_end = cv.imread('../picture/yys_mark/' + self.device_name + '_douji_end.jpg')

        self.douji_start_coor = self.picture_info.get('douji_start')
        self.douji_auto_choose_coor = self.picture_info.get('douji_auto_choose')
        self.douji_end_coor = self.picture_info.get('douji_end')

    def is_douji_start(self):
        is_match, result = self.judge_pic_state(self.douji_start, self.douji_start_coor)
        if is_match:
            self.log_utils.log('is_douji_start ', result)
        return is_match

    def tap_after_douji_start(self):
        tap_coor = self.random_tap(self.douji_start_coor)
        self.android_utils.tap_point(tap_coor[0], tap_coor[1])

    def is_douji_auto_choose(self):
        is_match, result = self.judge_pic_state(self.douji_auto_choose, self.douji_auto_choose_coor)
        if is_match:
            self.log_utils.log('is_douji_auto_choose ', result)
        return is_match

    def tap_after_douji_auto_choose(self):
        tap_coor = self.random_tap(self.douji_auto_choose_coor)
        self.android_utils.tap_point(tap_coor[0], tap_coor[1])

    def is_douji_end(self):
        is_match, result = self.judge_pic_state(self.douji_end, self.douji_end_coor)
        if is_match:
            self.log_utils.log('is_douji_end ', result)
        return is_match

    def tap_after_douji_end(self):
        tap_coor = self.random_tap(self.douji_end_coor)
        self.android_utils.tap_point(tap_coor[0], tap_coor[1])
