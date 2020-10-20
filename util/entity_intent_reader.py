import sys
import re

QUERY_UK_INDEX = 0
QUERY_ELEMENTS_INDEX = 1
QUERY_COMPONENT_INDEX = 1
QUERY_LOGIC_INDEX = 1
QUERY_UK_MASTER_INDEX = 0
QUERY_UK_SLAVE_INDEX = 1

#TODO : 쿼리타입별로 클래스 쪼개서 상속 클래스
class EntityIntentReader:
    def __init__(self, query_json_data):
        self.intent = query_json_data['query_type']
        self.entity = query_json_data['element']

        self.data_korean2english()

        # TODO: 이걸 다 쪼갠이유는 모든 질의에 UK가 있느냐? 없을 수도 있기애 이렇게 되어버림.  
        # TODO: INTENT마다 질의에 대한 구조 픽스가 필요하다.  

        if self.intent == "action":
            self.action_unit_knowledge = self.entity[QUERY_UK_INDEX]
            self.action_expression_list = self.entity[QUERY_ELEMENTS_INDEX:]
        
        elif self.intent == "component":
            self.component_unit_knowledge = self.entity[QUERY_UK_INDEX]
            self.component = self.entity[QUERY_COMPONENT_INDEX]

        elif self.intent == "logic":
            self.logic_unit_knowledge = self.entity[QUERY_UK_INDEX]
            self.logic_expression = self.entity[QUERY_LOGIC_INDEX]

        elif self.intent == "implication":
            self.implication_unit_knowledge_master = self.entity[QUERY_UK_MASTER_INDEX]
            self.implication_unit_knowledge_slave = self.entity[QUERY_UK_SLAVE_INDEX]
        else :
            pass

    def test(self):
        print('test')

    def data_korean2english(self):
        for e in self.entity:
            if e["type"] == "unit_knowledge" :
                if self.is_hangul(e["data"]):
                    e["data_en"] = uk_korean_english[e["data"]]
                else : 
                    e["data_en"] = e["data"]           
            elif e["type"] == "component":
                if self.is_hangul(e["data"]):
                    e["data_en"] = component_korean_english[e["data"]]
                else : 
                    e["data_en"] = e["data"]

                    
    def is_hangul(self, text):
        #Check the Python Version
        py_ver3 =  sys.version_info >= (3, 0)

        if py_ver3 : # for Ver 3 or later
            enc_text = text
        else: # for Ver 2.x
            if type(text) is not unicode:
                enc_text = text.decode('utf-8')
            else:
                enc_text = text

        han_count = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', enc_text))
        return han_count > 0

entit_type = ["unit_knowledge", "expression", "component"]
    

uk_korean_english = {
    "단위지식" : "UnitKnowledge",
    "방정식" : "Equation",
    "식" : "Expression",
    "일차식" : "LinearExpression",
    "단항식" : "Monomial",
    "다항식" : "Polynomial",
    "대입" : "Substitution" ,
    "수" : "Number",
    "항" : "AlgebraicTerm" ,
    "등식" : "LikeTerm",
    "차수" : "Degree",
    "상수항" : "ConstantTerm",
    "계수" : "Coefficient",
    "식의 값" : "ValueOfAlgebraicTerm",
    "동류항" : "SimilarTerm",
    "좌변" : "LeftHandSide",
    "우변" : "RightHandSide",
    "양변" : "BothSide",
    "항등식" : "Identity",
    "이항" : "Transposition",
    "일차방정식" : "LinearEquation"

}

component_korean_english = {
    "정의" : "definition",
    "성질" : "property",
    "과정" : "process",
    "예시" : "example"
}