import sys
import re
import logging 
from _utils import is_hangul

class NLUResultReader:
    # TODO: 논리식의 input_json? 형태가 바뀌면 슬프게도 다바꾸어야 할듯.
    # 이 코드만 수정해서 다시 프로그램이 동작하게하길 희망..

    def __init__(self, nlu_result):
        try:
            self.intent_type = nlu_result['intent_type']
            self.element = nlu_result['element']
            self.main = nlu_result['element']['main']
            self.sub = nlu_result['element']['sub']
            self.main_expression = nlu_result['element']['main_expression']
            self.variable = nlu_result['element']['variable']
            self.value = nlu_result['element']['value']
            self.data_korean2english()

            # 네개의 질의 유형에 따라 데이터를 필요한 것만 추출
            # NLU 는 미래에 별도의 모듈이 될수도 있으니 어찌됬든 이런 추출해주는 코드는 여기에 있어야함.

            self.knowledge = Knowledge(self.main, self.sub)
            self.relation = Relation(self.main, self.sub)
            self.logic = Logic(self.main, self.main_expression)
            self.action = Action(self.main, self.main_expression, self.variable, self.value)

        except Exception as e:
            self.nlu_reader_logger = logging.getLogger("NLUResultReader")
            self.nlu_reader_logger.error(e)



    # 영문 UK 이름 추가하는 작업인데 도통 어딨어야 행복할지 모르겠어.    
    # 어쨋든 이 정보들이 전부 NLU에도 있어야 하는거 같은데. NLU에서 하는게 좋지 않을까? 
    def data_korean2english(self):
        if len(self.main) > 0:
            if self.main["type"] == "unit_knowledge":
                if is_hangul(self.main["data"]):
                    self.element["main"]["data_en"] = uk_korean_english[self.main["data"]]
                else :
                    self.element["main"]["data_en"] = self.main["data"]

        if len(self.sub) > 0:
            if self.sub["type"] == "component":                
                if is_hangul(self.sub["data"]):
                    self.element["sub"]["data_en"] = knowledge_name_korean_english[self.sub["data"]]
                else : 
                    self.element["sub"]["data_en"] = self.sub["data"]

class Knowledge:
    def __init__(self, uk, attribute):
        self.uk = Multilingual(uk["data"], uk["data_en"])
        self.attribute = Multilingual(attribute["data"], attribute["data_en"])

class Relation:
    def __init__(self, uk1, uk2):
        self.uk1 = Multilingual(uk1["data"], uk1["data_en"])
        self.uk2 = Multilingual(uk2["data"], uk2["data_en"])

class Logic:
    def __init__(self, uk, expression):
        self.uk = Multilingual(uk["data"], uk["data_en"])
        self.expression = expression["data"]

class Action:
    def __init__(self,uk, expression, variable, value):
        self.uk = Multilingual(uk["data"], uk["data_en"])

# 나중에 인도어 지원할때 변수 추가하셈 
class Multilingual:
    def __init__(self, ko, en):
        self.ko = ko
        self.en = en

'''DB'''

entit_type = ["unit_knowledge", "expression", "component"]
    
# TODO: 디비에 있기를 기대하는 정보들 
# TODO: 여기서도 DB 쿼리 해야하나? 어딘가 이 정보들을 캐싱해놓고 싶군..
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

knowledge_name_korean_english = {
    "정의" : "definition",
    "성질" : "property",
    "과정" : "process",
    "예시" : "example"
}