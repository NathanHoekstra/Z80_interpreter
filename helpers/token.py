from helpers.enums import TokenType


class Token(object):
    def __init__(self, token_type: TokenType, value: str, line: int, sub_type: TokenType = None):
        self.token_type = token_type
        self.sub_type = sub_type
        self.value = value
        self.line = line

    def __str__(self):
        return f"Token(Type:{self.token_type}, Sub-type:{self.sub_type} Value:'{self.value}', Line:{self.line})"

    def __repr__(self):
        return self.__str__()