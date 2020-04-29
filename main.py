from helpers.utilities import Utilities
import lexer
import parser


if __name__ == "__main__":
    code = Utilities.read_asm_file("src/add_increment_test.asm")
    tokens = lexer.lexer(code)
    for token in tokens:
        print(token)
    # Parse the token list
    parsed = parser.parser(tokens)
    print(parsed)
