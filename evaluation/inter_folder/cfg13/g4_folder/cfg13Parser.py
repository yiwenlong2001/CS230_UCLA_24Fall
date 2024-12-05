# Generated from ./g4_folder/cfg13.g4 by ANTLR 4.13.2
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
        4,1,1,28,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,1,1,1,
        1,1,1,2,1,2,1,2,3,2,19,8,2,1,3,1,3,1,3,3,3,24,8,3,1,4,1,4,1,4,0,
        0,5,0,2,4,6,8,0,0,24,0,10,1,0,0,0,2,12,1,0,0,0,4,18,1,0,0,0,6,23,
        1,0,0,0,8,25,1,0,0,0,10,11,3,2,1,0,11,1,1,0,0,0,12,13,5,1,0,0,13,
        14,3,4,2,0,14,3,1,0,0,0,15,19,1,0,0,0,16,17,5,1,0,0,17,19,3,6,3,
        0,18,15,1,0,0,0,18,16,1,0,0,0,19,5,1,0,0,0,20,24,1,0,0,0,21,22,5,
        1,0,0,22,24,3,8,4,0,23,20,1,0,0,0,23,21,1,0,0,0,24,7,1,0,0,0,25,
        26,1,0,0,0,26,9,1,0,0,0,2,18,23
    ]

class cfg13Parser ( Parser ):

    grammarFileName = "cfg13.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'c'" ]

    symbolicNames = [  ]

    RULE_s = 0
    RULE_s1 = 1
    RULE_s2 = 2
    RULE_s3 = 3
    RULE_s4 = 4

    ruleNames =  [ "s", "s1", "s2", "s3", "s4" ]

    EOF = Token.EOF
    T__0=1

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
            return self.getTypedRuleContext(cfg13Parser.S1Context,0)


        def getRuleIndex(self):
            return cfg13Parser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)




    def s(self):

        localctx = cfg13Parser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
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

        def s2(self):
            return self.getTypedRuleContext(cfg13Parser.S2Context,0)


        def getRuleIndex(self):
            return cfg13Parser.RULE_s1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS1" ):
                listener.enterS1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS1" ):
                listener.exitS1(self)




    def s1(self):

        localctx = cfg13Parser.S1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_s1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(cfg13Parser.T__0)
            self.state = 13
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
            return self.getTypedRuleContext(cfg13Parser.S3Context,0)


        def getRuleIndex(self):
            return cfg13Parser.RULE_s2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS2" ):
                listener.enterS2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS2" ):
                listener.exitS2(self)




    def s2(self):

        localctx = cfg13Parser.S2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_s2)
        try:
            self.state = 18
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(cfg13Parser.T__0)
                self.state = 17
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

        def s4(self):
            return self.getTypedRuleContext(cfg13Parser.S4Context,0)


        def getRuleIndex(self):
            return cfg13Parser.RULE_s3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS3" ):
                listener.enterS3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS3" ):
                listener.exitS3(self)




    def s3(self):

        localctx = cfg13Parser.S3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_s3)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.match(cfg13Parser.T__0)
                self.state = 22
                self.s4()
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


    class S4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cfg13Parser.RULE_s4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS4" ):
                listener.enterS4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS4" ):
                listener.exitS4(self)




    def s4(self):

        localctx = cfg13Parser.S4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_s4)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





