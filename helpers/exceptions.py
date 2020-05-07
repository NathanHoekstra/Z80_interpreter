import sys


# Custom exception class
class NoTraceBackWithLineNumber(Exception):
    def __init__(self, line, msg):
        self.args = "{0.__name__} (line {1}): {2}".format(type(self), line, msg),
        sys.exit(self)


# Inherited assembly syntax error exception
class ASMSyntaxError(NoTraceBackWithLineNumber):
    pass


# Inherited ASM label error exception
class ASMLabelError(NoTraceBackWithLineNumber):
    pass


# Inherited Display Closed error exception
class DisplayClosed(NoTraceBackWithLineNumber):
    pass
