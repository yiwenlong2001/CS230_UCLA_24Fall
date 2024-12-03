# Generated from ./g4_folder/cfg10.g4 by ANTLR 4.13.2
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
        4,1,4,27,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,1,1,1,
        1,1,3,1,16,8,1,1,2,1,2,1,2,3,2,21,8,2,1,3,1,3,3,3,25,8,3,1,3,0,0,
        4,0,2,4,6,0,0,25,0,8,1,0,0,0,2,15,1,0,0,0,4,20,1,0,0,0,6,24,1,0,
        0,0,8,9,3,2,1,0,9,10,3,4,2,0,10,11,3,6,3,0,11,1,1,0,0,0,12,16,1,
        0,0,0,13,14,5,1,0,0,14,16,3,2,1,0,15,12,1,0,0,0,15,13,1,0,0,0,16,
        3,1,0,0,0,17,21,5,2,0,0,18,19,5,2,0,0,19,21,3,4,2,0,20,17,1,0,0,
        0,20,18,1,0,0,0,21,5,1,0,0,0,22,25,1,0,0,0,23,25,5,3,0,0,24,22,1,
        0,0,0,24,23,1,0,0,0,25,7,1,0,0,0,3,15,20,24
    ]

class cfg10Parser ( Parser ):

    grammarFileName = "cfg10.g4"

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

    ruleNames =  [ "s", "s1", "s2", "s3" ]

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
            return self.getTypedRuleContext(cfg10Parser.S1Context,0)


        def s2(self):
            return self.getTypedRuleContext(cfg10Parser.S2Context,0)


        def s3(self):
            return self.getTypedRuleContext(cfg10Parser.S3Context,0)


        def getRuleIndex(self):
            return cfg10Parser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)




    def s(self):

        localctx = cfg10Parser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.s1()
            self.state = 9
            self.s2()
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

        def s1(self):
            return self.getTypedRuleContext(cfg10Parser.S1Context,0)


        def getRuleIndex(self):
            return cfg10Parser.RULE_s1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS1" ):
                listener.enterS1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS1" ):
                listener.exitS1(self)




    def s1(self):

        localctx = cfg10Parser.S1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_s1)
        try:
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.match(cfg10Parser.T__0)
                self.state = 14
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


    class S2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s2(self):
            return self.getTypedRuleContext(cfg10Parser.S2Context,0)


        def getRuleIndex(self):
            return cfg10Parser.RULE_s2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS2" ):
                listener.enterS2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS2" ):
                listener.exitS2(self)




    def s2(self):

        localctx = cfg10Parser.S2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_s2)
        try:
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(cfg10Parser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(cfg10Parser.T__1)
                self.state = 19
                self.s2()
                pass


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
            return cfg10Parser.RULE_s3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS3" ):
                listener.enterS3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS3" ):
                listener.exitS3(self)




    def s3(self):

        localctx = cfg10Parser.S3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_s3)
        try:
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(cfg10Parser.T__2)
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





