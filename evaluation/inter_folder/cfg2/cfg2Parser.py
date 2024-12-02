# Generated from ./g4_folder/cfg2.g4 by ANTLR 4.13.2
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
        4,1,3,13,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,3,1,11,8,1,1,1,
        0,0,2,0,2,0,0,11,0,4,1,0,0,0,2,10,1,0,0,0,4,5,3,2,1,0,5,6,5,1,0,
        0,6,1,1,0,0,0,7,8,5,2,0,0,8,11,3,2,1,0,9,11,5,0,0,1,10,7,1,0,0,0,
        10,9,1,0,0,0,11,3,1,0,0,0,1,10
    ]

class cfg2Parser ( Parser ):

    grammarFileName = "cfg2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'d'", "'a'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "WS" ]

    RULE_s = 0
    RULE_s1 = 1

    ruleNames =  [ "s", "s1" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    WS=3

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
            return self.getTypedRuleContext(cfg2Parser.S1Context,0)


        def getRuleIndex(self):
            return cfg2Parser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)




    def s(self):

        localctx = cfg2Parser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.s1()
            self.state = 5
            self.match(cfg2Parser.T__0)
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

        def s1(self):
            return self.getTypedRuleContext(cfg2Parser.S1Context,0)


        def EOF(self):
            return self.getToken(cfg2Parser.EOF, 0)

        def getRuleIndex(self):
            return cfg2Parser.RULE_s1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS1" ):
                listener.enterS1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS1" ):
                listener.exitS1(self)




    def s1(self):

        localctx = cfg2Parser.S1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_s1)
        try:
            self.state = 10
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 7
                self.match(cfg2Parser.T__1)
                self.state = 8
                self.s1()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 9
                self.match(cfg2Parser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





