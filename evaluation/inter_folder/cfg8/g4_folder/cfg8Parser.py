# Generated from ./g4_folder/cfg8.g4 by ANTLR 4.13.2
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
        4,1,3,18,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,
        1,2,3,2,16,8,2,1,2,0,0,3,0,2,4,0,0,15,0,6,1,0,0,0,2,8,1,0,0,0,4,
        15,1,0,0,0,6,7,3,4,2,0,7,1,1,0,0,0,8,9,5,1,0,0,9,10,5,2,0,0,10,3,
        1,0,0,0,11,16,3,2,1,0,12,13,3,2,1,0,13,14,3,4,2,0,14,16,1,0,0,0,
        15,11,1,0,0,0,15,12,1,0,0,0,16,5,1,0,0,0,1,15
    ]

class cfg8Parser ( Parser ):

    grammarFileName = "cfg8.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'a'", "'b'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "WS" ]

    RULE_s = 0
    RULE_s1 = 1
    RULE_s2 = 2

    ruleNames =  [ "s", "s1", "s2" ]

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

        def s2(self):
            return self.getTypedRuleContext(cfg8Parser.S2Context,0)


        def getRuleIndex(self):
            return cfg8Parser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)




    def s(self):

        localctx = cfg8Parser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
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
            return cfg8Parser.RULE_s1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS1" ):
                listener.enterS1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS1" ):
                listener.exitS1(self)




    def s1(self):

        localctx = cfg8Parser.S1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_s1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(cfg8Parser.T__0)
            self.state = 9
            self.match(cfg8Parser.T__1)
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

        def s1(self):
            return self.getTypedRuleContext(cfg8Parser.S1Context,0)


        def s2(self):
            return self.getTypedRuleContext(cfg8Parser.S2Context,0)


        def getRuleIndex(self):
            return cfg8Parser.RULE_s2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS2" ):
                listener.enterS2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS2" ):
                listener.exitS2(self)




    def s2(self):

        localctx = cfg8Parser.S2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_s2)
        try:
            self.state = 15
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.s1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 12
                self.s1()
                self.state = 13
                self.s2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





