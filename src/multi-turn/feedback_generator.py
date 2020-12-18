import entity_recovery as er
import tiki_taka as tt
#multi-turn 

#recover typo
def typo_multi_turn(input_json):
    main=input_json["question"]["element"]["main"]
    sub=input_json["question"]["element"]["sub"]
    if main["type"]!='unknown' and sub["type"]=='unknown': 
        output_dict = {
                "message_type" : "recover_typo_1", 
                "argument_1" : sub["data"],
                "argument_2" : er.db_similar_word(sub["data"]),
                # NLG output : argument1 을 이해하지 못했습니다, argument2 말씀이신가요?
            }
        return output_dict
       
    elif main["type"]=='unknown' and sub["type"]!='unknown': 
        output_dict = {
                "message_type" : "recover_typo_2", 
                "argument_1" : main["data"],
                "argument_2" : er.db_similar_word(main["data"])
                # NLG output : argument1 을 이해하지 못했습니다, argument2 말씀이신가요?
            }
        return output_dict
       
    elif main["type"]!='unknown' and sub["type"]!='unknown': 
        output_dict = {
                "message_type" : "recover_typo_3", 
                "argument_1" : sub["data"],
                "argument_2" : er.db_similar_word(sub["data"]),
                "argument_3" : main["data"],
                "argument_4" : er.db_similar_word(main["data"]),
                # NLG output : argument1 을 이해하지 못했습니다, argument2 말씀이신가요? argument3 을 이해하지 못했습니다, argument4 말씀이신가요?
            }
        return output_dict
    else:
        output_dict = {
                "message_type" : "recover_typo_4", 
                # NLG output : 질문을 이해할 수 없습니다.
            }
        return output_dict


   
#typo 처리가 끝난 후
def voca_multi_turn(input_json):
    main=input_json["question"]["element"]["main"]
    sub=input_json["question"]["element"]["sub"]
    if main["type"]!='unknown' and sub["type"]=='unknown':
        output_dict = {
                "message_type" : "main_sub_1", 
                "argument_1" : main["data"],
                "argument_2" : er.db_sub_finder(main["data"]),
                # NLG output : argument1 에 관한 질문은 argument2 중에서 질문해 주세요.
            }
        return output_dict
        


    elif main["type"]=='unknown' and sub["type"]!='unknown':
        output_dict = {
                "message_type" : "main_sub_2", 
                "argument_1" : sub["data"],
                "argument_2" : er.db_main_finder(sub["data"]),
                # NLG output : argument1 에 관한 질문은 argument2 중에서 질문해 주세요.
            }
        return output_dict
    
    elif main["type"]=='unknown' and sub["type"]=='unknown':
        output_dict = {
                "message_type" : "main_sub_3", 
                # NLG output : 질문을 이해할 수 없습니다.
            }
        return output_dict
  


def expression_multi_turn(input_json):
    main=input_json["question"]["element"]["main"]
    main_expression=input_json["question"]["element"]["main_expression"]
    variable=input_json["question"]["element"]["variable"]
    value=input_json["question"]["element"]["value"]
   
    if main["type"]=='unknown':
        return voca_multi_turn(input_json)

    elif main["data"] in er.query_list_to_expression(main_expression["type"]) and variable["type"]=='unknown':
        output_dict = {
                "message_type" : "correct_expression_1", 
                # NLG output : 요청해야 하는 변수가 빠졌거나 부적절합니다.
            }
        return output_dict

    elif main["data"] in er.query_list_to_expression(main_expression["type"]) and value["type"]=='unknown':
        output_dict = {
                "message_type" : "correct_expression_2", 
                # NLG output :요청해야 하는 값이 빠졌거나 부적절합니다.
            }
        return output_dict
        
    elif not main["data"] in er.query_list_to_expression(main_expression["type"]):
        output_dict = {
            "message_type" : "incorrect_expression", 
	        "argument_1" : main["data"],
            "argument_2" : er.query_list_to_expression(main["data"])
            # NLG output : argument1를 요청할 수 없습니다. argument1 요청은 argument2 에만 가능합니다.
        }
        return output_dict
        
    elif not main["data"] in er.query_list_to_expression(main_expression["type"]):
        output_dict = {
            "message_type" : "incorrect_expression", 
	        "argument_1" : main["data"],
            "argument_2" : er.query_list_to_expression(main["data"])
            # NLG output : argument1를 요청할 수 없습니다. argument1 요청은 argument2 에만 가능합니다.
        }
        return output_dict
        



    
