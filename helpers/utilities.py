import numpy as np
from helpers.token import Token, TokenType


class Utilities:
    @staticmethod
    def read_asm_file(file: str) -> [list]:
        """
        Read an assembly file and return the contents as a list
        :param file: The file to be read from
        :return: The file parsed as a list
        """
        lines = []
        if not file.endswith(".asm"):
            raise NameError("Filetype not supported, please specify a .asm file")
        asm_file = open(file=file, mode="r")
        for line in asm_file.readlines():
            line = line.split(';')[0]  # don't parse the comments
            # check if the line is not empty
            if line:
                splitted = line.split('    ')
                if not splitted[0]:
                    lines.append(splitted[1])
                else:
                    lines.append(splitted[0])
        return lines

    @staticmethod
    def get_value(token: Token) -> np.uint8:
        if not token.token_type == TokenType.VALUE:
            raise ValueError(f"Wrong token type input specified, "
                             f"expected {TokenType.VALUE.name} received {token.token_type.name}")
        # Check what the subtype is
        if token.sub_type == TokenType.HEXADECIMAL:
            # let's strip the $ from the value and return it
            value = token.value.strip("$")
            return np.uint8(int(value, 16))
        elif token.sub_type == TokenType.DECIMAL:
            # let's strip the # from the value and return it
            return np.uint8(token.value.strip("#"))
        elif token.sub_type == TokenType.BINARY:
            # let's strip the % from the value
            value = token.value.strip("%")
            return np.uint8(int(value, 2))
        # The token value has an unknown subtype
        else:
            raise ValueError(f"The token {TokenType.VALUE.name} has an unknown subtype: {token.sub_type.name}")
