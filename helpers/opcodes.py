import numpy as np
from typing import Union
from helpers.decorators import count
from helpers.token import TokenType as tt
from helpers.token import Token
from helpers.exceptions import LabelNotFound
from helpers.utilities import Utilities
from cpu import Cpu


def ADC(cpu: Cpu, token1: Token, token2: Token) -> None:
    raise NotImplementedError()


def ADD(cpu: Cpu, token1: Token, token2: Token) -> None:
    # TODO: Set flags
    # If token 2 is of type value
    if token2.token_type == tt.VALUE:
        # Add the value of token 2 to the register specified inside token 1
        cpu.register[token1.token_type] += Utilities.get_value(token2)
    # otherwise it must be another register
    else:
        cpu.register[token1.token_type] += cpu.register[token2.token_type]


def AND(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


def BIT(cpu: Cpu, token1: Token, token2: Token) -> None:
    raise NotImplementedError()


def CALL(cpu: Cpu, token1: Token, token2: Token = None) -> None:
    raise NotImplementedError()


def CCF(cpu: Cpu) -> None:
    raise NotImplementedError()


def CP(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


def CPL(cpu: Cpu) -> None:
    raise NotImplementedError()


def DAA(cpu: Cpu) -> None:
    raise NotImplementedError()


def DEC(cpu: Cpu, token1: Token) -> None:
    # Check if the register isn't already at 0
    if not cpu.register[token1.token_type] == 0:
        cpu.register[token1.token_type] -= 1
        # Set the subtract flag since a subtraction was performed
        cpu.flags["N"] = True
    # Set the zero flag to true since the register value is now zero
    if cpu.register[token1.token_type] == 0:
        cpu.flags["Z"] = True


def DI(cpu: Cpu) -> None:
    raise NotImplementedError()


def EI(cpu: Cpu) -> None:
    raise NotImplementedError()


def HALT(cpu: Cpu) -> None:
    raise NotImplementedError()


def INC(cpu: Cpu, token1: Token) -> None:
    # TODO: Set flags
    cpu.register[token1.token_type] += 1
    # Reset the the subtract flag since a increment was performed
    cpu.flags["N"] = False


@count
def JP(cpu: Cpu, token1: Token, token2: Token = None) -> Union[None, np.uint8]:
    # If the token 1 is of type label, jump straight away
    if token1.token_type == tt.LABEL:
        # Check if the label exists
        if token1.value in cpu.labels:
            return cpu.labels[token1.value] - 1  # Remove one since it is a line number not an index
        else:
            raise LabelNotFound(token1.line, f"The label {token1.value} was not found")
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
                raise LabelNotFound(token2.line, f"The label '{token2.value}' was not found")
    return None


def JR(cpu: Cpu, token1: Token, token2: Token = None) -> None:
    raise NotImplementedError()


def LD(cpu: Cpu, token1: Token, token2: Token) -> None:
    # Check if the second parameter input is of type value
    if token2.token_type == tt.VALUE:
        # Set the register specified in token 1 to the value of token 2
        cpu.register[token1.token_type] = Utilities.get_value(token2)
    # Otherwise the second parameter must be a register
    else:
        # Set the value of the register specified in token 1 to be the value of the register specified in token 2
        cpu.register[token1.token_type] = cpu.register[token2.token_type]


def LDD(cpu: Cpu, token1: Token, token2: Token) -> None:
    raise NotImplementedError()


def LDH(cpu: Cpu, token1: Token, token2: Token) -> None:
    raise NotImplementedError()


def LDI(cpu: Cpu, token1: Token, token2: Token) -> None:
    raise NotImplementedError()


def NOP(cpu: Cpu) -> None:
    # Do nothing
    return


def OR(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


def POP(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


def PUSH(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


def RES(cpu: Cpu, token1: Token, token2: Token) -> None:
    raise NotImplementedError()


def RET(cpu: Cpu, token1: Token = None) -> None:
    # Return (exit the program)
    return


def RETI(cpu: Cpu) -> None:
    raise NotImplementedError()


def RL(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


def RLA(cpu: Cpu) -> None:
    raise NotImplementedError()


def RLC(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


def RLCA(cpu: Cpu) -> None:
    raise NotImplementedError()


def RR(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


def RRA(cpu: Cpu) -> None:
    raise NotImplementedError()


def RRC(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


def RRCA(cpu: Cpu) -> None:
    raise NotImplementedError()


def RST(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


def SBC(cpu: Cpu, token1: Token, token2: Token) -> None:
    raise NotImplementedError()


def SCF(cpu: Cpu) -> None:
    raise NotImplementedError()


def SET(cpu: Cpu, token1: Token, token2: Token) -> None:
    raise NotImplementedError()


def SLA(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


def SRA(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


def SRL(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


def STOP(cpu: Cpu) -> None:
    raise NotImplementedError()


def SUB(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


def SWAP(cpu: Cpu, token1: Token) -> None:
    raise NotImplementedError()


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
