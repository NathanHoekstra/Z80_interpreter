from helpers.token import TokenType as tt
from helpers.token import Token
from cpu import Cpu


def ADC(cpu: Cpu, token1: Token, token2: Token):
    raise NotImplementedError()


def ADD(cpu: Cpu, token1: Token, token2: Token):
    raise NotImplementedError()


def AND(cpu: Cpu, token1: Token):
    raise NotImplementedError()


def BIT(cpu: Cpu, token1: Token, token2: Token):
    raise NotImplementedError()


def CALL(cpu: Cpu, token1: Token, token2: Token = None):
    raise NotImplementedError()


def CCF(cpu: Cpu):
    raise NotImplementedError()


def CP(cpu: Cpu, token1: Token):
    raise NotImplementedError()


def CPL(cpu: Cpu):
    raise NotImplementedError()


def DAA(cpu: Cpu):
    raise NotImplementedError()


def DEC(cpu: Cpu, token1: Token):
    raise NotImplementedError()


def DI(cpu: Cpu):
    raise NotImplementedError()


def EI(cpu: Cpu):
    raise NotImplementedError()


def HALT(cpu: Cpu):
    raise NotImplementedError()


def INC(cpu: Cpu, token1: Token):
    raise NotImplementedError()


def JP(cpu: Cpu, token1: Token, token2: Token = None):
    raise NotImplementedError()


def JR(cpu: Cpu, token1: Token, token2: Token = None):
    raise NotImplementedError()


def LD(cpu: Cpu, token1: Token, token2: Token):
    raise NotImplementedError()


def LDD(cpu: Cpu, token1: Token, token2: Token):
    raise NotImplementedError()


def LDH(cpu: Cpu, token1: Token, token2: Token):
    raise NotImplementedError()


def LDI(cpu: Cpu, token1: Token, token2: Token):
    raise NotImplementedError()


def NOP(cpu: Cpu):
    raise NotImplementedError()


def OR(cpu: Cpu, token1: Token):
    raise NotImplementedError()


def POP(cpu: Cpu, token1: Token):
    raise NotImplementedError()


def PUSH(cpu: Cpu, token1: Token):
    raise NotImplementedError()


def RES(cpu: Cpu, token1: Token, token2: Token):
    raise NotImplementedError()


def RET(cpu: Cpu, token1: Token = None):
    raise NotImplementedError()


def RETI(cpu: Cpu):
    raise NotImplementedError()


def RL(cpu: Cpu, token1: Token):
    raise NotImplementedError()


def RLA(cpu: Cpu):
    raise NotImplementedError()


def RLC(cpu: Cpu, token1: Token):
    raise NotImplementedError()


def RLCA(cpu: Cpu):
    raise NotImplementedError()


def RR(cpu: Cpu, token1: Token):
    raise NotImplementedError()


def RRA(cpu: Cpu):
    raise NotImplementedError()


def RRC(cpu: Cpu, token1: Token):
    raise NotImplementedError()


def RRCA(cpu: Cpu):
    raise NotImplementedError()


def RST(cpu: Cpu, token1: Token):
    raise NotImplementedError()


def SBC(cpu: Cpu, token1: Token, token2: Token):
    raise NotImplementedError()


def SCF(cpu: Cpu):
    raise NotImplementedError()


def SET(cpu: Cpu, token1: Token, token2: Token):
    raise NotImplementedError()


def SLA(cpu: Cpu, token1: Token):
    raise NotImplementedError()


def SRA(cpu: Cpu, token1: Token):
    raise NotImplementedError()


def SRL(cpu: Cpu, token1: Token):
    raise NotImplementedError()


def STOP(cpu: Cpu):
    raise NotImplementedError()


def SUB(cpu: Cpu, token1: Token):
    raise NotImplementedError()


def SWAP(cpu: Cpu, token1: Token):
    raise NotImplementedError()


def XOR(cpu: Cpu, token1: Token):
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
