#!/usr/bin/env python3
# coding:utf-8
import os
import time
import argparse
from utils.device_config import DeviceConfig
from game.lidao_game_operator import LidaoGameOperator

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--p', type=str, default='MI8')
    args = parser.parse_args()
    device_config = DeviceConfig(args.p)
    game_operator = LidaoGameOperator(device_config)
    stop_times = 1000
    current_times = 0
    while True:

        game_operator.get_phone_picture()

        if game_operator.is_yuxin_challenge():
            game_operator.tap_after_yuxin_challenge()
            time.sleep(1)

        if game_operator.is_prepare():
            game_operator.tap_after_prepare()
            time.sleep(30)

        if game_operator.is_xuanshang() or game_operator.is_xuanshang2():
            game_operator.tap_after_xuanshang()

        if game_operator.is_fight_end() or game_operator.is_win_box():
            game_operator.tap_after_fight_end()
            time.sleep(2)
