'''
    REFACTORING COMPLETED
    NOT USING THIS MODULE ANYMORE, WILL BE DELETED SOON
    PLEASE USE 'util/latex2sympy.py'
'''

import re
import json
import logging
from util.bnf_json import BnfJson, BnfJsonEncoder
from util.type_checker import NumType, ExprType

LOGGING_LEVEL = logging.DEBUG
debug = 0 # if 1, input as terminal and create json file

logger = logging.getLogger('inference_engine/math_util')
logger.setLevel(LOGGING_LEVEL)
stream_hander = logging.StreamHandler()
logger.addHandler(stream_hander)


# test if expression includes input variable
def has_element(expression, variable):
    expression = expression['expr']
    regexp = re.compile(variable)
    find = regexp.search(expression)
    if find is None:
        logger.debug(expression + ' has no element of ' + variable)
        return False
    else:
        logger.debug(expression + ' has element of ' + variable)
        return True


# parse expression into terms
def expression_to_term(expression):
    expression = re.sub('[\s$]', '', expression['expr'])  # remove whitespace and LaTeX identifier
    logger.debug('input expr'.ljust(10) + ' : ' + expression)
    expression = re.sub('\+', ' ', expression)  # remove '+'
    terms = expression.split(' ')  # parse expression into terms
    logger.debug('term(s)'.ljust(10) + ' : ' + str(terms))
    return terms


# find all variables in expression
def variable_in_expression(expression):
    expression = re.sub('[\d\s\+\-\*\^\$]', '', expression['expr'])
    variable = ''.join(sorted(set(expression)))
    logger.debug(list(variable))
    return list(variable)


def is_float(num):
    try:
        judge = str(float(num))
        return False if (judge == 'nan' or judge == 'inf' or judge == '-inf') else True
    except ValueError:
        return False


# encode expression to bnf form
# input : LaTeX expression
# output : bnf form of expr
def expression2bnf(expression, bnf_input):
    logger.debug('input expr : ' + expression)
    expression = re.sub('[\s$]', '', expression)  # remove whitespace and LaTeX '$' sign
    expression = re.sub(r"\\eq", "=", expression)
    expression = re.sub(r"\\neq", "~=", expression)
    expression = re.sub(r"\\leq", "<=", expression)
    expression = re.sub(r"\\lt", "<", expression)
    expression = re.sub(r"\\geq", ">=", expression)
    expression = re.sub(r"\\gt", ">", expression)
    expression = re.sub(r"\\times", "*", expression)
    expression = re.sub(r"(-)([a-zA-Z])", r"-1\2", expression)  # replace "-x" to "(-1)*(x)"
    expression = re.sub(r"([0-9a-zA-Z\)])(-)([\(0-9a-zA-Z])", r"\1+-\3", expression)  # insert '+' in front of '-'
    expression = re.sub(r"(\\frac{)([0-9a-zA-Z]+)(}{)([0-9a-zA-Z]+)(\})", r"\2/\4", expression)  # LaTex frac -> /
    expression = re.sub(r"([0-9a-zA-Z]+)(\\div)([0-9a-zA-Z]+)", r"\1/\3", expression)  # LaTex div -> /
    expression = re.sub(r"((?:\d+)|(?:[a-zA-Z]\w*\(\w+\)))((?:[a-zA-Z]\w*)|\()", r"\1*\2", expression)  # insert '*' between coefficient and variable
    expression = re.sub(r"([a-zA-Z])([a-zA-Z])", r"\1*\2", expression)  # insert '*' between multiply of variables
    expression = re.sub(r"([a-zA-Z]\))(\([0-9a-zA-Z])", r"\1*\2", expression)  # insert '*' between ')' and '('
    logger.debug('regex expr'.ljust(10) + ' : ' + expression)

    bnf_json = BnfJson()
    bnf_json.expr = expression

    matches = ['+', '*', '^', '<=', '>=', '~=', '=', '>', '<', '/']
    if any(x in expression for x in matches):
        if '<=' in expression:
            expr_elems = expression.split('<=')
            expr_type = 'leq'
        elif '>=' in expression:
            expr_elems = expression.split('>=')
            expr_type = 'geq'
        elif '~=' in expression:
            expr_elems = expression.split('~=')
            expr_type = 'neq'
        elif '=' in expression:
            expr_elems = expression.split('=')
            expr_type = 'eq'
        elif '>' in expression:
            expr_elems = expression.split('>')
            expr_type = 'gt'
        elif '<' in expression:
            expr_elems = expression.split('<')
            expr_type = 'lt'
        elif '+' in expression:
            expression = re.sub('\+', ' ', expression)  # remove '+'
            expr_elems = expression.split(' ')  # parse expression into terms
            expr_type = 'finite_addition'
        elif '*' in expression:
            expr_elems = expression.split('*')
            expr_type = 'finite_product'
        elif '^' in expression:
            expr_elems = expression.split('^')
            expr_type = 'exponential'
        elif '/' in expression:
            expr_elems = expression.split('/')
            expr_type = 'fraction'
        expr_n = len(expr_elems)

        logger.debug('expr_type'.ljust(10) + ' : ' + expr_type)
        logger.debug('expr_n'.ljust(10) + ' : ' + str(expr_n))
        logger.debug('expr_elem'.ljust(10) + ' : ' + str(expr_elems)+'\n')

        bnf_json.expr_type = expr_type
        bnf_json.expr_n = expr_n

        for idx, elem in enumerate(expr_elems):  # generate bnf form recursively
            bnf_json.expr_elem.append(expression2bnf(elem, ''))

    else:
        expr_elems = expression
        type_checker = NumType()
        if type_checker.is_float(expr_elems) is True:
            expr_type = 'constant'
        else:
            expr_type = 'variable'
        expr_n = 1

        logger.debug('expr_type'.ljust(10) + ' : ' + expr_type)
        logger.debug('expr_n'.ljust(10) + ' : ' + str(expr_n))
        logger.debug('expr_elem'.ljust(10) + ' : ' + str(expr_elems)+'\n')

        bnf_json.expr_type = expr_type
        bnf_json.expr_n = expr_n
        bnf_json.expr_elem = []

    return bnf_json


