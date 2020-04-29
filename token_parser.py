from typing import List
from lexer import Token
from helpers.rules import parser_rules
from helpers.enums import TokenType as tt


def check_rules(token: Token, token_index: int, rules: List) -> bool:
    # Out of rules to check, so no matching rule was found
    if len(rules) == 0:
        return False
    head, *tail = rules
    # If a matching rule was found
    t_type = token.token_type
    if t_type == tt.DECIMAL or t_type == tt.HEXADECIMAL or t_type == tt.BINARY:
        t_type = tt.VALUE
    try:
        if head[token_index] == t_type:
            return True
    # Try the next item
    except IndexError:
        return check_rules(token, token_index, tail)
    # otherwise look at the next item in the rule list
    return check_rules(token, token_index, tail)


# parser :: List[Token] -> int -> List[List[Token]]
def parser(token_list: List[Token], i_index: int = 0, current_line: int = 0, new_list: List = None) -> List[List[Token]]:
    if new_list is None:
        new_list = []
    # We went through the token list
    if len(token_list) == 0:
        return new_list
    head, *tail = token_list
    # check if this is the first iteration
    if current_line == 0:
        current_line = head.line
    # if the current line is not equal to the current token line, so next line
    elif current_line != head.line:
        # set the current line to the new line
        current_line = head.line
        # reset the item index
        i_index = 0
    if check_rules(head, i_index, parser_rules):
        if i_index == 0:
            new_list.append([head])
        else:
            new_list[current_line - 1].append(head)
        i_index += 1
        return parser(tail, i_index, current_line, new_list)
    else:
        raise ValueError(f"The token: {head} on line: {current_line} is invalid")
