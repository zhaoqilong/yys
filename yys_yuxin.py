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
    while True:
        game_operator.get_phone_picture()

        if game_operator.is_yuxin_challenge():
            game_operator.tap_after_yuxin_challenge()

        if game_operator.is_prepare():
            game_operator.tap_after_prepare()
            time.sleep(5)

        if game_operator.is_xuanshang():
            game_operator.tap_after_xuanshang()

        if game_operator.is_fight_end() or game_operator.is_drum():
            game_operator.tap_after_fight_end()
            time.sleep(1)
