import logging
import json
import os
from sympy import *
cas_logger = logging.getLogger(__name__)


class Cas:
        
    
    def __init__(self, query):

        self.query = query
        self.unit_knowledge = query["unit_knowledge"]
        self.task = query["task"]
        self.expression = query['expression']
        self.result = {
            "result_type" : "cas_success",
            "message" : ""
        }

        if self.unit_knowledge == "Coefficient":
            self.result['message'] = self.coefficient(self.expression)

        elif self.unit_knowledge == "Substitution":
            self.result['message'] = self.substitution(self.expression)

        elif self.unit_knowledge == "Degree":
            self.result['message'] = self.degree_of_term()

        else:
            print("Not supported in this version CAS")
            self.result['result_type'] = "cas_fail"
            self.result['message'] = "unit_knowledge not supported"

    def coefficient(self, expression):
        x, y, z, a, b, c, d= symbols('x y z a b c d')
        main_expression = sympify(expression['main_expression']['data']['expr'])
        sub_expression = sympify(expression['sub_expression']['data']['expr'])
        return main_expression.coeff(sub_expression,1)

    def substitution(self, expression):
        x, y, z, a, b, c, d= symbols('x y z a b c d')
        main_expression = sympify(expression['main_expression']['data']['expr'])
        sub_expression = sympify(expression['sub_expression']['data']['expr'])
        sub_variable = sympify(expression['sub_variable']['data']['expr'])
        return main_expression.subs(sub_expression,sub_variable)

    def degree_of_term(self):
        pass

    def get_result(self):
        return self.result
 
def dummy_cas_getter(url, json):
    cas = Cas(json)
    result = cas.get_result()
    cas_logger.debug("----cas_result----")
    cas_logger.debug(result)
    return result 

def cas_getter(url, json):
    pass

if __name__=='__main__':

    cas_logger.debug("dummy_cas_main")
    query_json_data = json.load(open(os.path.join("query_example/cas_input_example_substitution.json"), 'r', encoding='UTF8'))

    dummy_cas_getter("url", query_json_data)