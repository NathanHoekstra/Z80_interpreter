from typing import List, Tuple, Union
from lexer import Token
from helpers.rules import parser_rules
from helpers.enums import TokenType


# validate_tokens :: Tuple[TokenType] -> List[Tuple] -> Bool
def validate_tokens(tokens: Tuple[TokenType], rules: List[Tuple]) -> bool:
    # Out of rules to check, so no matching rule was found
    if len(rules) == 0:
        return False
    rule, *tail = rules
    if tokens == rule:  # If a match has been found
        return True
    # No match has been found with the current rule, let's try the next rule
    return validate_tokens(tokens, tail)


# get_tokens :: List[Token] -> int -> List[Token] -> Union[List[Token], [List[TokenType]]
def get_tokens(tokens: List[Token], curr_line: int, just_type: bool = False) -> Union[List[Token], List[TokenType]]:
    # No more tokens to go through, let's exit out of the recursion
    if len(tokens) == 0:
        return []
    head, *tail = tokens
    if head.line == curr_line:  # Is the current token still on the correct line?
        if just_type:  # Do we just want the token type?
            head = head.token_type
        return [head] + get_tokens(tail, curr_line, just_type)
    return []


# parser :: List[Token] -> int -> List[List[Token]]
def parser(token_list: List[Token], current_line: int = 1) -> List[List[Token]]:
    # We went through the token list
    if len(token_list) == 0:
        return []
    curr_types = get_tokens(token_list, current_line, True)
    curr_tokens = get_tokens(token_list, current_line)
    if validate_tokens(tuple(curr_types), parser_rules):
        current_line += 1
        return [curr_tokens] + parser(token_list[len(curr_tokens):], current_line)
    else:
        raise SyntaxError(f"Invalid syntax on line {current_line}: {' '.join(str(x.value) for x in curr_tokens)}")
