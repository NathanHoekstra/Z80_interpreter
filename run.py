from typing import List, Dict
from helpers.token import Token
from helpers.enums import TokenType
from helpers.opcodes import cpu_opcodes
from helpers.exceptions import ASMSyntaxError
from cpu import Cpu


# search_labels :: List[List[Token]] -> Dict -> Dict
def search_labels(parsed_tokens: List[List[Token]], result: Dict = None) -> Dict:
    # If the dict is not initialized, initialize it
    if result is None:
        result = {}

    # Did we went through the whole token list yet?
    if len(parsed_tokens) == 0:
        return result

    # Unpack the first item in the list as the head
    head, *tail = parsed_tokens

    # If the line marks the start of a labeled section, add it to the dict
    if len(head) == 1 and head[0].token_type == TokenType.LABEL:
        label = head[0].value.split(":")[0]
        result[label] = head[0].line

    # Recursively search for more labels through the token list
    return search_labels(tail, result)


# runner :: Cpu -> List[List[Token]] -> None
def runner(cpu: Cpu, parsed_tokens: List[List[Token]]) -> None:
    # Is the program finished?
    if cpu.register[TokenType.REGISTER_PC] >= len(parsed_tokens) - 1:
        return

    # Are the labels found yet?
    if cpu.labels is None:
        cpu.labels = search_labels(parsed_tokens)

    # Unpack current line
    opcode, *params = parsed_tokens[cpu.register[TokenType.REGISTER_PC]]

    # Check if the to be executed line isn't an invalid line
    if opcode.token_type == TokenType.INVALID:
        raise ASMSyntaxError(opcode.line, f"Invalid syntax: {opcode.value}")

    # Execute current line
    pc_value = cpu_opcodes[opcode.token_type](cpu, *params)

    # If the pc_value is not none, set the PC register to that value (happens with JP instruction)
    if pc_value:
        cpu.register[TokenType.REGISTER_PC] = pc_value
    # Otherwise up the program counter by one
    else:
        cpu.register[TokenType.REGISTER_PC] += 1

    # call the runner recursively
    return runner(cpu, parsed_tokens)
