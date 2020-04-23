from enum import Enum


class TokenType(Enum):
    # --- Opcodes ---
    ADC = 0
    ADD = 1
    AND = 2
    BIT = 3
    CALL = 4
    CCF = 5
    CP = 6
    CPD = 7
    CPDR = 8
    CPI = 9
    CPIR = 10
    CPL = 11
    DAA = 12
    DEC = 13
    DI = 14
    DJNZ = 15
    EI = 16
    EX = 17
    EXX = 18
    HALT = 19
    IM = 20
    IN = 21
    INC = 22
    IND = 23
    INDR = 24
    INI = 25
    INIR = 26
    JP = 27
    JR = 28
    LD = 29
    LDD = 30
    LDDR = 31
    LDI = 32
    LDIR = 33
    NEG = 34
    NOP = 35
    OR = 36
    OTDR = 37
    OTIR = 38
    OUT = 39
    OUTD = 40
    OUTI = 41
    POP = 42
    PUSH = 43
    RES = 44
    RET = 45
    RETI = 46
    RETN = 47
    RL = 48
    RLA = 49
    RLC = 50
    RLCA = 51
    RLD = 52
    RR = 53
    RRA = 54
    RRC = 55
    RRCA = 56
    RRD = 57
    RST = 58
    SBC = 59
    SCF = 60
    SET = 61
    SLA = 62
    SLL = 63
    SRA = 64
    SRL = 65
    SUB = 66
    XOR = 67
    # --- 8-bit Registers ---
    REGISTER_A = 68
    REGISTER_B = 69
    REGISTER_C = 70
    REGISTER_D = 71
    REGISTER_E = 72
    REGISTER_F = 73
    REGISTER_H = 74
    REGISTER_L = 75

    # -- 16-bit Registers ---
    REGISTER_AF = 76
    REGISTER_BC = 77
    REGISTER_DE = 78
    REGISTER_HL = 79

    # --- Values ---
    DECIMAL = 100
    HEXADECIMAL = 101
    BINARY = 102

    # --- Labels ---
    LABEL = 110

    # --- Unknown ---
    UNKNOWN = 150

