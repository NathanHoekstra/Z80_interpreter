from typing import List
import re
from helpers.enums import TokenType
from helpers.rules import regex_rules
from helpers.token import Token


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
        # Use higher order function to tokenize each line (#1)
        result = map(lambda x: tokenizer(x, regex_rules, line_num), head.split())
        line_num += 1
        return list(result) + lexer(tail, line_num)
