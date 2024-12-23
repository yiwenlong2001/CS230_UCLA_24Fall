# Generated from ./g4_folder/cfg24.g4 by ANTLR 4.13.2
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
        4,1,2,45,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        2,7,7,7,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,
        1,5,1,5,1,5,1,5,3,5,35,8,5,1,6,1,6,1,6,1,6,3,6,41,8,6,1,7,1,7,1,
        7,0,0,8,0,2,4,6,8,10,12,14,0,0,38,0,16,1,0,0,0,2,18,1,0,0,0,4,21,
        1,0,0,0,6,24,1,0,0,0,8,27,1,0,0,0,10,34,1,0,0,0,12,40,1,0,0,0,14,
        42,1,0,0,0,16,17,3,4,2,0,17,1,1,0,0,0,18,19,5,1,0,0,19,20,5,2,0,
        0,20,3,1,0,0,0,21,22,3,2,1,0,22,23,3,6,3,0,23,5,1,0,0,0,24,25,3,
        2,1,0,25,26,3,8,4,0,26,7,1,0,0,0,27,28,3,2,1,0,28,29,3,10,5,0,29,
        9,1,0,0,0,30,35,1,0,0,0,31,32,3,2,1,0,32,33,3,12,6,0,33,35,1,0,0,
        0,34,30,1,0,0,0,34,31,1,0,0,0,35,11,1,0,0,0,36,41,1,0,0,0,37,38,
        3,2,1,0,38,39,3,14,7,0,39,41,1,0,0,0,40,36,1,0,0,0,40,37,1,0,0,0,
        41,13,1,0,0,0,42,43,1,0,0,0,43,15,1,0,0,0,2,34,40
    ]

class cfg24Parser ( Parser ):

    grammarFileName = "cfg24.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'a'", "'b'" ]

    symbolicNames = [  ]

    RULE_s = 0
    RULE_s1 = 1
    RULE_s2 = 2
    RULE_s3 = 3
    RULE_s4 = 4
    RULE_s5 = 5
    RULE_s6 = 6
    RULE_s7 = 7

    ruleNames =  [ "s", "s1", "s2", "s3", "s4", "s5", "s6", "s7" ]

    EOF = Token.EOF
    T__0=1
    T__1=2

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
            return self.getTypedRuleContext(cfg24Parser.S2Context,0)


        def getRuleIndex(self):
            return cfg24Parser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)




    def s(self):

        localctx = cfg24Parser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
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
            return cfg24Parser.RULE_s1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS1" ):
                listener.enterS1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS1" ):
                listener.exitS1(self)




    def s1(self):

        localctx = cfg24Parser.S1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_s1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(cfg24Parser.T__0)
            self.state = 19
            self.match(cfg24Parser.T__1)
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
            return self.getTypedRuleContext(cfg24Parser.S1Context,0)


        def s3(self):
            return self.getTypedRuleContext(cfg24Parser.S3Context,0)


        def getRuleIndex(self):
            return cfg24Parser.RULE_s2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS2" ):
                listener.enterS2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS2" ):
                listener.exitS2(self)




    def s2(self):

        localctx = cfg24Parser.S2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_s2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.s1()
            self.state = 22
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
            return self.getTypedRuleContext(cfg24Parser.S1Context,0)


        def s4(self):
            return self.getTypedRuleContext(cfg24Parser.S4Context,0)


        def getRuleIndex(self):
            return cfg24Parser.RULE_s3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS3" ):
                listener.enterS3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS3" ):
                listener.exitS3(self)




    def s3(self):

        localctx = cfg24Parser.S3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_s3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.s1()
            self.state = 25
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
            return self.getTypedRuleContext(cfg24Parser.S1Context,0)


        def s5(self):
            return self.getTypedRuleContext(cfg24Parser.S5Context,0)


        def getRuleIndex(self):
            return cfg24Parser.RULE_s4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS4" ):
                listener.enterS4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS4" ):
                listener.exitS4(self)




    def s4(self):

        localctx = cfg24Parser.S4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_s4)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.s1()
            self.state = 28
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
            return self.getTypedRuleContext(cfg24Parser.S1Context,0)


        def s6(self):
            return self.getTypedRuleContext(cfg24Parser.S6Context,0)


        def getRuleIndex(self):
            return cfg24Parser.RULE_s5

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS5" ):
                listener.enterS5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS5" ):
                listener.exitS5(self)




    def s5(self):

        localctx = cfg24Parser.S5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_s5)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.s1()
                self.state = 32
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

        def s1(self):
            return self.getTypedRuleContext(cfg24Parser.S1Context,0)


        def s7(self):
            return self.getTypedRuleContext(cfg24Parser.S7Context,0)


        def getRuleIndex(self):
            return cfg24Parser.RULE_s6

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS6" ):
                listener.enterS6(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS6" ):
                listener.exitS6(self)




    def s6(self):

        localctx = cfg24Parser.S6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_s6)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.s1()
                self.state = 38
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
            return cfg24Parser.RULE_s7

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS7" ):
                listener.enterS7(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS7" ):
                listener.exitS7(self)




    def s7(self):

        localctx = cfg24Parser.S7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_s7)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





