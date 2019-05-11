#!/usr/bin/env python3
# coding:utf-8
import time
import argparse
import random
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
    while True:

        game_operator.get_phone_picture()
        if exception_utils.check_exception() is not None:
            print(exception_utils.check_exception())
            exit(0)

        # if game_operator.is_xuanshang() or game_operator.is_xuanshang2():
        #     exception_utils.update_step('is_xuanshang')
        #     game_operator.tap_after_xuanshang()

        if game_operator.is_yuhun_single_challenge() or game_operator.is_team_challenge_btn():
            game_operator.tap_after_yuhun_single_challenge()
            exception_utils.update_step('is_yuhun_single_challenge', 1)
            continue

        if game_operator.is_team_challenge_btn():
            game_operator.tap_after_team_challenge_btn()
            exception_utils.update_step('is_team_challenge_btn', 1)
            continue

        if game_operator.is_huntu_round_one():
            time.sleep(4)
            game_operator.tap_after_huntu_round_one()
            exception_utils.update_step('is_huntu_round_one')
            continue

        if game_operator.is_huntu_round_two():
            game_operator.tap_after_huntu_round_two()
            time.sleep(random.uniform(0.4, 0.5))
            game_operator.tap_after_huntu_round_two()
            time.sleep(random.uniform(0.4, 0.5))
            game_operator.tap_after_huntu_round_two()
            time.sleep(random.uniform(0.4, 0.5))
            exception_utils.update_step('is_huntu_round_two')
            continue

        if game_operator.is_huntu_round_three():
            game_operator.tap_after_huntu_round_three()
            time.sleep(random.uniform(0.4, 0.5))
            game_operator.tap_after_huntu_round_three()
            time.sleep(random.uniform(0.4, 0.5))
            game_operator.tap_after_huntu_round_three()
            time.sleep(random.uniform(0.4, 0.5))
            exception_utils.update_step('is_huntu_round_three')
            continue

        if game_operator.is_fight_end():
            game_operator.tap_after_fight_end()
            exception_utils.update_step('is_fight_end', 2)
            time.sleep(1)
            continue

        exception_utils.update_empty_loop()
