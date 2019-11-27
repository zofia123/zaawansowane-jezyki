from enum import Enum  


class ParrotType(Enum):  
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3
 
class Parrot:

    LOAD_FACTOR = 9
    BASE_SPEED = 12
    MAX_SPEED = 24 

    def __init__(self, type_of_parrot, number_of_coconuts, voltage, nailed):
        self._type = type_of_parrot
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed

    def speed(self):
        if self._type == ParrotType.EUROPEAN:
            return self._european_speed()
        if self._type == ParrotType.AFRICAN:
            return self._african_speed()
        if self._type == ParrotType.NORWEGIAN_BLUE:
            return self._norwegian_speed()

        raise ValueError("should be unreachable")

    def _compute_base_speed_for_voltage(self, voltage):
        return min([self.MAX_SPEED, voltage * self.BASE_SPEED])

    def _african_speed(self):
        return max(0, self.BASE_SPEED - self.LOAD_FACTOR * self._number_of_coconuts)

    def _norwegian_speed(self):
        if self._nailed:
            return 0
        else:
            return self._compute_base_speed_for_voltage(self._voltage)

    def _european_speed(self):
        return self.BASE_SPEED
