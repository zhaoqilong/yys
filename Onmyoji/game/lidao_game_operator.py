# coding:utf-8

from Onmyoji.utils.device_config import DeviceConfig
from Onmyoji.game.game_operator import GameOperator
import cv2 as cv

__init__ = ['LidaoGameOperator']


class LidaoGameOperator(GameOperator):

    def __init__(self, device_config: DeviceConfig):
        super(LidaoGameOperator, self).__init__(device_config)
        self.yuxin_challenge = cv.imread('./picture/yys_mark/' + self.device_name + '_yuxin_challenge.jpg')
        self.yuxin_challenge_coor = self.picture_info.get('yuxin_challenge')

    def is_yuxin_challenge(self):
        is_match, result = self.judge_pic_state(self.yuxin_challenge, self.yuxin_challenge_coor)
        if is_match:
            self.log_utils.log('is_yuxin_challenge ', result)
        return is_match

    def tap_after_yuxin_challenge(self):
        tap_coor = self.random_tap(self.yuxin_challenge_coor)
        self.android_utils.tap_point(tap_coor[0], tap_coor[1])
