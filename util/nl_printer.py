from util.teacher_say import NLG_FAIL

def nl_printer(nlg_output):
	nlg_result_type = nlg_output['result_type']
	nlg_message = nlg_output['message']
	nl = ""
	if nlg_result_type == 'nlg_success':
		nl = nlg_message
	else : 
		nl = NLG_FAIL
	return nl