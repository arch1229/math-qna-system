if __name__=='__main__':
	from type_checker import NumType, ExprType
else:
	from util.type_checker import NumType, ExprType

EXPR_TYPE_LAST_CANDIDATE_INDEX = -1
MAIN_EXPRESSION_INDEX = 0
SUB_EXPRESSION_INDEX = 1
SUB_VALUE_INDEX = 2

HAS_MAIN_EXPRESSION_SUB_EXPRESSION_SUB_VALIABLE = 3
HAS_MAIN_EXPRESSION_SUB_EXPRESSION = 2

# TODO: nl2query에서 날라오는 쿼리 규격을 수정하여 로직을 단순화 하자 

def cas_input_setter(task, unit_knowledge, elements, proper_type_of_elements):
	input_data = {}
	input_data["unit_knowledge"] = unit_knowledge
	input_data["task"] = task
	input_data["expression"] = {}
	input_data["expression"] = expression_data_setter(elements, proper_type_of_elements)
	
	return input_data

def expression_data_setter(elements, proper_type_of_elements):
	expr_checker = ExprType()
	expression_data = {}
	
	if len(proper_type_of_elements) == HAS_MAIN_EXPRESSION_SUB_EXPRESSION_SUB_VALIABLE:
		expression_data["main_expression"] = elements[MAIN_EXPRESSION_INDEX]
		# expression_data["main_expression"]["type"] = \
		# 	expr_checker.ExprType(elements[MAIN_EXPRESSION_INDEX]["data"])[EXPR_TYPE_LAST_CANDIDATE_INDEX]

		expression_data["sub_expression"] = elements[SUB_EXPRESSION_INDEX]
		# expression_data["sub_expression"]["type"] = \
		# 	expr_checker.ExprType(elements[SUB_EXPRESSION_INDEX]["data"])[EXPR_TYPE_LAST_CANDIDATE_INDEX]

		expression_data["sub_variable"] = elements[SUB_VALUE_INDEX]
		# expression_data["sub_variable"]["type"] = \
		# 	expr_checker.ExprType(elements[SUB_VALUE_INDEX]["data"])[EXPR_TYPE_LAST_CANDIDATE_INDEX]

	elif len(proper_type_of_elements) == HAS_MAIN_EXPRESSION_SUB_EXPRESSION:
		expression_data["main_expression"] = elements[MAIN_EXPRESSION_INDEX]
		# expression_data["main_expression"]["type"] = \
		# 	expr_checker.ExprType(elements[MAIN_EXPRESSION_INDEX]["data"])[EXPR_TYPE_LAST_CANDIDATE_INDEX]

		expression_data["sub_expression"] = elements[SUB_EXPRESSION_INDEX]
		# expression_data["sub_expression"]["type"] = \
		# 	expr_checker.ExprType(elements[SUB_EXPRESSION_INDEX]["data"])[EXPR_TYPE_LAST_CANDIDATE_INDEX]

		expression_data["sub_variable"] = {}

	return expression_data


if __name__=='__main__':
	test = {
                "expr": "2*x+-1*y+4",
                "expr_type": "finite_addition",
                "expr_n": 3,
                "expr_elem": [
                    {
                        "expr": "2*x",
                        "expr_type": "finite_product",
                        "expr_n": 2,
                        "expr_elem": [
                            {
                                "expr": "2",
                                "expr_type": "constant",
                                "expr_n": 1,
                                "expr_elem": []
                            },
                            {
                                "expr": "x",
                                "expr_type": "variable",
                                "expr_n": 1,
                                "expr_elem": []
                            }
                        ]
                    },
                    {
                        "expr": "-1*y",
                        "expr_type": "finite_product",
                        "expr_n": 2,
                        "expr_elem": [
                            {
                                "expr": "-1",
                                "expr_type": "constant",
                                "expr_n": 1,
                                "expr_elem": []
                            },
                            {
                                "expr": "y",
                                "expr_type": "variable",
                                "expr_n": 1,
                                "expr_elem": []
                            }
                        ]
                    },
                    {
                        "expr": "4",
                        "expr_type": "constant",
                        "expr_n": 1,
                        "expr_elem": []
                    }
                ]
            }
           
	expr_checker = ExprType()
	expr_type = expr_checker.ExprType(test)
	print(expr_type)