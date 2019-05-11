#!/usr/bin/env python3
# coding:utf-8
import time
import argparse
from yys.utils.device_config import DeviceConfig
from yys.game.douji_operator import DoujiGameOperator
from yys.utils.exception_utils import ExceptionUtils

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--p', type=str, default='MI8')
    args = parser.parse_args()
    device_config = DeviceConfig(args.p)
    exception_utils = ExceptionUtils(device_config)
    game_operator = DoujiGameOperator(device_config)
    while True:

        game_operator.get_phone_picture()
        # if exception_utils.check_exception() is not None:
        #     print(exception_utils.check_exception())
        #     exit(0)

        if game_operator.is_douji_start():
            game_operator.tap_after_douji_start()
            exception_utils.update_step('is_douji_start', 1)
            time.sleep(1)
            continue

        if game_operator.is_douji_auto_choose():
            game_operator.tap_after_douji_auto_choose()
            exception_utils.update_step('is_douji_auto_choose', 30)
            time.sleep(30)
            continue

        if game_operator.is_xuanshang() or game_operator.is_xuanshang2():
            exception_utils.update_step('is_xuanshang')
            game_operator.tap_after_xuanshang()
            continue

        if game_operator.is_douji_end():
            game_operator.tap_after_fight_end()
            exception_utils.update_step('is_douji_end', 2)
            time.sleep(2)
            continue

        exception_utils.update_empty_loop()
