import logging
import _utils

from _getter.nlu_getter import NLUResultReader
from _getter.nlg_getter import nlg_getter
from _getter.cas_getter import dummy_cas_getter
from _getter.db_getter import dummy_db_getter

from _setter.cas_input_setter import cas_input_setter
from _setter.db_input_setter import db_input_setter
from _setter.nlg_input_setter import nlg_input_setter

from _constant._string import ( ASK_TYPE,
    ELEMENT_STRING, 
    output_message,
    RESPONSE_STRING)

class UnitKnowledge:
    def __init__(self):
        self.uk_logger = logging.getLogger("UnitKnowledge")

    def do_action(self, action):
        try:
            elements_check_result = self.element_check(elements)
            if elements_check_result['result_type'] == ELEMENT_STRING['TYPE_PROPER']:
                self.uk_logger.info(unit_knowledge)
                # cas_query = cas_input_setter("action", unit_knowledge, elements, self.proper_type_of_elements)
                # return  dummy_cas_getter(_utils.CONFIG.CAS_URI, cas_query)
            return elements_check_result
        except Exception as e:
            self.uk_logger.error("do_action error : %s", e)        

        
    def get_knowledge(self, knowledge):
        try:
            uk_ko = knowledge.uk.ko
            attribute_en = knowledge.attribute.en
            self.uk_logger.info("uk : %s, attribute : %s", uk_ko, attribute_en)

            if uk_ko and attribute_en: # 이거 효력 있는 조건문인지 모르겠넹..
                db_query = db_input_setter(ASK_TYPE["KNOWLEDGE"], uk_ko, attribute_en)
                return dummy_db_getter(_utils.CONFIG.DB_URI, db_query)
            else : # condition error
                return output_message(RESPONSE_STRING["CONDITION_ERROR"], "")

        except Exception as e:
            self.uk_logger.error("get_knowledge error : %s", e)        

    def get_relation(self, unit_knowledge_master, unit_knowledge_slave):
        db_query = db_input_setter("implication", unit_knowledge_master, unit_knowledge_slave)
        return dummy_db_getter(_utils.CONFIG.DB_URI, db_query)

    def do_logic(self):
        pass
        

# 모든 모듈간의 통신은 Dict로 
# 그렇게 하면 미래에 모듈이 컨테이너로 분리되도 해당 Dict를 Post하면됨.
def response_generate(nlu_result):
    response_logger = logging.getLogger("response_generate")

    processed_nlu_result = NLUResultReader(nlu_result)
    ask_type = processed_nlu_result.intent_type
    elements = processed_nlu_result.element
    
    response = ""

    uk = UnitKnowledge()

    if ask_type == ASK_TYPE["ACTION"]:
        response = uk.do_action(processed_nlu_result.action)

    elif ask_type == ASK_TYPE["KNOWLEDGE"]:  
        response = uk.get_knowledge(processed_nlu_result.knowledge)

    elif ask_type == ASK_TYPE["LOGICAL_SOLVE"]:
        response = uk.do_logic(processed_nlu_result.logic)

    elif ask_type == ASK_TYPE["RELATION"]: # relation
        response = uk.get_relation(processed_nlu_result.relation)

    else:
        response_logger.info("Undefined ask type entered.")

    # Log print
    nlg_input = nlg_input_setter(nlu_result, response)
    response_logger.info("nlg_input: %s",nlg_input)
    nlg_output = nlg_getter(nlg_input)
    response_logger.info("nlg_output: %s",nlg_output)



    return nlg_output["message"]

