def reply(input_json):
    #input json 규격에 "question" 외에 이전 질문과 응답에 관한 "last_question", "last_answer"라는 key 값으로 주길 원합니다.
    
    last_question_expression=input_json["last_question"]["element"]["main"]["data"]
    last_answer_expression=input_json["last_answer"]["element"]["main"]["data"]
    main=input_json["question"]["elements"]["main"]["data"]
    main_expression=input_json["question"]["elements"]["main_expression"]["data"]
    
    if main_expression == 'unknown':

        output_dict = {
                "message_type" : "expression_tiki_taka", 
                "argument_1" : last_question_expression,
                "argument_2" : last_answer_expression,
                "argument_3" : main,
                # NLG output : argument1 의 main 을 물어보시나요? argument2 의 main 을 물어보시나요?
            }
        return output_dict