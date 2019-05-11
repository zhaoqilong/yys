#!/usr/bin/env python3
# coding:utf-8
import time
import argparse
from yys.utils.device_config import DeviceConfig
from yys.game.huntu_game_operator import HuntuGameOperator
from yys.utils.exception_utils import ExceptionUtils

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--p', type=str, default='MI8')
    args = parser.parse_args()
    device_config = DeviceConfig(args.p)
    exception_utils = ExceptionUtils(device_config)
    game_operator = HuntuGameOperator(device_config)
    stage = 'one'
    while True:

        game_operator.get_phone_picture()
        if exception_utils.check_exception() is not None:
            print(exception_utils.check_exception())
            exit(0)

        if game_operator.is_xuanshang() or game_operator.is_xuanshang2():
            exception_utils.update_step('is_xuanshang')
            game_operator.tap_after_xuanshang()

        if game_operator.is_challenge_btn():
            stage = 'one'
            game_operator.tap_after_challenge_btn()
            exception_utils.update_step('is_challenge_btn', 1)
            time.sleep(1)
            continue

        if stage == 'one' and game_operator.is_huntu_round_one():
            stage = 'two'
            game_operator.tap_after_prepare()
            time.sleep(1)
            game_operator.tap_after_huntu_round_one()
            exception_utils.update_step('is_huntu_round_one')
            continue

        if stage == 'two' and game_operator.is_huntu_round_two():
            game_operator.tap_after_huntu_round_two()
            exception_utils.update_step('is_huntu_round_two')
            stage = 'three'
            continue

        if stage == 'three' and game_operator.is_huntu_round_three():
            game_operator.tap_after_huntu_round_three()
            exception_utils.update_step('is_huntu_round_three')
            stage = 'end'
            continue

        if stage == 'end' and (game_operator.is_fight_end() or game_operator.is_win_box()):
            game_operator.tap_after_fight_end()
            exception_utils.update_step('is_fight_end', 2)
            time.sleep(2)
            stage = 'one'
            continue

        exception_utils.update_empty_loop()
