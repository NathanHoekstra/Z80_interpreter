from typing import List
from helpers.enums import TokenType
import re
from helpers.rules import regex_rules


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


# tokenizer :: str -> int -> Token
def tokenizer(item: str, rules: List, line_number: int) -> Token:
    if len(rules) == 0:
        # We went through the rules and didn't find a match
        return Token(TokenType.UNKNOWN, item, line_number)
    else:
        head, *tail = rules
        rule, *token_type = head
        match = re.match(rule, item)

        # No match has been found, let's try the next rule
        if not match:
            return tokenizer(item, tail, line_number)

        # A match has been found so let's return the token
        if len(token_type) == 1:  # Token type has no subtype
            return Token(token_type[0], item, line_number)
        else:  # This token has a sub-type so let's set it
            return Token(token_type[0], item, line_number, token_type[1])


# lexer :: List[str] -> int -> List[Token]
def lexer(code: List[str], line_num: int = 0) -> List[Token]:
    if len(code) == 0:
        return []
    else:
        head, *tail = code
        result = map(lambda x: tokenizer(x, regex_rules, line_num), head.split())
        line_num += 1
        return list(result) + lexer(tail, line_num)
