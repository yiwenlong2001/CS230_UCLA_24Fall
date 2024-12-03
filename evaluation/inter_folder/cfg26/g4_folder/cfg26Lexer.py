# Generated from ./g4_folder/cfg26.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,1,10,6,-1,2,0,7,0,1,0,4,0,5,8,0,11,0,12,0,6,1,0,1,0,0,0,1,1,
        1,1,0,1,3,0,9,10,13,13,32,32,10,0,1,1,0,0,0,1,4,1,0,0,0,3,5,7,0,
        0,0,4,3,1,0,0,0,5,6,1,0,0,0,6,4,1,0,0,0,6,7,1,0,0,0,7,8,1,0,0,0,
        8,9,6,0,0,0,9,2,1,0,0,0,2,0,6,1,6,0,0
    ]

class cfg26Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "WS" ]

    ruleNames = [ "WS" ]

    grammarFileName = "cfg26.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


