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
    CPL = 7
    DAA = 8
    DEC = 9
    DI = 10
    EI = 11
    HALT = 12
    INC = 13
    JP = 14
    JR = 15
    LD = 16
    LDD = 17
    LDH = 18
    LDI = 19
    NOP = 20
    OR = 21
    POP = 22
    PUSH = 23
    RES = 24
    RET = 25
    RETI = 26
    RL = 27
    RLA = 28
    RLC = 29
    RLCA = 30
    RR = 31
    RRA = 32
    RRC = 33
    RRCA = 34
    RST = 35
    SBC = 36
    SCF = 37
    SET = 38
    SLA = 39
    SRA = 40
    SRL = 41
    STOP = 42
    SUB = 43
    SWAP = 44
    XOR = 45
    # --- 8-bit Registers ---
    REGISTER_A = 50
    REGISTER_B = 51
    REGISTER_C = 52
    REGISTER_D = 53
    REGISTER_E = 54
    REGISTER_F = 55
    REGISTER_H = 56
    REGISTER_L = 57

    # -- 16-bit Registers ---
    REGISTER_AF = 60
    REGISTER_BC = 61
    REGISTER_DE = 62
    REGISTER_HL = 63
    REGISTER_SP = 64
    REGISTER_PC = 65

    # -- Conditions
    CONDITION_NZ = 70
    CONDITION_Z = 71
    CONDITION_NC = 72
    CONDITION_C = 73

    # --- Values ---
    DECIMAL = 80
    HEXADECIMAL = 81
    BINARY = 82

    # --- Labels ---
    LABEL = 90

    # --- Unknown ---
    UNKNOWN = 100
