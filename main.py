from utilities import Utilities
from display import Display


if __name__ == "__main__":
    print(Utilities.read_asm_file("src/add_increment_test.asm"))
    z80_display = Display()
    z80_display.run()
