# Generated from Grammar/PyLogic3.g4 by ANTLR 4.7
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by PyLogic3Parser.

class PyLogic3Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by PyLogic3Parser#single_input.
    def visitSingle_input(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#file_input.
    def visitFile_input(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#eval_input.
    def visitEval_input(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#decorator.
    def visitDecorator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#decorators.
    def visitDecorators(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#decorated.
    def visitDecorated(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#funcdef.
    def visitFuncdef(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#parameters.
    def visitParameters(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#typedargslist.
    def visitTypedargslist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#tfpdef.
    def visitTfpdef(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#varargslist.
    def visitVarargslist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#vfpdef.
    def visitVfpdef(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#stmt.
    def visitStmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#simple_stmt.
    def visitSimple_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#small_stmt.
    def visitSmall_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#expr_stmt.
    def visitExpr_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#testlist_star_expr.
    def visitTestlist_star_expr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#augassign.
    def visitAugassign(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#del_stmt.
    def visitDel_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#pass_stmt.
    def visitPass_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#flow_stmt.
    def visitFlow_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#break_stmt.
    def visitBreak_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#continue_stmt.
    def visitContinue_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#return_stmt.
    def visitReturn_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#yield_stmt.
    def visitYield_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#raise_stmt.
    def visitRaise_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#import_stmt.
    def visitImport_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#import_name.
    def visitImport_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#import_from.
    def visitImport_from(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#import_as_name.
    def visitImport_as_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#dotted_as_name.
    def visitDotted_as_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#import_as_names.
    def visitImport_as_names(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#dotted_as_names.
    def visitDotted_as_names(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#dotted_name.
    def visitDotted_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#global_stmt.
    def visitGlobal_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#nonlocal_stmt.
    def visitNonlocal_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#assert_stmt.
    def visitAssert_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#compound_stmt.
    def visitCompound_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#if_stmt.
    def visitIf_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#while_stmt.
    def visitWhile_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#for_stmt.
    def visitFor_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#try_stmt.
    def visitTry_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#with_stmt.
    def visitWith_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#with_item.
    def visitWith_item(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#except_clause.
    def visitExcept_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#suite.
    def visitSuite(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#test.
    def visitTest(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#test_nocond.
    def visitTest_nocond(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#lambdef.
    def visitLambdef(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#lambdef_nocond.
    def visitLambdef_nocond(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#or_test.
    def visitOr_test(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#and_test.
    def visitAnd_test(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#not_test.
    def visitNot_test(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#comparison.
    def visitComparison(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#comp_op.
    def visitComp_op(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#star_expr.
    def visitStar_expr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#expr.
    def visitExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#xor_expr.
    def visitXor_expr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#and_expr.
    def visitAnd_expr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#shift_expr.
    def visitShift_expr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#arith_expr.
    def visitArith_expr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#term.
    def visitTerm(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#factor.
    def visitFactor(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#power.
    def visitPower(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#atom.
    def visitAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#testlist_comp.
    def visitTestlist_comp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#trailer.
    def visitTrailer(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#subscriptlist.
    def visitSubscriptlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#subscript.
    def visitSubscript(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#sliceop.
    def visitSliceop(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#exprlist.
    def visitExprlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#testlist.
    def visitTestlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#dictorsetmaker.
    def visitDictorsetmaker(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#classdef.
    def visitClassdef(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#arglist.
    def visitArglist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#argument.
    def visitArgument(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#comp_iter.
    def visitComp_iter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#comp_for.
    def visitComp_for(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#comp_if.
    def visitComp_if(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#yield_expr.
    def visitYield_expr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#yield_arg.
    def visitYield_arg(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#strr.
    def visitStrr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#number.
    def visitNumber(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyLogic3Parser#integer.
    def visitInteger(self, ctx):
        return self.visitChildren(ctx)


