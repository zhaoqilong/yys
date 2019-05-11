# coding:utf-8

from yys.utils.device_config import DeviceConfig
from yys.game.game_operator import GameOperator
import cv2 as cv

__init__ = ['DaoguanGameOperator']


class DaoguanGameOperator(GameOperator):

    def __init__(self, device_config: DeviceConfig):
        super(DaoguanGameOperator, self).__init__(device_config)
        self.daoguan_prepare = cv.imread('../picture/yys_mark/' + self.device_name + '_daoguan_prepare.jpg')
        self.daoguan_prepare_coor = self.picture_info.get('daoguan_prepare')
        self.daoguan_prepare_tap = self.picture_info.get('daoguan_prepare_tap')


    def is_daoguan_prepare(self):
        is_match, result = self.judge_pic_state(self.daoguan_prepare, self.daoguan_prepare_coor)
        if is_match:
            self.log_utils.log('is_daoguan_challenge ', result)
        return is_match

    def tap_after_daoguan_prepare(self):
        tap_coor = self.random_tap(self.daoguan_prepare_tap)
        self.android_utils.tap_point(tap_coor[0], tap_coor[1])
