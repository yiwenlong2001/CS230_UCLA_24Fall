# Generated from ./g4_folder/cfg27.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,1,9,2,0,7,0,2,1,7,1,1,0,1,0,1,1,1,1,1,1,0,0,2,0,2,0,0,6,0,4,
        1,0,0,0,2,6,1,0,0,0,4,5,3,2,1,0,5,1,1,0,0,0,6,7,1,0,0,0,7,3,1,0,
        0,0,0
    ]

class cfg27Parser ( Parser ):

    grammarFileName = "cfg27.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "WS" ]

    RULE_s = 0
    RULE_s1 = 1

    ruleNames =  [ "s", "s1" ]

    EOF = Token.EOF
    WS=1

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s1(self):
            return self.getTypedRuleContext(cfg27Parser.S1Context,0)


        def getRuleIndex(self):
            return cfg27Parser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)




    def s(self):

        localctx = cfg27Parser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.s1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class S1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cfg27Parser.RULE_s1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS1" ):
                listener.enterS1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS1" ):
                listener.exitS1(self)




    def s1(self):

        localctx = cfg27Parser.S1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_s1)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





