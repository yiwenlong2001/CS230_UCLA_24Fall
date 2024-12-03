# Generated from ./g4_folder/cfg9.g4 by ANTLR 4.13.2
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
        4,1,4,17,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,
        3,2,15,8,2,1,2,0,0,3,0,2,4,0,0,14,0,6,1,0,0,0,2,9,1,0,0,0,4,14,1,
        0,0,0,6,7,5,1,0,0,7,8,3,4,2,0,8,1,1,0,0,0,9,10,5,2,0,0,10,11,5,3,
        0,0,11,3,1,0,0,0,12,15,5,0,0,1,13,15,3,2,1,0,14,12,1,0,0,0,14,13,
        1,0,0,0,15,5,1,0,0,0,1,14
    ]

class cfg9Parser ( Parser ):

    grammarFileName = "cfg9.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'a'", "'b'", "'c'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WS" ]

    RULE_s = 0
    RULE_s1 = 1
    RULE_s2 = 2

    ruleNames =  [ "s", "s1", "s2" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    WS=4

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

        def s2(self):
            return self.getTypedRuleContext(cfg9Parser.S2Context,0)


        def getRuleIndex(self):
            return cfg9Parser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)




    def s(self):

        localctx = cfg9Parser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(cfg9Parser.T__0)
            self.state = 7
            self.s2()
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
            return cfg9Parser.RULE_s1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS1" ):
                listener.enterS1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS1" ):
                listener.exitS1(self)




    def s1(self):

        localctx = cfg9Parser.S1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_s1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self.match(cfg9Parser.T__1)
            self.state = 10
            self.match(cfg9Parser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class S2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(cfg9Parser.EOF, 0)

        def s1(self):
            return self.getTypedRuleContext(cfg9Parser.S1Context,0)


        def getRuleIndex(self):
            return cfg9Parser.RULE_s2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS2" ):
                listener.enterS2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS2" ):
                listener.exitS2(self)




    def s2(self):

        localctx = cfg9Parser.S2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_s2)
        try:
            self.state = 14
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.match(cfg9Parser.EOF)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.s1()
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





