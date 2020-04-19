class Utilities:
    @staticmethod
    def read_asm_file(file: str) -> list:
        """
        Read an assembly file and return the contents as a list
        :param file: The file to be read from
        :return: The file parsed as a list
        """
        lines = []
        if not file.endswith(".asm"):
            raise NameError("Incorrect file specified")
        asm_file = open(file=file, mode="r")
        for line in asm_file.readlines():
            lines.append(line.split())
        return lines
