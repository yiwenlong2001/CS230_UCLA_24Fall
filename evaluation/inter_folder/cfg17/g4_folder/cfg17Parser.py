# Generated from ./g4_folder/cfg17.g4 by ANTLR 4.13.2
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
        4,1,6,23,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,
        3,1,15,8,1,1,2,1,2,1,2,1,2,3,2,21,8,2,1,2,0,0,3,0,2,4,0,0,21,0,6,
        1,0,0,0,2,14,1,0,0,0,4,20,1,0,0,0,6,7,5,1,0,0,7,8,3,4,2,0,8,9,5,
        2,0,0,9,1,1,0,0,0,10,11,5,3,0,0,11,15,5,4,0,0,12,13,5,5,0,0,13,15,
        5,6,0,0,14,10,1,0,0,0,14,12,1,0,0,0,15,3,1,0,0,0,16,21,1,0,0,0,17,
        18,3,2,1,0,18,19,3,4,2,0,19,21,1,0,0,0,20,16,1,0,0,0,20,17,1,0,0,
        0,21,5,1,0,0,0,2,14,20
    ]

class cfg17Parser ( Parser ):

    grammarFileName = "cfg17.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'a'", "'f'", "'b'", "'c'", "'d'", "'e'" ]

    symbolicNames = [  ]

    RULE_s = 0
    RULE_s1 = 1
    RULE_s3 = 2

    ruleNames =  [ "s", "s1", "s3" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6

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
            return self.getTypedRuleContext(cfg17Parser.S3Context,0)


        def getRuleIndex(self):
            return cfg17Parser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)




    def s(self):

        localctx = cfg17Parser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(cfg17Parser.T__0)
            self.state = 7
            self.s3()
            self.state = 8
            self.match(cfg17Parser.T__1)
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
            return cfg17Parser.RULE_s1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS1" ):
                listener.enterS1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS1" ):
                listener.exitS1(self)




    def s1(self):

        localctx = cfg17Parser.S1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_s1)
        try:
            self.state = 14
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.match(cfg17Parser.T__2)
                self.state = 11
                self.match(cfg17Parser.T__3)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 12
                self.match(cfg17Parser.T__4)
                self.state = 13
                self.match(cfg17Parser.T__5)
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
            return self.getTypedRuleContext(cfg17Parser.S1Context,0)


        def s3(self):
            return self.getTypedRuleContext(cfg17Parser.S3Context,0)


        def getRuleIndex(self):
            return cfg17Parser.RULE_s3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS3" ):
                listener.enterS3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS3" ):
                listener.exitS3(self)




    def s3(self):

        localctx = cfg17Parser.S3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_s3)
        try:
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [3, 5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.s1()
                self.state = 18
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





