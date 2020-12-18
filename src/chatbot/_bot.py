from chatbot.bot_string import BOT_MSG
from nlu.nlu import nlu_result
from response_generator.response_generator import response_generate
from _utils import is_hangul

# 수학질의 응답 도메인 특화된 답변을 생성하기 전에 전처리를 하는 부분

def is_wakeup_call_in(msg):
    return True if BOT_MSG["TEACHER_INIT"] in msg else False

def bot_answer(sender, msg, logger):
    answer = ""
    if not is_hangul(msg) :
        return BOT_MSG["LANGUAGE_NOT_SUPPORTED"]
    if not is_wakeup_call_in(msg): 
        return BOT_MSG["TEACHER_NEED_INIT"]      

    nlu_result_dict = nlu_result(msg)           # NLU가 여기있는 이유: 미래에 command랑 push 때문 
    
    if len(nlu_result_dict["element"]) == 0:    # NLU가 질문을 인식하지 못한 상황, 좀더 직관적인 NLU 분석 결과가 필요한듯 
        return BOT_MSG["QUESTION_NOT_DEFINE"]   

    else : # 인식하면 RG에 가서 처리 후 대답 return 
        logger.info(BOT_MSG["TEACHER_RECONIZE"])
        answer = response_generate(nlu_result_dict)


    return answer 
