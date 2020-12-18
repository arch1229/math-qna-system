def nlg_input_setter(question, response):

	input_data = {}
	input_data['question'] = question
	# response는 dict의 list 일수도 dict일수도 있다. 
	input_data['response'] = response
	
	return input_data