# coding:utf-8
import os
import time
import cv2 as cv
import argparse
import numpy as np
import random
import sys
from utils.we_chat_utils import WechatUtils
from utils.device_config import DeviceConfig
from utils.picture_utils import PictureUtil
from utils.android_utils import AndroidUtil
from game.game_operator import GameOperator

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--p', type=str, default='MI8')
    parser.add_argument('--t', type=str, default='yuling')
    args = parser.parse_args()
    operator_type = args.t
    device_config = DeviceConfig(args.p)
    game_operator = GameOperator(device_config)
    while True:
        game_operator.get_phone_picture()

        if game_operator.is_challenge_btn():
            game_operator.tap_after_challenge_btn()
            time.sleep(game_operator.sleep_after_start.get(operator_type))

        if game_operator.is_xuanshang():
            game_operator.tap_after_xuanshang()

        if game_operator.is_fight_end() or game_operator.is_drum():
            game_operator.tap_after_fight_end()
            time.sleep(1)
