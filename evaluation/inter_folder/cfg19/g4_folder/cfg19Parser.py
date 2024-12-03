# Generated from ./g4_folder/cfg19.g4 by ANTLR 4.13.2
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
        4,1,4,40,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        2,7,7,7,1,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,3,2,26,8,2,1,3,1,3,1,
        4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,
        14,0,1,1,0,2,3,32,0,16,1,0,0,0,2,19,1,0,0,0,4,25,1,0,0,0,6,27,1,
        0,0,0,8,29,1,0,0,0,10,31,1,0,0,0,12,34,1,0,0,0,14,37,1,0,0,0,16,
        17,3,2,1,0,17,18,3,10,5,0,18,1,1,0,0,0,19,20,5,1,0,0,20,21,3,4,2,
        0,21,3,1,0,0,0,22,26,1,0,0,0,23,24,5,1,0,0,24,26,3,6,3,0,25,22,1,
        0,0,0,25,23,1,0,0,0,26,5,1,0,0,0,27,28,1,0,0,0,28,7,1,0,0,0,29,30,
        7,0,0,0,30,9,1,0,0,0,31,32,3,8,4,0,32,33,3,12,6,0,33,11,1,0,0,0,
        34,35,3,8,4,0,35,36,3,14,7,0,36,13,1,0,0,0,37,38,3,8,4,0,38,15,1,
        0,0,0,1,25
    ]

class cfg19Parser ( Parser ):

    grammarFileName = "cfg19.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'a'", "'b'", "'c'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WS" ]

    RULE_s = 0
    RULE_s1 = 1
    RULE_s2 = 2
    RULE_s3 = 3
    RULE_s4 = 4
    RULE_s6 = 5
    RULE_s7 = 6
    RULE_s8 = 7

    ruleNames =  [ "s", "s1", "s2", "s3", "s4", "s6", "s7", "s8" ]

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

        def s1(self):
            return self.getTypedRuleContext(cfg19Parser.S1Context,0)


        def s6(self):
            return self.getTypedRuleContext(cfg19Parser.S6Context,0)


        def getRuleIndex(self):
            return cfg19Parser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)




    def s(self):

        localctx = cfg19Parser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.s1()
            self.state = 17
            self.s6()
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

        def s2(self):
            return self.getTypedRuleContext(cfg19Parser.S2Context,0)


        def getRuleIndex(self):
            return cfg19Parser.RULE_s1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS1" ):
                listener.enterS1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS1" ):
                listener.exitS1(self)




    def s1(self):

        localctx = cfg19Parser.S1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_s1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(cfg19Parser.T__0)
            self.state = 20
            self.s2()
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

        def s3(self):
            return self.getTypedRuleContext(cfg19Parser.S3Context,0)


        def getRuleIndex(self):
            return cfg19Parser.RULE_s2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS2" ):
                listener.enterS2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS2" ):
                listener.exitS2(self)




    def s2(self):

        localctx = cfg19Parser.S2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_s2)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(cfg19Parser.T__0)
                self.state = 24
                self.s3()
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


        def getRuleIndex(self):
            return cfg19Parser.RULE_s3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS3" ):
                listener.enterS3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS3" ):
                listener.exitS3(self)




    def s3(self):

        localctx = cfg19Parser.S3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_s3)
        try:
            self.enterOuterAlt(localctx, 1)

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


        def getRuleIndex(self):
            return cfg19Parser.RULE_s4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS4" ):
                listener.enterS4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS4" ):
                listener.exitS4(self)




    def s4(self):

        localctx = cfg19Parser.S4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_s4)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def s4(self):
            return self.getTypedRuleContext(cfg19Parser.S4Context,0)


        def s7(self):
            return self.getTypedRuleContext(cfg19Parser.S7Context,0)


        def getRuleIndex(self):
            return cfg19Parser.RULE_s6

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS6" ):
                listener.enterS6(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS6" ):
                listener.exitS6(self)




    def s6(self):

        localctx = cfg19Parser.S6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_s6)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.s4()
            self.state = 32
            self.s7()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class S7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s4(self):
            return self.getTypedRuleContext(cfg19Parser.S4Context,0)


        def s8(self):
            return self.getTypedRuleContext(cfg19Parser.S8Context,0)


        def getRuleIndex(self):
            return cfg19Parser.RULE_s7

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS7" ):
                listener.enterS7(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS7" ):
                listener.exitS7(self)




    def s7(self):

        localctx = cfg19Parser.S7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_s7)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.s4()
            self.state = 35
            self.s8()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class S8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s4(self):
            return self.getTypedRuleContext(cfg19Parser.S4Context,0)


        def getRuleIndex(self):
            return cfg19Parser.RULE_s8

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS8" ):
                listener.enterS8(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS8" ):
                listener.exitS8(self)




    def s8(self):

        localctx = cfg19Parser.S8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_s8)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.s4()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





