# Generated from ./g4_folder/cfg21.g4 by ANTLR 4.13.2
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
        4,1,5,31,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,1,1,1,
        1,1,1,1,3,1,17,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,29,
        8,4,1,4,0,0,5,0,2,4,6,8,0,0,27,0,10,1,0,0,0,2,16,1,0,0,0,4,18,1,
        0,0,0,6,21,1,0,0,0,8,28,1,0,0,0,10,11,3,4,2,0,11,1,1,0,0,0,12,13,
        5,1,0,0,13,17,5,2,0,0,14,15,5,3,0,0,15,17,5,4,0,0,16,12,1,0,0,0,
        16,14,1,0,0,0,17,3,1,0,0,0,18,19,3,2,1,0,19,20,3,6,3,0,20,5,1,0,
        0,0,21,22,3,2,1,0,22,23,3,8,4,0,23,7,1,0,0,0,24,29,1,0,0,0,25,26,
        3,2,1,0,26,27,3,8,4,0,27,29,1,0,0,0,28,24,1,0,0,0,28,25,1,0,0,0,
        29,9,1,0,0,0,2,16,28
    ]

class cfg21Parser ( Parser ):

    grammarFileName = "cfg21.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'a'", "'b'", "'c'", "'d'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WS" ]

    RULE_s = 0
    RULE_s1 = 1
    RULE_s3 = 2
    RULE_s4 = 3
    RULE_s5 = 4

    ruleNames =  [ "s", "s1", "s3", "s4", "s5" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    WS=5

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

        def s3(self):
            return self.getTypedRuleContext(cfg21Parser.S3Context,0)


        def getRuleIndex(self):
            return cfg21Parser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)




    def s(self):

        localctx = cfg21Parser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.s3()
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
            return cfg21Parser.RULE_s1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS1" ):
                listener.enterS1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS1" ):
                listener.exitS1(self)




    def s1(self):

        localctx = cfg21Parser.S1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_s1)
        try:
            self.state = 16
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.match(cfg21Parser.T__0)
                self.state = 13
                self.match(cfg21Parser.T__1)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(cfg21Parser.T__2)
                self.state = 15
                self.match(cfg21Parser.T__3)
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


    class S3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s1(self):
            return self.getTypedRuleContext(cfg21Parser.S1Context,0)


        def s4(self):
            return self.getTypedRuleContext(cfg21Parser.S4Context,0)


        def getRuleIndex(self):
            return cfg21Parser.RULE_s3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS3" ):
                listener.enterS3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS3" ):
                listener.exitS3(self)




    def s3(self):

        localctx = cfg21Parser.S3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_s3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.s1()
            self.state = 19
            self.s4()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class S4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s1(self):
            return self.getTypedRuleContext(cfg21Parser.S1Context,0)


        def s5(self):
            return self.getTypedRuleContext(cfg21Parser.S5Context,0)


        def getRuleIndex(self):
            return cfg21Parser.RULE_s4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS4" ):
                listener.enterS4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS4" ):
                listener.exitS4(self)




    def s4(self):

        localctx = cfg21Parser.S4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_s4)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.s1()
            self.state = 22
            self.s5()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class S5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s1(self):
            return self.getTypedRuleContext(cfg21Parser.S1Context,0)


        def s5(self):
            return self.getTypedRuleContext(cfg21Parser.S5Context,0)


        def getRuleIndex(self):
            return cfg21Parser.RULE_s5

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS5" ):
                listener.enterS5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS5" ):
                listener.exitS5(self)




    def s5(self):

        localctx = cfg21Parser.S5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_s5)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [1, 3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.s1()
                self.state = 26
                self.s5()
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





