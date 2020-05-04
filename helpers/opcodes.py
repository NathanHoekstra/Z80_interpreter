import numpy as np
from typing import Union
from helpers.decorators import count
from helpers.token import TokenType as tt
from helpers.token import Token
from helpers.exceptions import ASMLabelError
from cpu import Cpu


# get_value :: Token -> uint8
def get_value(token: Token) -> np.uint8:
    if not token.token_type == tt.VALUE:
        raise ValueError(f"Wrong token type input specified, "
                         f"expected {tt.VALUE.name} received {token.token_type.name}")
    # Check what the subtype is
    if token.sub_type == tt.HEXADECIMAL:
        # let's strip the $ from the value and return it
        value = token.value.strip("$")
        return np.uint8(int(value, 16))
    elif token.sub_type == tt.DECIMAL:
        # let's strip the # from the value and return it
        return np.uint8(token.value.strip("#"))
    elif token.sub_type == tt.BINARY:
        # let's strip the % from the value
        value = token.value.strip("%")
        return np.uint8(int(value, 2))
    # The token value has an unknown subtype
    else:
        raise ValueError(f"The token {tt.VALUE.name} has an unknown subtype: {token.sub_type.name}")

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


# AND :: Cpu -> Token -> None
def AND(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


# BIT :: Cpu -> Token -> Token -> None
def BIT(cpu: Cpu, token1: Token, token2: Token) -> None:
    raise NotImplementedError()


# CALL :: Cpu -> Token -> Token -> None
def CALL(cpu: Cpu, token1: Token, token2: Token = None) -> None:
    raise NotImplementedError()


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


# DI :: Cpu -> None
def DI(cpu: Cpu) -> None:
    raise NotImplementedError()


# EI :: Cpu -> None
def EI(cpu: Cpu) -> None:
    raise NotImplementedError()


# HALT :: Cpu -> None
def HALT(cpu: Cpu) -> None:
    raise NotImplementedError()


# INC :: Cpu -> Token -> None
def INC(cpu: Cpu, token1: Token) -> None:
    # TODO: Set flags
    cpu.register[token1.token_type] += 1
    # Reset the the subtract flag since a increment was performed
    cpu.flags["N"] = False


# JP :: Cpu -> Token -> Token -> Union[None, uint8]
@count
def JP(cpu: Cpu, token1: Token, token2: Token = None) -> Union[None, np.uint8]:
    # If the token 1 is of type label, jump straight away
    if token1.token_type == tt.LABEL:
        # Check if the label exists
        if token1.value in cpu.labels:
            return cpu.labels[token1.value] - 1  # Remove one since it is a line number not an index
        else:
            raise ASMLabelError(token1.line, f"The label {token1.value} was not found")
    # token 1 is not a label, so it must be a conditional jump
    else:
        if token1.token_type == tt.CONDITION_NZ and not cpu.flags["Z"] or \
                token1.token_type == tt.CONDITION_Z and cpu.flags["Z"] or \
                token1.token_type == tt.CONDITION_NC and not cpu.flags["C"] or \
                token1.token_type == tt.CONDITION_C and cpu.flags["C"]:
            # Check if the label exists
            if token2.value in cpu.labels:
                return cpu.labels[token2.value] - 1  # Remove one since it is a line number not an index
            else:
                raise ASMLabelError(token2.line, f"The label '{token2.value}' was not found")
    return None


# JR :: Cpu -> Token -> Token -> None
def JR(cpu: Cpu, token1: Token, token2: Token = None) -> None:
    raise NotImplementedError()


# LD :: Cpu -> Token -> Token -> None
def LD(cpu: Cpu, token1: Token, token2: Token) -> None:
    # Check if the second parameter input is of type value
    if token2.token_type == tt.VALUE:
        # Set the register specified in token 1 to the value of token 2
        cpu.register[token1.token_type] = get_value(token2)
    # Otherwise the second parameter must be a register
    else:
        # Set the value of the register specified in token 1 to be the value of the register specified in token 2
        cpu.register[token1.token_type] = cpu.register[token2.token_type]


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
    raise NotImplementedError()


# POP :: Cpu -> Token -> None
def POP(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


# PUSH :: Cpu -> Token -> None
def PUSH(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


# RES :: Cpu -> Token -> Token -> None
def RES(cpu: Cpu, token1: Token, token2: Token) -> None:
    raise NotImplementedError()


# RET :: Cpu -> Token -> None
def RET(cpu: Cpu, token1: Token = None) -> None:
    # Return (exit the program)
    return


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
    raise NotImplementedError()


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
    raise NotImplementedError()


# SWAP :: Cpu -> Token -> None
def SWAP(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


# XOR :: Cpu -> Token -> None
def XOR(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


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
