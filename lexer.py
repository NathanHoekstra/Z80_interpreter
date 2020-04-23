from typing import List
import regex


class Token(object):
    def __init__(self, token_type, value, line):
        self.token_type = token_type
        self.value = value
        self.line = line

    def __str__(self):
        return f"Token(Type:{self.token_type}, Value:{self.value}, Line:{self.line})"

    def __repr__(self):
        return self.__str__()


# tokenizer :: str -> int -> Token
def tokenizer(item: str, line_number: int) -> Token:
    # Capitalize items
    item = item.upper()
    # TODO: Tokenize stuff here, change to regex operations
    print(item)
    if item.startswith("#"):
        return Token("DECIMAL", item.split("#")[1], line_number)
    elif item.startswith("$"):
        return Token("HEX", item.split("$")[1], line_number)
    elif item.isdigit():
        return Token("DECIMAL", item, line_number)
    elif item == "A" or item == "B":
        return Token("REGISTER", item, line_number)
    elif item == "A," or item == "B,":
        return Token("REGISTER", item[0], line_number)
    return Token(item, None, line_number)


# lexer :: List[str] -> int -> List[Token]
def lexer(code: List[str], line_num: int = 0) -> List[Token]:
    if len(code) == 0:
        return []
    else:
        head, *tail = code
        result = map(lambda x: tokenizer(x, line_num), head.split())
        line_num += 1
        return list(result) + lexer(tail, line_num)
