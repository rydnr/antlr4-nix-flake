# vim: set fileencoding=utf-8
# Generated from NixFlake.g4 by ANTLR 4.13.0
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
        4,1,16,84,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,3,0,19,8,0,1,0,3,0,22,8,0,1,0,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,2,1,2,1,2,3,2,35,8,2,1,2,1,2,4,2,39,8,2,11,2,12,2,
        40,1,2,1,2,1,2,1,3,1,3,3,3,48,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        5,1,5,1,5,1,5,5,5,61,8,5,10,5,12,5,64,9,5,1,5,1,5,1,5,1,5,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,0,0,8,0,2,
        4,6,8,10,12,14,0,0,81,0,16,1,0,0,0,2,26,1,0,0,0,4,31,1,0,0,0,6,47,
        1,0,0,0,8,49,1,0,0,0,10,56,1,0,0,0,12,69,1,0,0,0,14,78,1,0,0,0,16,
        18,5,9,0,0,17,19,3,2,1,0,18,17,1,0,0,0,18,19,1,0,0,0,19,21,1,0,0,
        0,20,22,3,4,2,0,21,20,1,0,0,0,21,22,1,0,0,0,22,23,1,0,0,0,23,24,
        5,10,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,27,5,2,0,0,27,28,5,11,0,0,
        28,29,5,7,0,0,29,30,5,12,0,0,30,3,1,0,0,0,31,32,5,3,0,0,32,34,5,
        11,0,0,33,35,5,5,0,0,34,33,1,0,0,0,34,35,1,0,0,0,35,36,1,0,0,0,36,
        38,5,9,0,0,37,39,3,6,3,0,38,37,1,0,0,0,39,40,1,0,0,0,40,38,1,0,0,
        0,40,41,1,0,0,0,41,42,1,0,0,0,42,43,5,10,0,0,43,44,5,12,0,0,44,5,
        1,0,0,0,45,48,3,8,4,0,46,48,3,10,5,0,47,45,1,0,0,0,47,46,1,0,0,0,
        48,7,1,0,0,0,49,50,5,15,0,0,50,51,5,13,0,0,51,52,5,6,0,0,52,53,5,
        11,0,0,53,54,5,7,0,0,54,55,5,12,0,0,55,9,1,0,0,0,56,57,5,15,0,0,
        57,58,5,11,0,0,58,62,5,9,0,0,59,61,3,12,6,0,60,59,1,0,0,0,61,64,
        1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,65,1,0,0,0,64,62,1,0,0,0,
        65,66,3,14,7,0,66,67,5,10,0,0,67,68,5,12,0,0,68,11,1,0,0,0,69,70,
        5,3,0,0,70,71,5,13,0,0,71,72,5,15,0,0,72,73,5,13,0,0,73,74,5,4,0,
        0,74,75,5,11,0,0,75,76,5,7,0,0,76,77,5,12,0,0,77,13,1,0,0,0,78,79,
        5,6,0,0,79,80,5,11,0,0,80,81,5,7,0,0,81,82,5,12,0,0,82,15,1,0,0,
        0,6,18,21,34,40,47,62
    ]

