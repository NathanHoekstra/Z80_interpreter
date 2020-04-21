from typing import List


class Token(object):
    def __init__(self, token_type, value, line):
        self.token_type = token_type
        self.value = value
        self.line = line

    def __str__(self):
        return f"Token(Type:{self.token_type}, Value:{self.value}, Line:{self.line})"

    def __repr__(self):
        return self.__str__()


def tokenizer(item: str, line_number: int) -> Token:
    # TODO: Tokenize stuff here
    return Token(item, None, line_number)


# lexer :: List[str] -> int -> List[Token]
def lexer(code: List[str], line_num: int = 0) -> List[Token]:
    if len(code) == 0:
        return []
    else:
        head, *tail = code
        result = list(map(lambda x: tokenizer(x, line_num), head.split()))
        line_num += 1
        return result + lexer(tail, line_num)
