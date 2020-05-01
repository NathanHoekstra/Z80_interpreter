import numpy as np


class Cpu(object):
    def __init__(self):
        # Z80's memory size is 64KB
        self.memory = [np.uint8(0)] * 0xFFFF
        # Registers
        self.a = np.uint8(0x00)
        self.b = np.uint8(0x00)
        self.sp = np.uint16(0xFFFE)
        self.pc = np.uint16(0x00)

    def __str__(self):
        return f"Register A:        [{hex(self.a)}]\n" + \
               f"Register B:        [{hex(self.b)}]\n" + \
               f"Stack Pointer:     [{hex(self.sp)}]\n" + \
               f"Program Counter:   [{hex(self.pc)}]\n"

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    cpu = Cpu()
    print(cpu)
