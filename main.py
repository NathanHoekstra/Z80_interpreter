from utilities import Utilities
from display import Display
from cpu import Cpu
import lexer


if __name__ == "__main__":
    code = Utilities.read_asm_file("src/add_increment_test.asm")
    tokens = lexer.lexer(code)
    for token in tokens:
        print(token)
