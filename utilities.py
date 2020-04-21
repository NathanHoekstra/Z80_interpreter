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
                lines.append(line.split('  ')[0])
        return lines
