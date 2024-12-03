# Generated from ./g4_folder/cfg14.g4 by ANTLR 4.13.2
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
        4,1,3,40,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,
        30,8,4,1,5,1,5,1,5,1,5,3,5,36,8,5,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,
        12,0,0,34,0,14,1,0,0,0,2,16,1,0,0,0,4,19,1,0,0,0,6,22,1,0,0,0,8,
        29,1,0,0,0,10,35,1,0,0,0,12,37,1,0,0,0,14,15,3,4,2,0,15,1,1,0,0,
        0,16,17,5,1,0,0,17,18,5,2,0,0,18,3,1,0,0,0,19,20,3,2,1,0,20,21,3,
        6,3,0,21,5,1,0,0,0,22,23,3,2,1,0,23,24,3,8,4,0,24,7,1,0,0,0,25,30,
        1,0,0,0,26,27,3,2,1,0,27,28,3,10,5,0,28,30,1,0,0,0,29,25,1,0,0,0,
        29,26,1,0,0,0,30,9,1,0,0,0,31,36,1,0,0,0,32,33,3,2,1,0,33,34,3,12,
        6,0,34,36,1,0,0,0,35,31,1,0,0,0,35,32,1,0,0,0,36,11,1,0,0,0,37,38,
        1,0,0,0,38,13,1,0,0,0,2,29,35
    ]

class cfg14Parser ( Parser ):

    grammarFileName = "cfg14.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'a'", "'b'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "WS" ]

    RULE_s = 0
    RULE_s1 = 1
    RULE_s2 = 2
    RULE_s3 = 3
    RULE_s4 = 4
    RULE_s5 = 5
    RULE_s6 = 6

    ruleNames =  [ "s", "s1", "s2", "s3", "s4", "s5", "s6" ]

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
            return self.getTypedRuleContext(cfg14Parser.S2Context,0)


        def getRuleIndex(self):
            return cfg14Parser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)




    def s(self):

        localctx = cfg14Parser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
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
            return cfg14Parser.RULE_s1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS1" ):
                listener.enterS1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS1" ):
                listener.exitS1(self)




    def s1(self):

        localctx = cfg14Parser.S1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_s1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(cfg14Parser.T__0)
            self.state = 17
            self.match(cfg14Parser.T__1)
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
            return self.getTypedRuleContext(cfg14Parser.S1Context,0)


        def s3(self):
            return self.getTypedRuleContext(cfg14Parser.S3Context,0)


        def getRuleIndex(self):
            return cfg14Parser.RULE_s2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS2" ):
                listener.enterS2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS2" ):
                listener.exitS2(self)




    def s2(self):

        localctx = cfg14Parser.S2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_s2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.s1()
            self.state = 20
            self.s3()
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
            return self.getTypedRuleContext(cfg14Parser.S1Context,0)


        def s4(self):
            return self.getTypedRuleContext(cfg14Parser.S4Context,0)


        def getRuleIndex(self):
            return cfg14Parser.RULE_s3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS3" ):
                listener.enterS3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS3" ):
                listener.exitS3(self)




    def s3(self):

        localctx = cfg14Parser.S3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_s3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.s1()
            self.state = 23
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
            return self.getTypedRuleContext(cfg14Parser.S1Context,0)


        def s5(self):
            return self.getTypedRuleContext(cfg14Parser.S5Context,0)


        def getRuleIndex(self):
            return cfg14Parser.RULE_s4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS4" ):
                listener.enterS4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS4" ):
                listener.exitS4(self)




    def s4(self):

        localctx = cfg14Parser.S4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_s4)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.s1()
                self.state = 27
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


    class S5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s1(self):
            return self.getTypedRuleContext(cfg14Parser.S1Context,0)


        def s6(self):
            return self.getTypedRuleContext(cfg14Parser.S6Context,0)


        def getRuleIndex(self):
            return cfg14Parser.RULE_s5

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS5" ):
                listener.enterS5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS5" ):
                listener.exitS5(self)




    def s5(self):

        localctx = cfg14Parser.S5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_s5)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.s1()
                self.state = 33
                self.s6()
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


    class S6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cfg14Parser.RULE_s6

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS6" ):
                listener.enterS6(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS6" ):
                listener.exitS6(self)




    def s6(self):

        localctx = cfg14Parser.S6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_s6)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





