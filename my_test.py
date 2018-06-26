#coding:utf-8
import argparse


def a():
    print(constant.device_id)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--phone', type=str, default=None)
    args = parser.parse_args()
    global constant
    constant = __import__('Constant_' + args.phone)
    print(constant.device_id)
    a()