class NixFlakeParser ( Parser ):

    grammarFileName = "NixFlake.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'description'", "'inputs'", 
                     "'follows'", "'rec'", "'url'", "<INVALID>", "<INVALID>", 
                     "'{'", "'}'", "'='", "';'", "'.'" ]

    symbolicNames = [ "<INVALID>", "SINGLE_LINE_COMMENT", "DESCRIPTION_LITERAL", 
                      "INPUTS_LITERAL", "FOLLOWS_LITERAL", "REC_LITERAL", 
                      "URL_LITERAL", "STRING", "NUMBER", "LCURLY", "RCURLY", 
                      "EQUAL", "SEMI", "DOT", "SYMBOL", "IDENTIFIER", "WS" ]

    RULE_flake = 0
    RULE_description = 1
    RULE_inputs = 2
    RULE_input = 3
    RULE_input_url_assignment = 4
    RULE_input_obj = 5
    RULE_input_pin = 6
    RULE_url = 7

    ruleNames =  [ "flake", "description", "inputs", "input", "input_url_assignment", 
                   "input_obj", "input_pin", "url" ]

    EOF = Token.EOF
    SINGLE_LINE_COMMENT=1
    DESCRIPTION_LITERAL=2
    INPUTS_LITERAL=3
    FOLLOWS_LITERAL=4
    REC_LITERAL=5
    URL_LITERAL=6
    STRING=7
    NUMBER=8
    LCURLY=9
    RCURLY=10
    EQUAL=11
    SEMI=12
    DOT=13
    SYMBOL=14
    IDENTIFIER=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FlakeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCURLY(self):
            return self.getToken(NixFlakeParser.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(NixFlakeParser.RCURLY, 0)

        def EOF(self):
            return self.getToken(NixFlakeParser.EOF, 0)

        def description(self):
            return self.getTypedRuleContext(NixFlakeParser.DescriptionContext,0)


        def inputs(self):
            return self.getTypedRuleContext(NixFlakeParser.InputsContext,0)


        def getRuleIndex(self):
            return NixFlakeParser.RULE_flake

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlake" ):
                listener.enterFlake(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlake" ):
                listener.exitFlake(self)




    def flake(self):

        localctx = NixFlakeParser.FlakeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_flake)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(NixFlakeParser.LCURLY)
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 17
                self.description()


            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 20
                self.inputs()


            self.state = 23
            self.match(NixFlakeParser.RCURLY)
            self.state = 24
            self.match(NixFlakeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DescriptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESCRIPTION_LITERAL(self):
            return self.getToken(NixFlakeParser.DESCRIPTION_LITERAL, 0)

        def EQUAL(self):
            return self.getToken(NixFlakeParser.EQUAL, 0)

        def STRING(self):
            return self.getToken(NixFlakeParser.STRING, 0)

        def SEMI(self):
            return self.getToken(NixFlakeParser.SEMI, 0)

        def getRuleIndex(self):
            return NixFlakeParser.RULE_description

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDescription" ):
                listener.enterDescription(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDescription" ):
                listener.exitDescription(self)




    def description(self):

        localctx = NixFlakeParser.DescriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_description)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(NixFlakeParser.DESCRIPTION_LITERAL)
            self.state = 27
            self.match(NixFlakeParser.EQUAL)
            self.state = 28
            self.match(NixFlakeParser.STRING)
            self.state = 29
            self.match(NixFlakeParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUTS_LITERAL(self):
            return self.getToken(NixFlakeParser.INPUTS_LITERAL, 0)

        def EQUAL(self):
            return self.getToken(NixFlakeParser.EQUAL, 0)

        def LCURLY(self):
            return self.getToken(NixFlakeParser.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(NixFlakeParser.RCURLY, 0)

        def SEMI(self):
            return self.getToken(NixFlakeParser.SEMI, 0)

        def REC_LITERAL(self):
            return self.getToken(NixFlakeParser.REC_LITERAL, 0)

        def input_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NixFlakeParser.InputContext)
            else:
                return self.getTypedRuleContext(NixFlakeParser.InputContext,i)


        def getRuleIndex(self):
            return NixFlakeParser.RULE_inputs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputs" ):
                listener.enterInputs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputs" ):
                listener.exitInputs(self)




    def inputs(self):

        localctx = NixFlakeParser.InputsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_inputs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(NixFlakeParser.INPUTS_LITERAL)
            self.state = 32
            self.match(NixFlakeParser.EQUAL)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 33
                self.match(NixFlakeParser.REC_LITERAL)


            self.state = 36
            self.match(NixFlakeParser.LCURLY)
            self.state = 38 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 37
                self.input_()
                self.state = 40 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==15):
                    break

            self.state = 42
            self.match(NixFlakeParser.RCURLY)
            self.state = 43
            self.match(NixFlakeParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def input_url_assignment(self):
            return self.getTypedRuleContext(NixFlakeParser.Input_url_assignmentContext,0)


        def input_obj(self):
            return self.getTypedRuleContext(NixFlakeParser.Input_objContext,0)


        def getRuleIndex(self):
            return NixFlakeParser.RULE_input

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput" ):
                listener.enterInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput" ):
                listener.exitInput(self)




    def input_(self):

        localctx = NixFlakeParser.InputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_input)
        try:
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.input_url_assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.input_obj()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Input_url_assignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(NixFlakeParser.IDENTIFIER, 0)

        def DOT(self):
            return self.getToken(NixFlakeParser.DOT, 0)

        def URL_LITERAL(self):
            return self.getToken(NixFlakeParser.URL_LITERAL, 0)

        def EQUAL(self):
            return self.getToken(NixFlakeParser.EQUAL, 0)

        def STRING(self):
            return self.getToken(NixFlakeParser.STRING, 0)

        def SEMI(self):
            return self.getToken(NixFlakeParser.SEMI, 0)

        def getRuleIndex(self):
            return NixFlakeParser.RULE_input_url_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput_url_assignment" ):
                listener.enterInput_url_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput_url_assignment" ):
                listener.exitInput_url_assignment(self)




    def input_url_assignment(self):

        localctx = NixFlakeParser.Input_url_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_input_url_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(NixFlakeParser.IDENTIFIER)
            self.state = 50
            self.match(NixFlakeParser.DOT)
            self.state = 51
            self.match(NixFlakeParser.URL_LITERAL)
            self.state = 52
            self.match(NixFlakeParser.EQUAL)
            self.state = 53
            self.match(NixFlakeParser.STRING)
            self.state = 54
            self.match(NixFlakeParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Input_objContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(NixFlakeParser.IDENTIFIER, 0)

        def EQUAL(self):
            return self.getToken(NixFlakeParser.EQUAL, 0)

        def LCURLY(self):
            return self.getToken(NixFlakeParser.LCURLY, 0)

        def url(self):
            return self.getTypedRuleContext(NixFlakeParser.UrlContext,0)


        def RCURLY(self):
            return self.getToken(NixFlakeParser.RCURLY, 0)

        def SEMI(self):
            return self.getToken(NixFlakeParser.SEMI, 0)

        def input_pin(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NixFlakeParser.Input_pinContext)
            else:
                return self.getTypedRuleContext(NixFlakeParser.Input_pinContext,i)


        def getRuleIndex(self):
            return NixFlakeParser.RULE_input_obj

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput_obj" ):
                listener.enterInput_obj(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput_obj" ):
                listener.exitInput_obj(self)




    def input_obj(self):

        localctx = NixFlakeParser.Input_objContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_input_obj)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(NixFlakeParser.IDENTIFIER)
            self.state = 57
            self.match(NixFlakeParser.EQUAL)
            self.state = 58
            self.match(NixFlakeParser.LCURLY)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 59
                self.input_pin()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self.url()
            self.state = 66
            self.match(NixFlakeParser.RCURLY)
            self.state = 67
            self.match(NixFlakeParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Input_pinContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUTS_LITERAL(self):
            return self.getToken(NixFlakeParser.INPUTS_LITERAL, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(NixFlakeParser.DOT)
            else:
                return self.getToken(NixFlakeParser.DOT, i)

        def IDENTIFIER(self):
            return self.getToken(NixFlakeParser.IDENTIFIER, 0)

        def FOLLOWS_LITERAL(self):
            return self.getToken(NixFlakeParser.FOLLOWS_LITERAL, 0)

        def EQUAL(self):
            return self.getToken(NixFlakeParser.EQUAL, 0)

        def STRING(self):
            return self.getToken(NixFlakeParser.STRING, 0)

        def SEMI(self):
            return self.getToken(NixFlakeParser.SEMI, 0)

        def getRuleIndex(self):
            return NixFlakeParser.RULE_input_pin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput_pin" ):
                listener.enterInput_pin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput_pin" ):
                listener.exitInput_pin(self)




    def input_pin(self):

        localctx = NixFlakeParser.Input_pinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_input_pin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(NixFlakeParser.INPUTS_LITERAL)
            self.state = 70
            self.match(NixFlakeParser.DOT)
            self.state = 71
            self.match(NixFlakeParser.IDENTIFIER)
            self.state = 72
            self.match(NixFlakeParser.DOT)
            self.state = 73
            self.match(NixFlakeParser.FOLLOWS_LITERAL)
            self.state = 74
            self.match(NixFlakeParser.EQUAL)
            self.state = 75
            self.match(NixFlakeParser.STRING)
            self.state = 76
            self.match(NixFlakeParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UrlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def URL_LITERAL(self):
            return self.getToken(NixFlakeParser.URL_LITERAL, 0)

        def EQUAL(self):
            return self.getToken(NixFlakeParser.EQUAL, 0)

        def STRING(self):
            return self.getToken(NixFlakeParser.STRING, 0)

        def SEMI(self):
            return self.getToken(NixFlakeParser.SEMI, 0)

        def getRuleIndex(self):
            return NixFlakeParser.RULE_url

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUrl" ):
                listener.enterUrl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUrl" ):
                listener.exitUrl(self)




    def url(self):

        localctx = NixFlakeParser.UrlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_url)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(NixFlakeParser.URL_LITERAL)
            self.state = 79
            self.match(NixFlakeParser.EQUAL)
            self.state = 80
            self.match(NixFlakeParser.STRING)
            self.state = 81
            self.match(NixFlakeParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