# import numpy as np 
# db.json으로부터 intent 파악을 위한 keyword_scoring 함수.    
# def keyword_scoring(input_json, given_vec):
#     db_keys_list=list(input_json.keys());
#     db_values_list=list(input_json.values());

#     for i in range(len(db_keys_list)):
#         for j in range(0,3):
#             if input_json[db_keys_list[i]][choice_list[j]]["keyword"] != []:
#                 answer=[ db_keys_list[i], choice_list[j], np.dot(given_vec, np.array(input_json[db_keys_list[i]][choice_list[j]]["keyword"])) ] 
#             responses.append(answer)
#         ks = np.array(responses)
      
  
#     for i in range(np.shape(ks)[0]):             
#         score_list.append(ks[i][2])

#     glist=list(score_list)

#     return ks[np.argmax(glist)][0]+ nl.sayof + ks[np.argmax(glist)][1]+ nl.ending


 #--------------------------------------------------------------------------------------------------------------------------------------------- multi-turn
def feedback_generator(input_json):
    keys_list=list(input_json.keys())
    main=input_json["question"]["element"]["main"]
    sub=input_json["question"]["element"]["sub"]

    if input_json["type"]=="elements_type_error":
        if input_json["question"]["intent_type"]=='expression_reasoning' or input_json["question"]["intent_type"]=='logical_reasoning':
            if main["data"]=='unknown':
                return typo_multi_turn(input_json)
            else:    
                return expression_multi_turn(input_json)

        elif input_json["question"]["intent_type"]!='expression_reasoning' and input_json["question"]["intent_type"]!='logical_reasoning':    
            if main["data"]=='unknown' or sub["data"]=='unknown':
                return typo_multi_turn(input_json)
            else:    
                return voca_multi_turn(input_json)

    elif input_json["type"]=="tiki_taka": #문형분석에서 "이 식의" "이 것의" 등의 지시대명사면, input_json의 type에 tiki_taka로 주길 원합니다.
        return tt.reply(input_json)




#--------------------------------------------------------------------------------------------------------------------------------------------- feedback_generator
if __name__ == '__main__':
    

    json={
    "type" : "elements_type_error",
    "what" : "variable",
    "why" : "none",
    "from" : "response_generator",
    "reference" : {
                  "count" : 2,
                  "data":[ 
                      {
                      "key_name" : "main_expression",
                      "value_type" : "expression",
                      "data_type" : "unique"
                      },
                      {
                      "key_name" : "variable",
                      "value_type" : "character",
                      "data_type" : "set"
                      }
                  ]
    },
    "question" : {
        "intent_type":"expression_reasoning",
        "element": 
            {
                "main" : {
                    "type": "unit_knowledge",
                    "data": "x절편"              
                },
                "sub" : {},
                "main_expression" : {
                    "type": "expression",
                    "data": "2x-y-4"
                },
                "variable" : {},
                "value" : {}
            }
      }
  }


#     db_json2={
#     "type" : "elements_type_error",
#     "what" : "variable",
#     "why" : "none",
#     "from" : "response_generator",
#     "reference" : {
#                   "count" : 2,
#                   "data":[ 
#                       {
#                       "key_name" : "main_expression",
#                       "value_type" : "expression",
#                       "data_type" : "unique"
#                       },
#                       {
#                       "key_name" : "variable",
#                       "value_type" : "character",
#                       "data_type" : "set"
#                       }
#                   ]
#     },
#     "question" : {
#         "intent_type":"expression_reasoning",
#         "element": 
#             {
#                 "main" : {
#                     "type": "unit_knowledge",
#                     "data": "계수"              
#                 },
#                 "sub" : {},
#                 "main_expression" : {
#                     "type": "expression",
#                     "data": "2x-y-4"
#                 },
#                 "variable" : {},
#                 "value" : {}
#             }
#       }
#   }

print(feedback_generator(json))




