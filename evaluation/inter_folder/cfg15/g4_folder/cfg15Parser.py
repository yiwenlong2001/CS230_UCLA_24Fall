# Generated from ./g4_folder/cfg15.g4 by ANTLR 4.13.2
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
        4,1,4,68,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,0,1,1,
        1,1,1,2,1,2,1,2,1,3,1,3,1,3,3,3,37,8,3,1,4,1,4,1,4,1,5,1,5,1,5,1,
        6,1,6,1,6,3,6,48,8,6,1,7,1,7,1,7,3,7,53,8,7,1,8,1,8,1,8,3,8,58,8,
        8,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,11,0,0,12,0,2,4,6,8,10,
        12,14,16,18,20,22,0,0,59,0,24,1,0,0,0,2,28,1,0,0,0,4,30,1,0,0,0,
        6,36,1,0,0,0,8,38,1,0,0,0,10,41,1,0,0,0,12,47,1,0,0,0,14,52,1,0,
        0,0,16,57,1,0,0,0,18,59,1,0,0,0,20,61,1,0,0,0,22,64,1,0,0,0,24,25,
        3,2,1,0,25,26,3,8,4,0,26,27,3,20,10,0,27,1,1,0,0,0,28,29,5,1,0,0,
        29,3,1,0,0,0,30,31,5,2,0,0,31,32,3,6,3,0,32,5,1,0,0,0,33,37,1,0,
        0,0,34,35,5,2,0,0,35,37,3,6,3,0,36,33,1,0,0,0,36,34,1,0,0,0,37,7,
        1,0,0,0,38,39,5,3,0,0,39,40,3,10,5,0,40,9,1,0,0,0,41,42,5,3,0,0,
        42,43,3,12,6,0,43,11,1,0,0,0,44,48,1,0,0,0,45,46,5,3,0,0,46,48,3,
        14,7,0,47,44,1,0,0,0,47,45,1,0,0,0,48,13,1,0,0,0,49,53,1,0,0,0,50,
        51,5,3,0,0,51,53,3,16,8,0,52,49,1,0,0,0,52,50,1,0,0,0,53,15,1,0,
        0,0,54,58,1,0,0,0,55,56,5,3,0,0,56,58,3,18,9,0,57,54,1,0,0,0,57,
        55,1,0,0,0,58,17,1,0,0,0,59,60,1,0,0,0,60,19,1,0,0,0,61,62,5,2,0,
        0,62,63,3,22,11,0,63,21,1,0,0,0,64,65,5,2,0,0,65,66,3,4,2,0,66,23,
        1,0,0,0,4,36,47,52,57
    ]

