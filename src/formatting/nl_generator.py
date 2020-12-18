from formatting.KoreaJosa import *
from _constant._string import output_message, NLG_STRING, ASK_TYPE
import logging
from _getter.nlu_getter import NLUResultReader
 

def nl_action(input_json):
	answer = input_json["output"][0]["message"]
	output_dict = {
	"result_type" : "nlg_success", #nlg_fail
	"message" : "${}$ {}".format(answer,END)
	}
	return output_dict



def nl_implication(input_json):
	element0 = input_json["entity_intent"]["element"][0]["data"]
	element1 = input_json["entity_intent"]["element"][1]["data"]
	
	if input_json["output"][0]["message"]=="true":
		answer = YES
	else:
		answer = NO

	output_dict = {
	"result_type" : "nlg_success", #nlg_fail
	"message" : replace_josa("{}(은)는 {}(이)가 {}".format(element1,element0,answer))
	}
	return output_dict


def nl_logic(input_json):
	element0 = input_json["entity_intent"]["element"][0]["data"]
	element1 = input_json["entity_intent"]["element"][1]["data"]["expr"]
	if input_json["output"][0]["message"]=="true":
		answer = YES
	else:
		answer = NO

	output_dict = {
	"result_type" : "nlg_success", #nlg_fail
	"message" : replace_josa("${}$(은)는 {}(이)가 {}".format(element1,element0,answer))
	}
	return output_dict

def is_responce_sequence(response):
	return isinstance(response[0], list)

def knowledge_nl_form_maker(uk,attribute,response):
	return "{}의 {}: {}".format(uk,attribute,response) 

def response_process(response):
	output_message = ""
	result_type = ""
	logger = logging.getLogger("response_process")

	if response["result_type"].split("_")[-1]  == "success":
		result_type = "success"
		message = response["message"]

		if is_responce_sequence(message):
			# list로 구성된 답변을 처리하는 코드를 여기에 코딩하시죠.
			# 일단은 걍 다 더해버림.
			for m in message:
				output_message += (m + "\n")
		else : # list 아니면 걍 출력 
			output_message = message

	else : # Something fail
		result_type = "fail"
		logger.info(response["result_type"])

	return output_message, result_type

def question_process(question):
	return NLUResultReader(question)

def nl_generator(input_json):
	nl_generator_logger = logging.getLogger("nl_generator")

	question = question_process(input_json["question"])
	response, result_type = response_process(input_json["response"])

	intent_type = question.intent_type

	msg = ""
	if result_type == "success":
		if intent_type == ASK_TYPE["KNOWLEDGE"]:
			# input이 바뀌었다고 이걸 바꾸면 안됨. NLUResultReader를 바꾸자.!
			uk = question.knowledge.uk.ko
			attribute = question.knowledge.attribute.ko
			msg = knowledge_nl_form_maker(uk, attribute, response)
		
		elif intent_type==ASK_TYPE["ACTION"]:
			return nl_action(input_json)
		elif intent_type==ASK_TYPE["RELATION"]:
			return nl_implication(input_json)
		elif intent_type==ASK_TYPE["LOGICAL_SOLVE"]:
			return nl_logic(input_json)
		else:
			return output_message(NLG_STRING["RESULT_TYPE"]["FAIL"], NLG_STRING["MESSAGE"]["INTENT_FAIL"])

		return output_message(NLG_STRING["RESULT_TYPE"]["SUCCESS"], msg)

	else : # "fail" 
		return output_message(NLG_STRING["RESULT_TYPE"]["FAIL"], NLG_STRING["MESSAGE"]["RG_FAIL"])

	