#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Parrot(object):
    BASE_SPEED = 12

    def speed(self):
        return self.BASE_SPEED


class EuropeanParrot(Parrot):
    pass


class AfricanParrot(Parrot):
    LOAD_FACTOR = 9

    def __init__(self, number_of_coconuts):
        super(AfricanParrot, self).__init__()
        self._number_of_coconuts = number_of_coconuts

    def speed(self):
        return max(0, self.BASE_SPEED - self.LOAD_FACTOR * self._number_of_coconuts)


class NorwegianParrot(Parrot):
    MAX_SPEED = 24

    def __init__(self, voltage, nailed):
        super(NorwegianParrot, self).__init__()
        self._voltage = voltage
        self._nailed = nailed

    def speed(self):
        return (self._compute_speed_for_voltage() if not self._nailed else 0)

    def _compute_speed_for_voltage(self):
        return min([self.MAX_SPEED, self._voltage * self.BASE_SPEED])
