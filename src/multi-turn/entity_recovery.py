
# DB엔진을 이용하는 함수들 ...

import requests, json

def db_main_finder(input):
    #feedback_generator으로부터 들어오는 input(=component)를 갖는 uk list 반환
    #새로 요구하는 searchtype "related_uk" 
    #response 의 result(key)에 "related_uk" 값을 반환
    datas={
            "searchType": ["related_uk"],   
            "searchTerms": [input],    
            "threshold": 0.5
    }
    url="http://222.122.51.15:18010/knowledgedb/api/search"

    response=requests.post(url, data=datas).json() # url 주소 수정바람
    return response["result"]["related_uk"]

def db_sub_finder(input):
    #feedback_generator으로부터 들어오는 input(=uk)의 component list 반환
    #새로 요구하는 searchtype "related_component" 
    #response 의 result(key)에 "related_component" 값을 반환
    datas={
            "searchType": ["related_component"],   
            "searchTerms": [input],    
            "threshold": 0.5
    }
    url="http://222.122.51.15:18010/knowledgedb/api/search"

    response=requests.post(url, data=datas).json() # url 주소 수정바람
    return response["result"]["related_component"]


def similar_word(input):
    #input과 가장 유사단어 찾아주는 함수. 
    #새로 요구하는 searchtype "related_word" 
    #response 의 result(key)에 "related_word" 값을 반환
    datas={
            "searchType": ["related_word"],   
            "searchTerms": [input],    
            "threshold": 0.5
    }
    url="http://222.122.51.15:18010/knowledgedb/api/search"
    response=requests.post(url, data=datas).json() # url 주소 수정바람
    return response["result"]["related_word"]



def query_list_to_expression(input):
    #question의 main 요청(e.g. "대입")을 할 수 있는 main_expression type을 반환하는 함수
    #새로 요구하는 searchtype "main_expression_type" 
    #response 의 result(key)에 "main_expression_type" 값을 반환
    datas={
            "searchType": ["main_expression_type"],   
            "searchTerms": [input],    
            "threshold": 0.5
    }
    url="http://222.122.51.15:18010/knowledgedb/api/search"
    response=requests.post(url, data=datas).json() # url 주소 수정바람
    return response["result"]["main_expression_type"]