# end of "def expression2bnf(expression)"


# encode expression to bnf form and write to json file
def expression2json(input_expr):
    if debug is 1:
        input_expr = input('input expr(LaTeX) : ')
    output_file_name = 'bnf' + input_expr.replace('\\', '') + '.json'
    bnf_form_expr = expression2bnf(input_expr, '')
    encode_bnf_form_expr = BnfJsonEncoder().encode(bnf_form_expr)
    json_out = json.loads(encode_bnf_form_expr)
    if debug is 1:
        print('bnf form'.ljust(10) + ' : ' + encode_bnf_form_expr)
        with open(output_file_name, 'w', encoding="utf-8") as json_file:
            json.dump(json_out, json_file, ensure_ascii=False, indent="\t")
    return json_out


# print("---- expression2bnf test ----")
# while True:
#     expr_dict_test = input('input expr(LaTeX) : ')
#     expression2json(expr_dict_test)
# expr_dict_test = expression2json('$\\frac{A}{C}=\\frac{B}{C}$')
# print(expr_dict_test)

# print("---- has_element test----")
# has_element(expr_dict_test, 'y')
# has_element(expr_dict_test, 'z')

# print("---- expression_to_term test----")
# expression_to_term(expr_dict_test)

# print("---- variable_in_expression test----")
# variable_in_expression(expr_dict_test)

# print("=== expr type check test ===")
# expr_checker = ExprType()
# test_expr = ['0', '1', 'x', 'xy', 'x+1', 'xy+1', 'x=', 'x=y', '2=2', 'x=2']
# for i in test_expr:
#     expr_dict_test = expression2json(i)
#     print('in : ' + i)
#     expr_type = expr_checker.ExprType(expr_dict_test)
#     print('out: ' + str(expr_type))
# print(expr_checker.LinearExpression(expr_dict_test))
