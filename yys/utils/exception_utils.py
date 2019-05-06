#!/usr/bin/env python3
# coding:utf-8
import os
from yys.utils import DeviceConfig
__all__=['ExceptionUtils']


class ExceptionUtils(object):

    def __init__(self, device_config: DeviceConfig):
        self.device_config = device_config
        self.operator_config = device_config.operator_config
        self.step_dict = {}
        self.step_threshold_dict = {}
        self.battle_count = 0
        self.empty_loop_count = 0
        self.step_threshold = self.operator_config.get('step_threshold')
        self.empty_loop_threshold = self.operator_config.get('empty_loop_threshold')

    def register_step(self, step_name, reduction_factor=0.2):
        self.step_dict[step_name] = 0
        self.step_threshold_dict[step_name] = self.step_threshold // (reduction_factor * 5)

    def update_step(self, step_name, reduction_factor=0.2):
        self.empty_loop_count = 0
        if step_name not in self.step_dict.keys():
            self.register_step(step_name, reduction_factor)
        self.step_dict[step_name] += 1

    def update_empty_loop(self):
        for key in self.step_dict.keys():
            self.step_dict[key] = 0
        self.empty_loop_count += 1

    def check_exception(self):
        for key in self.step_dict.keys():
            if self.step_dict[key] > self.step_threshold_dict[key]:
                return key
        if self.empty_loop_count > self.empty_loop_threshold:
            return 'empty_loop'
        return None

