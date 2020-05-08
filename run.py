import argparse
import sys
from typing import List, Dict
from helpers.token import Token
from helpers.enums import TokenType
from helpers.opcodes import cpu_opcodes, JP
from helpers.exceptions import ASMSyntaxError, DisplayClosed
from helpers.utilities import Utilities
import lexer
import token_parser
from cpu import Cpu
from display import Display


#
# NOTE: As discussed with Diederik, I won't be making a copy of the CPU class
#


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
def runner(cpu: Cpu, parsed_tokens: List[List[Token]], display: Display = None) -> None:
    # Is the program finished?
    if cpu.register[TokenType.REGISTER_PC] >= len(parsed_tokens):
        print(f"[info] The program has jumped {JP.counter} times\n")
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

    # If the pc_value is not none, set the PC register to that value (happens with jump-like instructions)
    if pc_value:
        cpu.register[TokenType.REGISTER_PC] = pc_value
    # Otherwise up the program counter by one
    else:
        cpu.register[TokenType.REGISTER_PC] += 1

    # Check if a display is supplied
    if display:
        if display.draw(cpu):
            raise DisplayClosed(None, "Display has been closed")

    # call the runner recursively
    return runner(cpu, parsed_tokens, display)


if __name__ == "__main__":
    # Increase recursion limit
    sys.setrecursionlimit(10**6)
    # Parse arguments
    parser = argparse.ArgumentParser(description='GameBoy (Z80) ASM interpreter')
    parser.add_argument('--input', metavar='i', type=str, help='a Z80 assembly file', required=True)
    parser.add_argument('--display', metavar='d', type=bool, default=False, help='Enable display?')
    args = parser.parse_args()
    # Create display variable, set initially to None
    display = None
    # Create CPU object
    z80 = Cpu()
    if args.display:
        display = Display()
    # Execute interpreter
    print(f"[INFO] Parsing the specified asm file: {args.input}")
    parsed = token_parser.parser(lexer.lexer(Utilities.read_asm_file(args.input)))
    print("[INFO] Executing the ASM file...")
    runner(z80, parsed, display)
    # Print out the cpu registers after runner has finished
    print(z80)
    exit(0)  # Close program
