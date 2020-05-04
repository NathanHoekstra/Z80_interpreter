import sys
import inspect


# Custom exception without traceback thanks to:
# https://stackoverflow.com/questions/17784849/print-an-error-message-without-printing-a-traceback-and-close-the-program-when-a
class NoTraceBackWithLineNumber(Exception):
    def __init__(self, msg):
        try:
            ln = sys.exc_info()[-1].tb_lineno
        except AttributeError:
            ln = inspect.currentframe().f_back.f_lineno
        self.args = "{0.__name__} (line {1}): {2}".format(type(self), ln, msg),
        sys.exit(self)


# Inherited assembly syntax error exception
class ASMSyntaxError(NoTraceBackWithLineNumber):
    pass


# Inherited label not found exception
class LabelNotFound(NoTraceBackWithLineNumber):
    pass
