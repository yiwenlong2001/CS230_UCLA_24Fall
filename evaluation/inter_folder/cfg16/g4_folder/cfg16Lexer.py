# Generated from ./g4_folder/cfg16.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,11,50,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,1,1,1,1,2,1,2,
        1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,4,10,
        45,8,10,11,10,12,10,46,1,10,1,10,0,0,11,1,1,3,2,5,3,7,4,9,5,11,6,
        13,7,15,8,17,9,19,10,21,11,1,0,1,3,0,9,10,13,13,32,32,50,0,1,1,0,
        0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,
        0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,
        1,23,1,0,0,0,3,25,1,0,0,0,5,27,1,0,0,0,7,29,1,0,0,0,9,31,1,0,0,0,
        11,33,1,0,0,0,13,35,1,0,0,0,15,37,1,0,0,0,17,39,1,0,0,0,19,41,1,
        0,0,0,21,44,1,0,0,0,23,24,5,48,0,0,24,2,1,0,0,0,25,26,5,49,0,0,26,
        4,1,0,0,0,27,28,5,50,0,0,28,6,1,0,0,0,29,30,5,51,0,0,30,8,1,0,0,
        0,31,32,5,52,0,0,32,10,1,0,0,0,33,34,5,53,0,0,34,12,1,0,0,0,35,36,
        5,54,0,0,36,14,1,0,0,0,37,38,5,55,0,0,38,16,1,0,0,0,39,40,5,56,0,
        0,40,18,1,0,0,0,41,42,5,57,0,0,42,20,1,0,0,0,43,45,7,0,0,0,44,43,
        1,0,0,0,45,46,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,48,1,0,0,0,
        48,49,6,10,0,0,49,22,1,0,0,0,2,0,46,1,6,0,0
    ]

class cfg16Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'0'", "'1'", "'2'", "'3'", "'4'", "'5'", "'6'", "'7'", "'8'", 
            "'9'" ]

    symbolicNames = [ "<INVALID>",
            "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "WS" ]

    grammarFileName = "cfg16.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


