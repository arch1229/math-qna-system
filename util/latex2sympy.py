import logging
from sympy.parsing.latex import parse_latex
# from sympy.core.sympify import SympifyError
from sympy.parsing.latex.errors import LaTeXParsingError
import sympy
import antlr4  # 4.7.1

LOGGING_LEVEL = logging.DEBUG
logger = logging.getLogger('inference_engine/latex2sympy')
logger.setLevel(LOGGING_LEVEL)
stream_hander = logging.StreamHandler()
logger.addHandler(stream_hander)


class LatexConverter:
    def __init__(self):
        pass

    ''' Convert Latex String into Sympy expression

        Usage
        >>> LatexConverter = LatexConverter()
        >>> sympy_expr = LatexConverter.latex2sympy(input_latex_expr)
    '''
    def latex2sympy(self, latex):
        expression = latex.replace('$', '')  # remove LaTeX dollar sign
        try:
            sympy_expression = parse_latex(expression)
        except sympy.parsing.latex.errors.LaTeXParsingError:
            logger.error("latex2sympy ERROR : Input expression is not a LaTeX math expression.")
            return False
        return sympy_expression

    def sympy2latex(self, sympy_expression):
        return sympy.latex(sympy_expression)

    def sympytype(self, sympy_expression):
        return type(sympy_expression)
        # sympy type, NOT EXPRESSION TYPE!!
        # please refer to 'util/type_checker.py' for expression type check


# LatexConverter = LatexConverter()
# sympylist = []
# while True:
#     input_expr = input('input_expr : ')
#     if input_expr == "quit":
#         break
#     sympy_expr = LatexConverter.latex2sympy(input_expr)
#     sympy_expr.
#     sympylist.append(sympy_expr)
#     print(sympy_expr)
#     print(type(sympy_expr))  # sympy.core.***
#     print(sympy_expr.is_real)
#     print(sympy.latex(sympy_expr))  # input_expr
