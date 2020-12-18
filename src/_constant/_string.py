'''
	- result_type은 something_success, something_fail로 약속합니다. 
	- 각각의 모듈의 String들을 파일단위로 분리하고 각각 모듈 폴더 안으로 이동합시다. 
	- 그외의 룰은 이어서 적어주세요."
'''
ASK_TYPE = {
	"KNOWLEDGE" : "component",
	"RELATION" : "implication",
	"LOGICAL_SOLVE"	: "logic",
	"ACTION" : "action"
}

ELEMENT_STRING = {
	"TYPE_PROPER" : "element_type_proper",
	"TYPE_PROPER_MSG" : "element type is proper",
	"TYPE_ERROR" : "element_type_error",
	"TYPE_ERROR_MSG" : "element type is not proper"
}
INTENT_STRING = {
	"TYPE_ERROR" : "intent_type_error",
	"TYPE_ERROR_MSG" : "intent not supported"
}
RESPONSE_STRING = {
	"CONDITION_ERROR" : "condition_error",
}

NLG_STRING = {
	"MESSAGE" : {
		"RG_FAIL" : "다른 모듈의 오류로 자연어를 생성할 수 없습니다.",
		"INTENT_FAIL" : "처리가 불가능한 질의 유형입니다. ",
		"UNKNOWN" : "자연어 생성중 알수없는 오류 발생"
	},
	"RESULT_TYPE" : {
		"SUCCESS" : "nlg_success",
		"FAIL" : "nlg_fail"
	},
	"END" : "입니다",
	"YES" : "맞습니다",
	"NO" : "아닙니다",
} 

def output_message(result_type, message):
	return {"result_type": result_type, "message": message}