# vim: set fileencoding=utf-8
from antlr4 import *

class Fortran90LexerBase(Lexer):
    def IsColumnZero(self):
        return self.column == 0
