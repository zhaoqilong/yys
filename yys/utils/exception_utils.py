# coding: uft-8

class ExceptionUtils(object):

    def __init__(self, device_config):
        self.device_config = device_config
        self.operator_config = device_config.get('operator_config')
        self.step_dict = {}
        self.step_threshold_dict = {}
        self.battle_count = 0
        self.empty_loop_count = 0

        self.step_threshold = self.operator_config.get('step_threshold')
        self.empty_loop_threshold = self.operator_config.get('empty_loop_threshold')

    def register_step(self, step_name, reduction_factor = 1):
        self.step_dict[step_name] = 0
        self.step_threshold_dict[step_name] = step_name // (reduction_factor * 5)

    def update_step(self, step_name):
        if step_name not in self.step_dict.keys():
            self.register_step(step_name)
        self.step_dict[step_name] += 1


    def update_total(self):
        self.battle_count += 1

    def update_empty_loop(self):
        self.empty_loop_count += 1

