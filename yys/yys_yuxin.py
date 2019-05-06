#!/usr/bin/env python3
# coding:utf-8
import time
import argparse
from yys.utils.device_config import DeviceConfig
from yys.game.lidao_game_operator import LidaoGameOperator
from yys.utils.exception_utils import ExceptionUtils

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--p', type=str, default='MI8')
    args = parser.parse_args()
    device_config = DeviceConfig(args.p)
    exception_utils = ExceptionUtils(device_config)
    game_operator = LidaoGameOperator(device_config)
    while True:

        game_operator.get_phone_picture()
        if exception_utils.check_exception() is not None:
            print(exception_utils.check_exception())
            exit(0)


        if game_operator.is_yuxin_challenge():
            game_operator.tap_after_yuxin_challenge()
            exception_utils.update_step('is_yuxin_challenge', 1)
            time.sleep(1)
            continue

        if game_operator.is_prepare():
            game_operator.tap_after_prepare()
            exception_utils.update_step('is_prepare', 30)
            time.sleep(30)
            continue

        if game_operator.is_xuanshang() or game_operator.is_xuanshang2():
            exception_utils.update_step('is_xuanshang')
            game_operator.tap_after_xuanshang()
            continue

        if game_operator.is_fight_end() or game_operator.is_win_box():
            game_operator.tap_after_fight_end()
            exception_utils.update_step('is_fight_end', 2)
            time.sleep(2)
            continue

        exception_utils.update_empty_loop()