class cfg15Parser ( Parser ):

    grammarFileName = "cfg15.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'a'", "'c'", "'b'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WS" ]

    RULE_s = 0
    RULE_s1 = 1
    RULE_s10 = 2
    RULE_s11 = 3
    RULE_s2 = 4
    RULE_s3 = 5
    RULE_s4 = 6
    RULE_s5 = 7
    RULE_s6 = 8
    RULE_s7 = 9
    RULE_s8 = 10
    RULE_s9 = 11

    ruleNames =  [ "s", "s1", "s10", "s11", "s2", "s3", "s4", "s5", "s6", 
                   "s7", "s8", "s9" ]

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
            return self.getTypedRuleContext(cfg15Parser.S1Context,0)


        def s2(self):
            return self.getTypedRuleContext(cfg15Parser.S2Context,0)


        def s8(self):
            return self.getTypedRuleContext(cfg15Parser.S8Context,0)


        def getRuleIndex(self):
            return cfg15Parser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)




    def s(self):

        localctx = cfg15Parser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.s1()
            self.state = 25
            self.s2()
            self.state = 26
            self.s8()
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
            return cfg15Parser.RULE_s1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS1" ):
                listener.enterS1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS1" ):
                listener.exitS1(self)




    def s1(self):

        localctx = cfg15Parser.S1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_s1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(cfg15Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class S10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s11(self):
            return self.getTypedRuleContext(cfg15Parser.S11Context,0)


        def getRuleIndex(self):
            return cfg15Parser.RULE_s10

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS10" ):
                listener.enterS10(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS10" ):
                listener.exitS10(self)




    def s10(self):

        localctx = cfg15Parser.S10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_s10)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(cfg15Parser.T__1)
            self.state = 31
            self.s11()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class S11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s11(self):
            return self.getTypedRuleContext(cfg15Parser.S11Context,0)


        def getRuleIndex(self):
            return cfg15Parser.RULE_s11

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS11" ):
                listener.enterS11(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS11" ):
                listener.exitS11(self)




    def s11(self):

        localctx = cfg15Parser.S11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_s11)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(cfg15Parser.T__1)
                self.state = 35
                self.s11()
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


    class S2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s3(self):
            return self.getTypedRuleContext(cfg15Parser.S3Context,0)


        def getRuleIndex(self):
            return cfg15Parser.RULE_s2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS2" ):
                listener.enterS2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS2" ):
                listener.exitS2(self)




    def s2(self):

        localctx = cfg15Parser.S2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_s2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(cfg15Parser.T__2)
            self.state = 39
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

        def s4(self):
            return self.getTypedRuleContext(cfg15Parser.S4Context,0)


        def getRuleIndex(self):
            return cfg15Parser.RULE_s3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS3" ):
                listener.enterS3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS3" ):
                listener.exitS3(self)




    def s3(self):

        localctx = cfg15Parser.S3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_s3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(cfg15Parser.T__2)
            self.state = 42
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

        def s5(self):
            return self.getTypedRuleContext(cfg15Parser.S5Context,0)


        def getRuleIndex(self):
            return cfg15Parser.RULE_s4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS4" ):
                listener.enterS4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS4" ):
                listener.exitS4(self)




    def s4(self):

        localctx = cfg15Parser.S4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_s4)
        try:
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.match(cfg15Parser.T__2)
                self.state = 46
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

        def s6(self):
            return self.getTypedRuleContext(cfg15Parser.S6Context,0)


        def getRuleIndex(self):
            return cfg15Parser.RULE_s5

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS5" ):
                listener.enterS5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS5" ):
                listener.exitS5(self)




    def s5(self):

        localctx = cfg15Parser.S5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_s5)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(cfg15Parser.T__2)
                self.state = 51
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

        def s7(self):
            return self.getTypedRuleContext(cfg15Parser.S7Context,0)


        def getRuleIndex(self):
            return cfg15Parser.RULE_s6

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS6" ):
                listener.enterS6(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS6" ):
                listener.exitS6(self)




    def s6(self):

        localctx = cfg15Parser.S6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_s6)
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(cfg15Parser.T__2)
                self.state = 56
                self.s7()
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


    class S7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cfg15Parser.RULE_s7

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS7" ):
                listener.enterS7(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS7" ):
                listener.exitS7(self)




    def s7(self):

        localctx = cfg15Parser.S7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_s7)
        try:
            self.enterOuterAlt(localctx, 1)

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

        def s9(self):
            return self.getTypedRuleContext(cfg15Parser.S9Context,0)


        def getRuleIndex(self):
            return cfg15Parser.RULE_s8

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS8" ):
                listener.enterS8(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS8" ):
                listener.exitS8(self)




    def s8(self):

        localctx = cfg15Parser.S8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_s8)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(cfg15Parser.T__1)
            self.state = 62
            self.s9()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class S9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s10(self):
            return self.getTypedRuleContext(cfg15Parser.S10Context,0)


        def getRuleIndex(self):
            return cfg15Parser.RULE_s9

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS9" ):
                listener.enterS9(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS9" ):
                listener.exitS9(self)




    def s9(self):

        localctx = cfg15Parser.S9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_s9)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(cfg15Parser.T__1)
            self.state = 65
            self.s10()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





