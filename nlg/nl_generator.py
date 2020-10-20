END = "입니다"
YES = "맞습니다"
NO = "아닙니다"
    
#----------------------------------------------------------------------------- fixed word


if __name__ == '__main__':
    import KoreaJosa
else :
    from nlg.KoreaJosa import *
#------------------------------------------------------------------------------ pyjosa


def nl_attribute(input_json):
    element0 = input_json["entity_intent"]["element"][0]["data"]
    element1 = input_json["entity_intent"]["element"][1]["data"]
    answer = input_json["output"][0]["message"]
    output_dict = {
	"result_type" : "nlg_success", #nlg_fail
	"message" : "{}의 {}: {}".format(element0,element1,answer)
    }
    return output_dict 


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




def nl_generator(input_json):
    if input_json["entity_intent"]["query_type"]=="component":
	    return nl_attribute(input_json)
    elif input_json["entity_intent"]["query_type"]=="action":
        return nl_action(input_json)
    elif input_json["entity_intent"]["query_type"]=="implication":
        return nl_implication(input_json)
    elif input_json["entity_intent"]["query_type"]=="logic":
        return nl_logic(input_json)
    else:
        return { 
            "result_type" : "nlg_fail", #nlg_fail
            "message" : "intent_type_not_supported"
        }


if __name__ == '__main__':
    in_data={
	"entity_intent": {
	    "query_type" :"logic",
	    "element": [
	        {
	            "type":"unit_knowledge",
	            "data":"상수항"
	        },
	        {
	            "type":"expression",
	            "data": {
	                "expr": "0",
	                "expr_type": "constant",
	                "expr_n": 1,
	                "expr_elem": []
	            }
	        }
	    ]
	},
	"output" : [{        
		"result_type" : "inference_success",
        "message" : "false"
    }]
}



    print(nl_generator(in_data))
#  result = nl_generator(in_data)
