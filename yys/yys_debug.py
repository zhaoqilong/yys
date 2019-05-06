# coding:utf-8
import argparse
from yys.utils.device_config import DeviceConfig
from yys.game.lidao_game_operator import LidaoGameOperator

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--p', type=str, default='MI8')
    args = parser.parse_args()
    device_config = DeviceConfig(args.p)
    game_operator = LidaoGameOperator(device_config)
    stop_times = 1000
    current_times = 0
    game_operator.get_phone_picture()
    # game_operator.show_current_crop(None)
