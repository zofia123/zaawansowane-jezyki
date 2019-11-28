#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Parrot(object):

    LOAD_FACTOR = 9
    BASE_SPEED = 12
    MAX_SPEED = 24 

    def __init__(self, number_of_coconuts, voltage, nailed):
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed

    def speed(self):
        raise NotImplementedError


class EuropeanParrot(Parrot):

    def __init__(self):
        super(EuropeanParrot, self).__init__(None, None, None)

    def speed(self):
        return self._european_speed()

    def _european_speed(self):
        return self.BASE_SPEED


class AfricanParrot(Parrot):

    def __init__(self, number_of_coconuts):
        super(AfricanParrot, self).__init__(number_of_coconuts, None, None)

    def speed(self):
        return self._african_speed()

    def _african_speed(self):
        return max(0, self.BASE_SPEED - self.LOAD_FACTOR * self._number_of_coconuts)


class NorwegianParrot(Parrot):

    def __init__(self, voltage, nailed):
        super(NorwegianParrot, self).__init__(None, voltage, nailed)

    def speed(self):
        return self._norwegian_speed()

    def _norwegian_speed(self):
        if self._nailed:
            return 0
        else:
            return self._compute_base_speed_for_voltage(self._voltage)

    def _compute_base_speed_for_voltage(self, voltage):
        return min([self.MAX_SPEED, voltage * self.BASE_SPEED])
