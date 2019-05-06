# coding: utf-8
import logging
import time

__all__ = ['LogUtils']


class LogUtils(object):

    def __init__(self, device_config):
        self.device_config = device_config
        self.device_info = device_config.device_info
        self.operator_config = device_config.operator_config
        self.log_type = self.operator_config.get('log_type')
        self.device_id = self.device_info.get('device_id')

    def log(self, step_name, result):
        curr_time = time.asctime(time.localtime(time.time()))
        log_str = curr_time + " " + step_name + " " + str(round(result, 2))
        if self.log_type == 'screen':
            print(log_str)
        elif self.log_type == 'file':
            print(log_str)
            logging.basicConfig(level=logging.INFO,
                                filename='../log/'+ self.device_id + '.log',
                                filemode='a')
            logging.info(log_str)




