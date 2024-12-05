# Generated from ./g4_folder/cfg5.g4 by ANTLR 4.13.2
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
        4,1,3,22,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,1,1,1,1,1,1,2,
        1,2,1,3,1,3,1,3,1,3,3,3,20,8,3,1,3,0,0,4,0,2,4,6,0,1,1,0,2,3,18,
        0,8,1,0,0,0,2,10,1,0,0,0,4,13,1,0,0,0,6,19,1,0,0,0,8,9,3,6,3,0,9,
        1,1,0,0,0,10,11,5,1,0,0,11,12,3,4,2,0,12,3,1,0,0,0,13,14,7,0,0,0,
        14,5,1,0,0,0,15,20,1,0,0,0,16,17,3,2,1,0,17,18,3,6,3,0,18,20,1,0,
        0,0,19,15,1,0,0,0,19,16,1,0,0,0,20,7,1,0,0,0,1,19
    ]

class cfg5Parser ( Parser ):

    grammarFileName = "cfg5.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'a'", "'b'", "'c'" ]

    symbolicNames = [  ]

    RULE_s = 0
    RULE_s1 = 1
    RULE_s3 = 2
    RULE_s4 = 3

    ruleNames =  [ "s", "s1", "s3", "s4" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3

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

        def s4(self):
            return self.getTypedRuleContext(cfg5Parser.S4Context,0)


        def getRuleIndex(self):
            return cfg5Parser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)




    def s(self):

        localctx = cfg5Parser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.s4()
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

        def s3(self):
            return self.getTypedRuleContext(cfg5Parser.S3Context,0)


        def getRuleIndex(self):
            return cfg5Parser.RULE_s1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS1" ):
                listener.enterS1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS1" ):
                listener.exitS1(self)




    def s1(self):

        localctx = cfg5Parser.S1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_s1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(cfg5Parser.T__0)
            self.state = 11
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


        def getRuleIndex(self):
            return cfg5Parser.RULE_s3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS3" ):
                listener.enterS3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS3" ):
                listener.exitS3(self)




    def s3(self):

        localctx = cfg5Parser.S3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_s3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
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


    class S4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s1(self):
            return self.getTypedRuleContext(cfg5Parser.S1Context,0)


        def s4(self):
            return self.getTypedRuleContext(cfg5Parser.S4Context,0)


        def getRuleIndex(self):
            return cfg5Parser.RULE_s4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS4" ):
                listener.enterS4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS4" ):
                listener.exitS4(self)




    def s4(self):

        localctx = cfg5Parser.S4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_s4)
        try:
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.s1()
                self.state = 17
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





