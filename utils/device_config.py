# coding:utf-8
import cv2 as cv
import os
import sys
import yaml
from pathlib import Path

__all__ = ['DeviceConfig']


class DeviceConfig(object):

    def __init__(self, config_name):
        self.config_path = Path('./config/%s.yaml' % config_name)
        with open(self.config_path) as f:
            dictionary = yaml.load(f)
        self.dictionary = dictionary
        self.device_info = dictionary.get('device_info')
        self.picture_info = dictionary.get('picture_info')
        self.operator_config = dictionary.get('operator_config')
