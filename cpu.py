import numpy as np
from helpers.token import TokenType as tt


class Cpu(object):
    def __init__(self):
        self.labels = None
        # Z80's memory size is 64KB
        self.memory = [np.uint8(0)] * 0xFFFF
        # Registers
        self.register = {
            tt.REGISTER_A: np.uint8(0x00),
            tt.REGISTER_B: np.uint8(0x00),
            tt.REGISTER_C: np.uint8(0x00),
            tt.REGISTER_D: np.uint8(0x00),
            tt.REGISTER_E: np.uint8(0x00),
            tt.REGISTER_F: np.uint8(0x00),
            tt.REGISTER_H: np.uint8(0x00),
            tt.REGISTER_L: np.uint8(0x00),
            tt.REGISTER_AF: np.uint16(0x00),
            tt.REGISTER_BC: np.uint16(0x00),
            tt.REGISTER_DE: np.uint16(0x00),
            tt.REGISTER_HL: np.uint16(0x00),
            tt.REGISTER_SP: np.uint16(0xFFFE),
            tt.REGISTER_PC: np.uint16(0x00)
        }
        self.flags = {
            "Z": False,
            "N": False,
            "H": False,
            "C": False
        }

    def __str__(self):
        return '----- Registers -----\n' +\
               '\n'.join(str(k.name) + "\t" + hex(v) for k, v in self.register.items()) +\
               '\n----- Flags -----\n' +\
               '\n'.join(str(k) + "\t" + str(v) for k, v in self.flags.items())

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    cpu = Cpu()
    print(cpu)
