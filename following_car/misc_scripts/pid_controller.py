# -*- coding: utf-8 -*-

"""
    Based on Arduino PID Library (Version 1.0.1) by Brett Beauregard <br3ttb@gmail.com> brettbeauregard.com
"""

import datetime
import sys

class PID(object):
    def __init__(self, input, output, setpoint, kp, ki, kd, direct):
        self._output = output
        self._input = input
        self._setpoint = setpoint

        self._kp = 0
        self._ki = 0
        self._kd = 0
        self._disp_kp = 0
        self._disp_ki = 0
        self._disp_kd = 0
        self._i_term = None
        self._auto = False
        self._direct = None
        self._sample_time = 100
        self._sample_timedelta = None
        self._output_value = None
        self._last_input = None
        self._out_min = -sys.maxsize - 1
        self._out_max = sys.maxsize

        self.set_output_limits(0, 255)
        self.sample_time = 100  # milliseconds
        self.direct = direct
        self.set_tunings(kp, ki, kd)
        self.last_time = datetime.datetime.now() - self._sample_timedelta


    def initialize(self):
        self._i_term = self.output_value
        self._last_input = self._input()
        if self._i_term > self._out_max:
            self._i_term = self._out_max
        elif self._i_term < self._out_min:
            self._i_term = self._out_min


    def compute(self):
        if not self.auto:
            return False
        now = datetime.datetime.now()
        time_change = now - self.last_time

        if time_change < self._sample_timedelta:
            return False

        input_value = self._input()
        error = self.setpoint - input_value
        self._i_term += self._ki * error
        if self._i_term > self._out_max:
            self._i_term = self._out_max
        elif self._i_term < self._out_min:
            self._i_term = self._out_min

        delta_input = input_value - self._last_input
        output = self._kp * error + self._i_term - self._kd * delta_input

        if output > self._out_max:
            output = self._out_max
        elif output < self._out_min:
            output = self._out_min

        self.output_value = output

        self._last_input = input_value
        self.last_time = now
        return True

    @property
    def output_value(self):
        return self._output_value

    @output_value.setter
    def output_value(self, value):
        self._output_value = value
        self._output(value)

    def set_tunings(self, kp, ki, kd):
        if kp < 0 or ki < 0 or kd < 0:
            return

        self._disp_kp = kp
        self._disp_ki = ki
        self._disp_kd = kd

        sample_time_in_sec = self.sample_time / 1000.0
        self._kp = kp
        self._ki = ki * sample_time_in_sec
        self._kd = kd * sample_time_in_sec

        if not self.direct:
            self._kp = 0 - self._kp
            self._ki = 0 - self._ki
            self._kd = 0 - self._kd

    @property
    def setpoint(self):
        return self._setpoint

    @setpoint.setter
    def setpoint(self, value):
        self._setpoint = value

    @property
    def sample_time(self):
        return self._sample_time

    @sample_time.setter
    def sample_time(self, new_sample_time):
        if new_sample_time <= 0:
            return

        ratio = new_sample_time / float(self._sample_time)
        self._ki *= ratio
        self._kd /= ratio
        self._sample_time = new_sample_time
        self._sample_timedelta = datetime.timedelta(milliseconds=new_sample_time)

    def set_output_limits(self, out_min, out_max):
        if out_min >= out_max:
            return
        self._out_min = out_min
        self._out_max = out_max

        if not self.auto:
            return

        if self.output_value > self._out_max:
            self.output_value = self._out_max
        elif self.output_value < self._out_min:
            self.output_value = self._out_min

        if self._i_term > self._out_max:
            self._i_term = self._out_max
        elif self._i_term < self._out_min:
            self._i_term = self._out_min

    @property
    def auto(self):
        return self._auto

    @auto.setter
    def auto(self, new_auto):
        if new_auto != self._auto:
            self.initialize()
        self._auto = new_auto

    @property
    def direct(self):
        return self._direct

    @direct.setter
    def direct(self, value):
        if self.auto and value != self._direct:
            self._kp = 0 - self._kp
            self._ki = 0 - self._ki
            self._kd = 0 - self._kd
        self._direct = value

    @property
    def kp(self):
        return self._disp_kp

    @property
    def ki(self):
        return self._disp_ki

    @property
    def kd(self):
        return self._disp_kd
