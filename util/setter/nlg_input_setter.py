def nlg_input_setter(question, inference_result):

	input_data = {}
	input_data['entity_intent'] = question
	input_data['output'] = [inference_result]
	
	return input_data