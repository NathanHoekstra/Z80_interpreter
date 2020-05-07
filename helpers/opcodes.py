import numpy as np
import time
from typing import Union
from helpers.decorators import count
from helpers.token import TokenType as tt
from helpers.token import Token
from helpers.exceptions import ASMLabelError
from cpu import Cpu


# get_value :: Token -> Union[uint8, uint16]
def get_value(token: Token) -> Union[np.uint8, np.uint16]:
    if not token.token_type == tt.VALUE:
        raise ValueError(f"Wrong token type input specified, "
                         f"expected {tt.VALUE.name} received {token.token_type.name}")
    # Check what the subtype is
    if token.sub_type == tt.HEXADECIMAL:
        # let's strip the $ from the value and add trailing 0x
        value = int("0x" + token.value.strip("$"), 0)
        if value > 255:  # Check if the value is 16-bit
            return np.uint16(value)
        return np.uint8(value)
    elif token.sub_type == tt.DECIMAL:
        # let's strip the # from the value and return it
        value = int(token.value.strip("#"))
        if value > 255:  # Check if the value is 16-bit
            return np.uint16(value)
        return np.uint8(value)
    elif token.sub_type == tt.BINARY:
        # let's strip the % from the value
        value = token.value.strip("%")
        return np.uint8(int(value, 2))
    # The token value has an unknown subtype
    else:
        raise ValueError(f"The token {tt.VALUE.name} has an unknown subtype: {token.sub_type.name}")


# get_direct_value -> Cpu -> Token -> uint16
def get_direct_value(cpu: Cpu, token: Token) -> np.uint16:
    # Check if specified token is actually a direct token
    if not token.token_type == tt.DIRECT:
        raise ValueError(f"Wrong token type input specified, "
                         f"expected {tt.DIRECT.name} received {token.token_type.name}")
    # Check if the subtype is of type hex
    if token.sub_type == tt.HEXADECIMAL:
        value = "0x" + token.value.strip("[]$,")
        return np.uint16(int(value, 0))
    # Otherwise the subtype is a register
    return cpu.register[token.sub_type]


# check_condition :: Cpu -> Token -> Bool
def check_condition(cpu: Cpu, token: Token) -> bool:
    if not token:  # Token can possibly be None
        return False
    elif token.token_type == tt.CONDITION_NZ and not cpu.flags["Z"] or \
            token.token_type == tt.CONDITION_Z and cpu.flags["Z"] or \
            token.token_type == tt.CONDITION_NC and not cpu.flags["C"] or \
            token.token_type == tt.CONDITION_C and cpu.flags["C"]:
        return True
    else:
        return False

#                                       #
#   ---- Opcode implementations ----    #
#                                       #


# ADC :: Cpu -> Token -> Token -> None
def ADC(cpu: Cpu, token1: Token, token2: Token) -> None:
    raise NotImplementedError()


# ADD :: Cpu -> Token -> Token -> None
def ADD(cpu: Cpu, token1: Token, token2: Token) -> None:
    # TODO: Set flags
    # If token 2 is of type value
    if token2.token_type == tt.VALUE:
        # Add the value of token 2 to the register specified inside token 1
        cpu.register[token1.token_type] += get_value(token2)
    # otherwise it must be another register
    else:
        cpu.register[token1.token_type] += cpu.register[token2.token_type]
    return


# AND :: Cpu -> Token -> None
def AND(cpu: Cpu, token1: Token) -> None:
    # Check if the token is of type value
    if token1.token_type == tt.VALUE:
        cpu.register[tt.REGISTER_A] &= get_value(token1)
    # Otherwise it must be a register
    else:
        cpu.register[tt.REGISTER_A] &= cpu.register[token1.token_type]
    # Setup flags
    if cpu.register[tt.REGISTER_A] == 0:
        cpu.flags["Z"] = True
    cpu.flags["N"] = False
    cpu.flags["H"] = True
    cpu.flags["C"] = False
    return


# BIT :: Cpu -> Token -> Token -> None
def BIT(cpu: Cpu, token1: Token, token2: Token) -> None:
    bit = int(token1.value.strip(','))
    # If the bit is not set
    if not cpu.register[token2.token_type] & (1 << bit):
        cpu.flags["Z"] = True
    cpu.flags["N"] = False
    cpu.flags["H"] = True
    return


