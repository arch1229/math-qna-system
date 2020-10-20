from unit_knowledge.unit_knowledge import *
from sympy import symbols 


class Expression(UnitKnowledge):
    pass

class LinearExpression(Expression):
    # normal_form = DB['LinearExpression']['NormalForm']
    pass
    # def __init__(self,expression):
    #     self.logic = 0
    #     self.expression = expression
    #     if PolynomialExpression(self.expression).logic:
    #         if DegreeOfPolynomial.action(self.expression) == 1:
    #             self.logic = 1

class Monomial(Expression):
    # normal_form = DB['MonomialExpression']['NormalForm']
    pass    
    # def __init__(self,expression):
    #     self.logic = 0
    #     self.expression = expression
    #     # 단항식은 항과 같은 logic으로 판단하여 더이상 진행 X

class Polynomial(Expression):
    # normal_form = DB['PolynomialExpression']['NormalForm'] # 항+
    pass    
    # def __init__(self,expression):
    #     self.logic = 1
    #     self.expression = expression
    #     for term in expression_to_term(expression):
    #         self.logic &= AlgebraicTerm(term).logic

class Substitution(UnitKnowledge):
    
    # TODO: 아래의 정보를 DB에서 불러오기!
    def __init__(self):
        super().__init__()
        self.proper_lenth_of_elements = 3
        self.proper_type_of_elements = [
            ['finite_addition'],
            ['variable'],
            ['constant']
        ]
        
        
class Coefficient(UnitKnowledge):
    # TODO: 이 UK도 마찬가지 
    def __init__(self):
        super().__init__()
        self.proper_lenth_of_elements = 2
        self.proper_type_of_elements = [
            ['finite_addition'],
            ['variable']
        ]
    # normal_form = DB['Coefficient']['NormalForm'] # 0이 아닌 수
    pass
    # def action(expression, variable):
    #     expression = simplify(expression)
    #     for term in expression_to_term(expression):
    #         if AlgebraicTerm(term).logic:
    #             if Coefficient(term).logic:
    #                 pass
                    # term 에서 input variable을 제외한 나머지를 반환

class Degree(UnitKnowledge):
    pass
    # def __init__(self,expression):
    #     self.logic = 0
    #     self.expression = expression
    #     if PolynomialExpression(self.expression).logic:
    #         self.logic = 1
    
    # def action(expression):
    #     if DegreeOfPolynomial(expression).logic:
    #         result = 0
    #         for variable in variable_in_expression(expression):
    #             for term in expression_to_term(expression,variable):
    #                 result = max(result, DegreeOfTerm.action(term))
    #         return result
