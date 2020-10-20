from util.latex2sympy import *
from sympy import degree, S

def latex_exprtype_check(expr_latex):
    ''' Determine number and expression type(s) of LaTeX expression

        Usage
        >>> latex_expr_type_check($LaTeX_expression_string$)

        Example

        in :0
        out:['zero']
        in :1
        out:['Polynomial', 'AlgebraicTerm', 'ConstantTerm', 'natural']
        in :x
        out:['Polynomial', 'LinearExpression', 'AlgebraicTerm']
        in :x+y
        out:['Polynomial', 'LinearExpression']
        in :xy+1
        out:['Polynomial', 'LinearExpression']
        in :2=2
        out:[]
        in :x=y
        out:['Equation', 'LikeTerm']
    '''
    expr_type_checker = ExprType()
    num_type_checker = NumType()
    latex_converter = LatexConverter()
    expr_sympy = latex_converter.latex2sympy(expr_latex)
    list_exprtype = expr_type_checker.check(expr_sympy)
    list_numtype = num_type_checker.check(expr_sympy)
    return list_exprtype + list_numtype


class NumType:
    def __init__(self):
        self.numtype = []

    # TODO: Legacy func
    def is_float(self, num):
        try:
            judge = str(float(num))
            if judge == 'nan' or judge == 'inf' or judge == '-inf':
                return False
            else:
                self.numtype = 'real number'
                return True
        except ValueError:
            return False
    ''' Determine Sympy number type(s)

        Usage
        >>> NumType = NumType()
        >>> NumType.check(expr)

        Example

        in : 0
        out: ['zero']
        in : 1
        out: ['natural']
        in : 2
        out: ['natural', 'prime']
        in : -5
        out: ['negative_integer']
        in : -0.5
        out: ['real', 'negative']
        in : -3
        out: ['negative_integer']
    '''
    def check(self, expr): # Numtype Checker
        self.numtype = []
        if expr.is_integer:
            if self.is_zero(expr) is True:
                self.numtype.append('zero')
            elif self.is_negint(expr) is True:
                self.numtype.append('negative_integer')
            elif self.is_nat(expr) is True:
                self.numtype.append('natural')
                if self.is_prime(expr) is True:
                    self.numtype.append('prime')
        else:
            if self.is_real(expr) is True:
                self.numtype.append('real')
            if self.is_pos(expr) is True:
                self.numtype.append('positive')
            elif self.is_neg(expr) is True:
                self.numtype.append('negative')
        return self.numtype

    def is_pos(self, expr):  # 양수
        return expr.is_positive

    def is_neg(self, expr):  # 음수
        return expr.is_negative

    def is_real(self, expr): # 실수
        return expr.is_real

    def is_zero(self, expr): # 0
        return expr.is_zero

    def is_nat(self, expr): # 자연수, 양의 정수
        return expr.is_positive & expr.is_integer

    def is_negint(self, expr): # 음의 정수
        return expr.is_negative & expr.is_integer

    def is_prime(self, expr): # 소수
        return expr.is_prime


class ExprType:
    def __init__(self):
        self.expr = ''
        self.exprtype = []

    ''' Determine Sympy expression type(s)

        Usage
        >>> ExprType = ExprType()
        >>> LatexConverter = LatexConverter()
        >>> print(ExprType.check(expr))

        ExprType.check Input-Output example

        in : 0
        out: []
        in : 1
        out: ['Polynomial', 'AlgebraicTerm', 'ConstantTerm']
        in : x
        out: ['Polynomial', 'LinearExpression', 'AlgebraicTerm']
        in : xy
        out: ['Polynomial', 'AlgebraicTerm']
        in : x+1
        out: ['Polynomial', 'LinearExpression']
        in : xy+1
        out: ['Polynomial']
        in : x=y
        out: ['Equation', 'LikeTerm']
        in : 2=2
        out: []
        in : x=2
        out: ['Equation', 'LikeTerm']
    '''
    def check(self, expr): # former name of function : ExprType
        self.exprtype = []
        if expr.is_Boolean:
            pass
        else:
            if self.like_term(expr) is True:
                if self.equation(expr) is True:
                    self.exprtype.append('Equation')
                self.exprtype.append('LikeTerm')
            elif self.polynomial(expr) is True:
                self.exprtype.append('Polynomial')
                if self.linear_expression(expr) is True:
                    self.exprtype.append('LinearExpression')
                if self.algebraic_term(expr) is True:
                    self.exprtype.append('AlgebraicTerm')
                    if self.constant_term(expr) is True:
                        self.exprtype.append('ConstantTerm')
        # elif self.Expression(expr) is False:
        #     self.exprtype.append('NotExpression')
        return self.exprtype

    def equation(self, expr): # 방정식
        return isinstance(expr, sympy.Equality)

    # def Expression(self, expr): # 식
    #     if isinstance(expr, sympy.logic.boolal):
    #         return False
    #     return True

    def linear_expression(self, expr): # 일차식
        var_list = list(expr.free_symbols)
        deg = 0
        for variable in var_list:
            deg = max(deg, degree(expr, variable))
        if deg is S.One and self.polynomial(expr):
            return True
        return False

    def polynomial(self, expr): # 다항식
        _const, _expr = expr.expand().as_coeff_add()
        if isinstance(expr, sympy.Equality):
            return False
        elif _const == 0 and len(_expr) == 0:
            return False
        return True

    def algebraic_term(self, expr): # 항, 단항식
        _const, _expr = expr.expand().as_coeff_add()
        if isinstance(expr, sympy.Equality):
            return False
        elif (_const == 0 and len(_expr) == 0) or (_const == 0 and len(_expr) > 1):
            return False
        return True

    def like_term(self, expr): # 등식
        return isinstance(expr, sympy.Equality)

    def constant_term(self, expr): # 상수항 = 상수 ^ 항
        # bnf version
        if expr['data']['expr_type'] == 'constant' and expr['data']['expr'] != '0':
            return True
        else:
            return False
        # end of bnf version

    # sympy version
        # if expr.is_constant(): # 상수
        #     if self.algebraic_term(expr): # 항
        #         return True # 상수 ^ 항
        # return False
    # end of sympy version

####### test

# ExprType = ExprType()
# NumType = NumType()
# LatexConverter = LatexConverter()
# while True:
#     expr = input('in : ')
#     expr = LatexConverter.latex2sympy(expr)
#     # print(type(expr))
#     # print('out: ' + str(ExprType.check(expr)))
#     print('out: ' + str(NumType.check(expr)))

# while True:
#     a = input('in :')
#     print(latex_expr_type_check(a))
