# coding:utf-8

from yys.utils.device_config import DeviceConfig
from yys.game.game_operator import GameOperator
import cv2 as cv

__init__ = ['HuntuGameOperator']


class HuntuGameOperator(GameOperator):

    def __init__(self, device_config: DeviceConfig):
        super(HuntuGameOperator, self).__init__(device_config)
        self.huntu_round_one = cv.imread('../picture/yys_mark/' + self.device_name + '_huntu_round_one.jpg')
        self.huntu_round_two = cv.imread('../picture/yys_mark/' + self.device_name + '_huntu_round_two.jpg')
        self.huntu_round_three = cv.imread('../picture/yys_mark/' + self.device_name + '_huntu_round_three.jpg')

        self.huntu_round_one_coor = self.picture_info.get('huntu_round_one')
        self.huntu_round_two_coor = self.picture_info.get('huntu_round_two')
        self.huntu_round_three_coor = self.picture_info.get('huntu_round_three')

        self.huntu_round_one_tap = self.picture_info.get('huntu_round_one_tap')
        self.huntu_round_two_tap = self.picture_info.get('huntu_round_two_tap')
        self.huntu_round_three_tap = self.picture_info.get('huntu_round_three_tap')


    def is_huntu_round_one(self):
        is_match, result = self.judge_pic_state(self.huntu_round_one, self.huntu_round_one_coor)
        if is_match:
            self.log_utils.log('is_huntu_round_one ', result)
        return is_match

    def tap_after_huntu_round_one(self):
        tap_coor = self.random_tap(self.huntu_round_one_tap)
        self.android_utils.tap_point(tap_coor[0], tap_coor[1])

    def is_huntu_round_two(self):
        is_match, result = self.judge_pic_state(self.huntu_round_two, self.huntu_round_two_coor)
        if is_match:
            self.log_utils.log('is_huntu_round_two ', result)
        return is_match

    def tap_after_huntu_round_two(self):
        tap_coor = self.random_tap(self.huntu_round_two_tap)
        self.android_utils.tap_point(tap_coor[0], tap_coor[1])

    def is_huntu_round_three(self):
        is_match, result = self.judge_pic_state(self.huntu_round_three, self.huntu_round_three_coor)
        if is_match:
            self.log_utils.log('is_huntu_round_three ', result)
        return is_match

    def tap_after_huntu_round_three(self):
        tap_coor = self.random_tap(self.huntu_round_three_tap)
        self.android_utils.tap_point(tap_coor[0], tap_coor[1])

