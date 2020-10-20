import logging
from util.getter.cas_getter import dummy_cas_getter
from util.getter.db_getter import dummy_db_getter
from util.setter.cas_input_setter import cas_input_setter
from util.setter.db_input_setter import db_input_setter
from util.result_message_list import *
from util.url import *

class UnitKnowledge:

    def __init__(self):

        self.logger = logging.getLogger('inference_engine.'+type(self).__name__)
        self.proper_lenth_of_elements = 0
        self.proper_type_of_elements = []

    def action(self, unit_knowledge, elements):
        elements_check_result = self.element_proper_check(elements)
        if elements_check_result['result_type'] == ELMENT_PROPER_STRING:
            cas_query = cas_input_setter("action", unit_knowledge, elements, self.proper_type_of_elements)
            return  dummy_cas_getter(CAS_URL, cas_query)

        return elements_check_result
        
    def component(self, unit_knowledge, component):
        db_query = db_input_setter("component", unit_knowledge, component)
        return dummy_db_getter(DB_URL, db_query)

    def implication(self, unit_knowledge_master, unit_knowledge_slave):
        db_query = db_input_setter("implication", unit_knowledge_master, unit_knowledge_slave)
        return dummy_db_getter(DB_URL, db_query)

    def logic(self):
        pass

    def test(self):
        self.logger.debug('Current UK : ' + type(self).__name__)

    def is_proper_lenth_of_elements(self, elements):
        self.logger.debug('len of elements='+str(len(elements)))
        return True if self.proper_lenth_of_elements == len(elements) else False
    
    def is_proper_type_of_elements(self, elements):
        for i in range(0, len(elements)):
            if elements[i]['type'] == 'expression' \
                and (elements[i]['data']['expr_type'] in self.proper_type_of_elements[i]):
                return True
            else :
                return False
                
    def element_proper_check(self, elements):
        if self.is_proper_lenth_of_elements(elements):
            pass
        else :
            return ELEMENT_LENTH_ERROR

        if  self.is_proper_type_of_elements(elements):
            pass
        else :
            return ELEMENT_TYPE_ERROR

        return ELEMENT_PROPER

