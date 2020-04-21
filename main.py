from utilities import Utilities
from display import Display
from cpu import Cpu


if __name__ == "__main__":
    print(Utilities.read_asm_file("src/add_increment_test.asm"))
    CPU = Cpu()
    print(CPU)
