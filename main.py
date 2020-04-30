from helpers.utilities import Utilities
import lexer
from token_parser import parser


if __name__ == "__main__":
    code = Utilities.read_asm_file("src/add_increment_test.asm")
    print("\n----- Stage 1 (Lexer) ----\n")
    tokens = lexer.lexer(code)
    for token in tokens:
        print(token)
    print("\n----- Stage 2 (Parser) ----\n")
    # Parse the token list
    parsed = parser(tokens)
    for parsed_item in parsed:
        print(parsed_item)
