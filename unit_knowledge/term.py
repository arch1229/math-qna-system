from unit_knowledge.unit_knowledge import *
from util.type_checker import NumType, ExprType
# from util.math_util import *

logger = logging.getLogger("inference_engine")

class AlgebraicTerm(UnitKnowledge):
    #class variable
    # normal_form = DB['AlgebraicTerm']['NormalForm']

    def __init__(self):
        self.out = {}

    def logic(self, expression):
        exprtype = ExprType()
        if exprtype.algebraic_term(expression) is True:
            query_result = {"result_type": "inference_success", "message": "true"}
        else:
            query_result = {"result_type": "inference_success", "message": "false"}
        return query_result


class LikeTerm(AlgebraicTerm):
    pass
    # def __init__(self,x,y):
    #     self.logic = 0
    #     self.x = x
    #     self.y = y
    #     if AlgebraicTerm(self.x).logic:
    #         if AlgebraicTerm(self.y).logic:
    #             if self.x["expr_type"] == "finite_product" and self.x["expr_n"] == 2:
    #                 self.x = self.x["expr_elem"][1] # 계수x문자 -> 문자만 분리
    #             if self.y["expr_type"] == "finite_product" and self.x["expr_n"] == 2:
    #                 self.y = self.y["expr_elem"][1] # 계수x문자 -> 문자만 분리
    #
    #             if self.x["expr_type"] == "constant" and self.y["expr_type"] == "constant":
    #                 self.logic = 1 # 상수항 끼리는 항상 동류항
    #             elif self.x["expr"] == self.y["expr"]:
    #                 self.logic = 1 # var = var. 계수 제외한 문자가 둘 다 1차항
    #             else:
    #                 if self.x["expr_type"] == "exponential" and self.y["expr_type"] == "exponential":
    #                     if self.x["expr_elem"][0]["expr"] == self.y["expr_elem"][0]["expr"]: # var = var
    #                         if self.x["expr_elem"][1]["expr"] == self.y["expr_elem"][1]["expr"]: # power = power
    #                             self.logic = 1


    # def action(expression, input_term):
    #     result = []
    #     for term in expression_to_term(expression):
    #         if LikeTerm(input_term, term).logic:
    #             result.append(term)
    #     return result



class DegreeOfTerm(AlgebraicTerm):
    pass
    # def __init__(self,x,y):
    #     self.logic = 0
    #     self.x = x
    #     self.y = y
    #     if AlgebraicTerm(self.x).logic:
    #         if x["expr_type"] == "constant" and y == 0:
    #             self.logic = 1
    #         else:
    #             if self.x["expr_type"] == "finite_product" and self.x["expr_n"] == 2:
    #                 self.x = self.x["expr_elem"][1] # 계수x문자 -> 문자만 분리
    #             for term in x["expr_elem"]: # x, x^2, 5^x
    #                 if term["expr_type"] == "variable" and y == 1: # x
    #                     self.logic = 1
    #                 elif term["expr_type"] == "exponential":
    #                     if term["expr_elem"][0]["expr_type"] == "constant" and y == 0: # 5^x
    #                         self.logic = 1
    #                     elif term["expr_elem"][0]["expr_type"] == "variable" and y == term["expr_elem"][1]["expr"]: # x^2
    #                         self.logic = 1
    #     pass


class ConstantTerm(AlgebraicTerm):
    def __init__(self):
        self.out = {}
        # self.logic = 0
        # self.expression = expression
        # if AlgebraicTerm(self.expression).logic:
        #     if self.expression["expr_type"] == "constant":
        #         if self.expression["expr"] != "0":
        #             self.logic = 1

    # def action(expression):
    #     for term in expression_to_term(expression["expr"]):
    #         term_json = expression2json(term)
    #         if ConstantTerm(term_json).logic:
    #             return term

    def logic(self, expression):
        exprtype = ExprType()
        logger.debug("------ConstantTerm.logic-----------")
        logger.debug(expression)
        if exprtype.constant_term(expression) is True:
            query_result = {"result_type": "inference_success", "message": "true"}
        else:
            query_result = {"result_type": "inference_success", "message": "false"}
        return query_result


class SimilarTerm(AlgebraicTerm):
    pass

# TODO: ValueOfAlgebraicTerm -> ValueOfAlgebraicExpreesion
class ValueOfAlgebraicExpreesion(UnitKnowledge):
    pass

# TODO: IdentityTerm -> IdentityEquation
class IdentityEquation(AlgebraicTerm):
    pass


# expr_dict_test = expression2json('0')
# ConstantTerm = ConstantTerm()
# test = ConstantTerm.logic(expr_dict_test)
# print(test)
# print(type(test))
