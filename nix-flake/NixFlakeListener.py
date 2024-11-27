# vim: set fileencoding=utf-8
# Generated from NixFlake.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .NixFlakeParser import NixFlakeParser
else:
    from NixFlakeParser import NixFlakeParser

# This class defines a complete listener for a parse tree produced by NixFlakeParser.
class NixFlakeListener(ParseTreeListener):

    # Enter a parse tree produced by NixFlakeParser#flake.
    def enterFlake(self, ctx:NixFlakeParser.FlakeContext):
        pass

    # Exit a parse tree produced by NixFlakeParser#flake.
    def exitFlake(self, ctx:NixFlakeParser.FlakeContext):
        pass


    # Enter a parse tree produced by NixFlakeParser#description.
    def enterDescription(self, ctx:NixFlakeParser.DescriptionContext):
        pass

    # Exit a parse tree produced by NixFlakeParser#description.
    def exitDescription(self, ctx:NixFlakeParser.DescriptionContext):
        pass


    # Enter a parse tree produced by NixFlakeParser#inputs.
    def enterInputs(self, ctx:NixFlakeParser.InputsContext):
        pass

    # Exit a parse tree produced by NixFlakeParser#inputs.
    def exitInputs(self, ctx:NixFlakeParser.InputsContext):
        pass


    # Enter a parse tree produced by NixFlakeParser#input.
    def enterInput(self, ctx:NixFlakeParser.InputContext):
        pass

    # Exit a parse tree produced by NixFlakeParser#input.
    def exitInput(self, ctx:NixFlakeParser.InputContext):
        pass


    # Enter a parse tree produced by NixFlakeParser#input_url_assignment.
    def enterInput_url_assignment(self, ctx:NixFlakeParser.Input_url_assignmentContext):
        pass

    # Exit a parse tree produced by NixFlakeParser#input_url_assignment.
    def exitInput_url_assignment(self, ctx:NixFlakeParser.Input_url_assignmentContext):
        pass


    # Enter a parse tree produced by NixFlakeParser#input_obj.
    def enterInput_obj(self, ctx:NixFlakeParser.Input_objContext):
        pass

    # Exit a parse tree produced by NixFlakeParser#input_obj.
    def exitInput_obj(self, ctx:NixFlakeParser.Input_objContext):
        pass


    # Enter a parse tree produced by NixFlakeParser#input_pin.
    def enterInput_pin(self, ctx:NixFlakeParser.Input_pinContext):
        pass

    # Exit a parse tree produced by NixFlakeParser#input_pin.
    def exitInput_pin(self, ctx:NixFlakeParser.Input_pinContext):
        pass


    # Enter a parse tree produced by NixFlakeParser#url.
    def enterUrl(self, ctx:NixFlakeParser.UrlContext):
        pass

    # Exit a parse tree produced by NixFlakeParser#url.
    def exitUrl(self, ctx:NixFlakeParser.UrlContext):
        pass



del NixFlakeParser