# CALL :: Cpu -> Token -> Token -> Union[None, uint16]
def CALL(cpu: Cpu, token1: Token, token2: Token = None) -> Union[None, np.uint16]:
    # Check if token 1 is of type label or a condition is met
    if token1.token_type == tt.LABEL or check_condition(cpu, token1):
        next_instruction = token1.line
        # Lower the stack pointer
        cpu.register[tt.REGISTER_SP] -= 1  # Decrement by two because a label is supposed to be 16 bit
        # Push the address of the next instruction onto the stack
        cpu.memory[cpu.register[tt.REGISTER_SP]] = next_instruction
        cpu.register[tt.REGISTER_SP] -= 1  # Decrement again because a label is supposed to be 16 bit
        # Jump to the address
        if token1.token_type == tt.LABEL:
            return JP(cpu, token1)
        else:
            return JP(cpu, token2)
    return None


# CCF :: Cpu -> None
def CCF(cpu: Cpu) -> None:
    raise NotImplementedError()


# CP :: Cpu -> Token -> None
def CP(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


# CPL :: Cpu -> None
def CPL(cpu: Cpu) -> None:
    raise NotImplementedError()


# DAA :: Cpu -> None
def DAA(cpu: Cpu) -> None:
    raise NotImplementedError()


# DEC :: Cpu -> Token -> None
def DEC(cpu: Cpu, token1: Token) -> None:
    # Check if the register isn't already at 0
    if not cpu.register[token1.token_type] == 0:
        cpu.register[token1.token_type] -= 1
        # Set the subtract flag since a subtraction was performed
        cpu.flags["N"] = True
    # Set the zero flag to true since the register value is now zero
    if cpu.register[token1.token_type] == 0:
        cpu.flags["Z"] = True
    return


# DI :: Cpu -> None
def DI(cpu: Cpu) -> None:
    raise NotImplementedError()


# EI :: Cpu -> None
def EI(cpu: Cpu) -> None:
    raise NotImplementedError()


# HALT :: Cpu -> None
def HALT(cpu: Cpu) -> None:
    # TODO: Halt now does a sleep of 1 second, normally waits for an interrupt
    time.sleep(1)
    return


# INC :: Cpu -> Token -> None
def INC(cpu: Cpu, token1: Token) -> None:
    # TODO: Set H flag
    cpu.register[token1.token_type] += 1
    # Reset the the subtract flag since a increment was performed
    cpu.flags["N"] = False
    return


# JP :: Cpu -> Token -> Token -> Union[None, uint16]
@count
def JP(cpu: Cpu, token1: Token, token2: Token = None) -> Union[None, np.uint16]:
    # If the token 1 is of type label, jump straight away
    if token1.token_type == tt.LABEL:
        # Check if the label exists
        if token1.value in cpu.labels:
            return cpu.labels[token1.value] - 1  # Remove one since it is a line number not an index
        else:
            raise ASMLabelError(token1.line, f"The label {token1.value} was not found")
    # token 1 is not a label, so it must be a conditional jump
    else:
        if check_condition(cpu, token1):
            # Check if the label exists
            if token2.value in cpu.labels:
                return cpu.labels[token2.value] - 1  # Remove one since it is a line number not an index
            else:
                raise ASMLabelError(token2.line, f"The label '{token2.value}' was not found")
    return None


# JR :: Cpu -> Token -> Token -> Union[None, uint16]
def JR(cpu: Cpu, token1: Token, token2: Token = None) -> Union[None, np.uint16]:
    # Check if token 1 is of type value or a condition is met
    if token1.token_type == tt.VALUE or check_condition(cpu, token1):
        curr_address = cpu.register[tt.REGISTER_SP]
        # If token 2 is none, it is a unconditional JR instruction
        if token2 is None:
            return curr_address + get_value(token1)
        # It is a conditional JR instruction so let's take the value from token 2
        else:
            return curr_address + get_value(token2)
    return None


# LD :: Cpu -> Token -> Token -> None
def LD(cpu: Cpu, token1: Token, token2: Token) -> None:
    # Check if the second token is of type value
    if token2.token_type == tt.VALUE:
        # Check if the first token is of type direct
        if token1.token_type == tt.DIRECT:
            cpu.memory[get_direct_value(cpu, token1)] = get_value(token2)
            return
        # Otherwise it must be a register
        cpu.register[token1.token_type] = get_value(token2)
    # Check if the second token is of type direct
    elif token2.token_type == tt.DIRECT:
        cpu.register[token1.token_type] = cpu.memory[get_direct_value(cpu, token2)]
        return
    # Otherwise it must be register
    else:
        # Check if the first token is of type direct
        if token1.token_type == tt.DIRECT:
            cpu.memory[get_direct_value(cpu, token1)] = cpu.register[token2.token_type]
            return
        # Otherwise it must be register to register operations
        cpu.register[token1.token_type] = cpu.register[token2.token_type]
    return


# LDD :: Cpu -> Token -> Token -> None
def LDD(cpu: Cpu, token1: Token, token2: Token) -> None:
    raise NotImplementedError()


# LDH :: Cpu -> Token -> Token -> None
def LDH(cpu: Cpu, token1: Token, token2: Token) -> None:
    raise NotImplementedError()


# LDI :: Cpu -> Token -> Token -> None
def LDI(cpu: Cpu, token1: Token, token2: Token) -> None:
    raise NotImplementedError()


# NOP :: Cpu -> None
def NOP(cpu: Cpu) -> None:
    # Do nothing
    return


# OR :: Cpu -> Token -> None
def OR(cpu: Cpu, token1: Token) -> None:
    # Check if the token is of type value
    if token1.token_type == tt.VALUE:
        cpu.register[tt.REGISTER_A] |= get_value(token1)
    # Otherwise it must be a register
    else:
        cpu.register[tt.REGISTER_A] |= cpu.register[token1.token_type]
    # Setup flags
    if cpu.register[tt.REGISTER_A] == 0:
        cpu.flags["Z"] = True
    cpu.flags["N"] = False
    cpu.flags["H"] = False
    cpu.flags["C"] = False
    return


# POP :: Cpu -> Token -> None
def POP(cpu: Cpu, token1: Token) -> None:
    # Check if the stack pointer isn't already at it's 'origin'
    if cpu.register[tt.REGISTER_SP] == 0xFFFE:
        return None
    first_byte = cpu.memory[cpu.register[tt.REGISTER_SP]]
    cpu.register[tt.REGISTER_SP] += 1
    second_byte = cpu.memory[cpu.register[tt.REGISTER_SP]]
    cpu.register[tt.REGISTER_SP] += 1
    cpu.register[token1.token_type] = (np.uint16(first_byte) << 8) | second_byte
    return


# PUSH :: Cpu -> Token -> None
def PUSH(cpu: Cpu, token1: Token) -> None:
    cpu.register[tt.REGISTER_SP] -= 1
    cpu.memory[cpu.register[tt.REGISTER_SP]] = cpu.register[token1.token_type] & 0xFF
    cpu.register[tt.REGISTER_SP] -= 1
    cpu.memory[cpu.register[tt.REGISTER_SP]] = (cpu.register[token1.token_type] >> 8)
    return


# RES :: Cpu -> Token -> Token -> None
def RES(cpu: Cpu, token1: Token, token2: Token) -> None:
    bit = int(token1.value.strip(','))
    cpu.register[token2.token_type] &= ~(1 << bit)
    return


# RET :: Cpu -> Token -> Union[None, uint16]
def RET(cpu: Cpu, token1: Token = None) -> Union[None, np.uint16]:
    # Check if the stack pointer isn't already at it's 'origin'
    if cpu.register[tt.REGISTER_SP] == 0xFFFE:
        return None
    # Check if the token is None or if an condition is met
    if token1 is None or check_condition(cpu, token1):
        cpu.register[tt.REGISTER_SP] += 1
        # Get the return address from the stack and point the SP one higher
        address = cpu.memory[cpu.register[tt.REGISTER_SP]]
        cpu.register[tt.REGISTER_SP] += 1  # Increment again because a label is supposed to be 16 bit
        return address
    return None


# RETI :: Cpu -> None
def RETI(cpu: Cpu) -> None:
    raise NotImplementedError()


# RL :: Cpu -> Token -> None
def RL(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


# RLA :: Cpu -> None
def RLA(cpu: Cpu) -> None:
    raise NotImplementedError()


# RLC :: Cpu -> Token -> None
def RLC(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


# RLCA :: Cpu -> None
def RLCA(cpu: Cpu) -> None:
    raise NotImplementedError()


# RR :: Cpu -> Token -> None
def RR(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


# RRA :: Cpu -> None
def RRA(cpu: Cpu) -> None:
    raise NotImplementedError()


# RRC :: Cpu -> Token -> None
def RRC(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


# RRCA :: Cpu -> None
def RRCA(cpu: Cpu) -> None:
    raise NotImplementedError()


# RST :: Cpu -> Token -> None
def RST(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


# SBC :: Cpu -> Token -> Token -> None
def SBC(cpu: Cpu, token1: Token, token2: Token) -> None:
    raise NotImplementedError()


# SCF :: Cpu -> None
def SCF(cpu: Cpu) -> None:
    raise NotImplementedError()


# SET :: Cpu -> Token -> Token -> None
def SET(cpu: Cpu, token1: Token, token2: Token) -> None:
    bit = int(token1.value.strip(','))
    cpu.register[token2.token_type] |= 1 << bit
    return


# SLA :: Cpu -> Token -> None
def SLA(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


# SRA :: Cpu -> Token -> None
def SRA(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


# SRL :: Cpu -> Token -> None
def SRL(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


# STOP :: Cpu -> Token -> None
def STOP(cpu: Cpu) -> None:
    raise NotImplementedError()


# SUB :: Cpu -> Token -> None
def SUB(cpu: Cpu, token1: Token) -> None:
    # check if the token is of type value
    if token1.token_type == tt.VALUE:
        cpu.register[tt.REGISTER_A] -= get_value(token1)
    # Otherwise it must be an register
    else:
        cpu.register[tt.REGISTER_A] -= cpu.register[token1.token_type]
    # Set flags
    if cpu.register[tt.REGISTER_A] <= 0:
        cpu.register[tt.REGISTER_A] = 0  # Make sure that the register isn't a negative value
        cpu.flags["Z"] = True
    cpu.flags["N"] = True
    return


# SWAP :: Cpu -> Token -> None
def SWAP(cpu: Cpu, token1: Token) -> None:
    register_value = cpu.register[token1.token_type]
    result = ((register_value & 0x0F) << 4 | (register_value & 0xF0) >> 4)
    # Set flags
    if result <= 0:
        result = 0
        cpu.flags["Z"] = True
    cpu.flags["N"] = False
    cpu.flags["H"] = False
    cpu.flags["C"] = False
    cpu.register[token1.token_type] = result
    return


# XOR :: Cpu -> Token -> None
def XOR(cpu: Cpu, token1: Token) -> None:
    # Check if the token is of type value
    if token1.token_type == tt.VALUE:
        cpu.register[tt.REGISTER_A] ^= get_value(token1)
    # Otherwise it must be a register
    else:
        cpu.register[tt.REGISTER_A] ^= cpu.register[token1.token_type]
    # Setup flags
    if cpu.register[tt.REGISTER_A] == 0:
        cpu.flags["Z"] = True
    cpu.flags["N"] = False
    cpu.flags["H"] = False
    cpu.flags["C"] = False
    return


cpu_opcodes = {
    tt.ADC: ADC,
    tt.ADD: ADD,
    tt.AND: AND,
    tt.BIT: BIT,
    tt.CALL: CALL,
    tt.CCF: CCF,
    tt.CPL: CPL,
    tt.CP: CP,
    tt.DAA: DAA,
    tt.DEC: DEC,
    tt.DI: DI,
    tt.EI: EI,
    tt.HALT: HALT,
    tt.INC: INC,
    tt.JP: JP,
    tt.JR: JR,
    tt.LDD: LDD,
    tt.LDH: LDH,
    tt.LDI: LDI,
    tt.LD: LD,
    tt.NOP: NOP,
    tt.OR: OR,
    tt.POP: POP,
    tt.PUSH: PUSH,
    tt.RES: RES,
    tt.RETI: RETI,
    tt.RET: RET,
    tt.RLCA: RLCA,
    tt.RLA: RLA,
    tt.RLC: RLC,
    tt.RL: RL,
    tt.RRCA: RRCA,
    tt.RRA: RRA,
    tt.RRC: RRC,
    tt.RR: RR,
    tt.RST: RST,
    tt.SBC: SBC,
    tt.SCF: SCF,
    tt.SET: SET,
    tt.SLA: SLA,
    tt.SRA: SRA,
    tt.SRL: SRL,
    tt.STOP: STOP,
    tt.SUB: SUB,
    tt.SWAP: SWAP,
    tt.XOR: XOR,
    tt.LABEL: NOP
}
