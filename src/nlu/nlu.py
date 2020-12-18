# from util.math_util import *

def expression_process(question):
    expressions = []
    while question.count('$'):
        start = question.index('$')
        length = question[start+1:].index('$')+1
        expression = question[start:start+length+1]
        expressions.append(expression)
        question = question.replace(expression, "expression")
    return question, expressions

def mecab_process(question):
    import MeCab
    mecab = MeCab.Tagger()
    out = mecab.parse(question).split('\n')[:-2]
    result = []
    for item in out:
        tmp_dict = {}
        item = item.split('\t')
        tmp_dict['token'] = item[0]
        tmp_dict['tag'] = item[1].split(',')[0].split('+')
        tmp_dict['morpheme'] = [morph.split('/')[0] for morph in item[1].split(',')[7].split('+')]
        if len(tmp_dict['morpheme'])==1: tmp_dict['morpheme'] = [item[0]]
        result.append(tmp_dict)
    return result

def abstract_append(abstract,key,element):
    try:
        abstract[key].append(element)
    except KeyError:
        abstract[key] = []
        abstract[key].append(element)

def abstract_generator(result, input_expressions):
    expressions = input_expressions.copy()
    uk_list = ['대입','식의 값','항','상수항','계수','다항식','단항식','차수','일차식','동류항','등식','좌변','우변','양변','방정식','항등식','이항','일차방정식']
    component_list = ['정의','성질','과정','예시']
    josa_tag = ['JKS','JKC','JKG','JKO','JKB','JKQ','JX','JC']
    is_tag = ['VCP','VCN']
    what = ['뭐','무엇']
    how = ['어떻게']
    why = ['왜']
    parser = []
    abstract = {}
    index = 0
    stats = {
            "UK":0,
            "Component":0,
            "Expression":0,
            }
    for item_dict in result:
        if item_dict['token'] in uk_list:
            abstract_append(abstract,'UK',(item_dict['token'],index))
            index += 1
            parser.append((item_dict['token'],'UK'))
            stats["UK"] += 1
        elif item_dict['token'] in component_list:
            abstract_append(abstract,'Component',(item_dict['token'],index))
            index += 1
            parser.append((item_dict['token'],'Component'))
            stats["Component"] += 1
        elif item_dict['token'] == 'expression':
            expression = expressions.pop(0)
            abstract_append(abstract,'Expression',(expression,index))
            index += 1
            parser.append((expression,'Expression'))
            stats["Expression"] += 1
        else:
            for i in range(len(item_dict['tag'])):
                tag = item_dict['tag'][i]
                particle = item_dict['morpheme'][i]
                if tag in josa_tag:
                    abstract_append(abstract,'tag',(item_dict['morpheme'][i],index))
                    index += 1
                    parser.append((item_dict['morpheme'][i],tag))
                elif tag in is_tag:
                    abstract_append(abstract,'is',(item_dict['morpheme'][i],index))
                    index += 1
                    parser.append((item_dict['morpheme'][i],'is'))
                elif particle in what:
                    abstract_append(abstract,'what',(item_dict['morpheme'][i],index))
                    index += 1
                    parser.append((item_dict['morpheme'][i],'what'))
                elif particle in how:
                    abstract_append(abstract,'how',(item_dict['morpheme'][i],index))
                    index += 1
                    parser.append((item_dict['morpheme'][i],'how'))
                elif particle in why:
                    abstract_append(abstract,'why',(item_dict['morpheme'][i],index))
                    index += 1
                    parser.append((item_dict['morpheme'][i],'why'))
    return abstract, parser, stats

def element_generator(input_type,input_data):
    element = {}
    element['type'] = input_type
    element['data'] = input_data
    return element

def query_interpreter(query):
    new_query = {
        "intent_type" : "",
        "element": {
            "main": {},
            "sub": {},
            "main_expression": {},
            "variable": {},
            "value": {}
        }
    }
    if query['query_type']:
        new_query['intent_type'] = query['query_type']
        if new_query['intent_type'] == 'component':
            new_query['element']['main'] = query['element'][0]
            new_query['element']['sub'] = query['element'][1]
            return new_query
        elif new_query['intent_type'] == 'implication':
            new_query['element']['main'] = query['element'][0]
            new_query['element']['sub'] = query['element'][1]
            return new_query
        elif new_query['intent_type'] == 'logic':
            new_query['element']['main'] = query['element'][0]
            new_query['element']['main_expression'] = query['element'][1]
            return new_query
        elif new_query['intent_type'] == 'action':
            key = ['main','main_expression','variable','value']
            for i in range(len(query['element'])):
                new_query['element'][key[i]] = query['element'][i]
            return new_query
    new_query['intent_type'] = "unidentified intent"
    return query

def nlu_result(question):
    question, expressions = expression_process(question)
    result = mecab_process(question)
    abstract, parser, stats = abstract_generator(result, expressions)
    query = {}
    query['element'] = []
    if stats['Expression'] == 0:
        if stats['UK'] == 0:
            #input NULL
            print("질문의 의도가 파악되지 않습니다.")
            query['query_type'] = ""
            return query_interpreter(query)
        elif stats['UK'] == 1:
            #Component
            query['query_type'] = "component"
            if stats['Component'] > 0:
                print('{}의 {}를 물어보셨습니다.'.format(abstract['UK'][0][0],abstract['Component'][-1][0]))
                query['element'].append(element_generator('unit_knowledge',abstract['UK'][0][0]))
                query['element'].append(element_generator('component',abstract['Component'][-1][0]))
                return query_interpreter(query)
            else:
                print('{}의 정의를 물어보셨습니다.'.format(abstract['UK'][0][0]))
                query['element'].append(element_generator('unit_knowledge',abstract['UK'][0][0]))
                query['element'].append(element_generator('component','정의'))
                return query_interpreter(query)
        else:
            #Relation
            query['query_type'] = "implication"
            uk = [item[0] for item in abstract['UK']]
            print('{}의 개념에 {}(이)가 포함되는지를 물어보셨습니다.'.format(uk[-1],uk[-2]))
            query['element'].append(element_generator('unit_knowledge',uk[-1]))
            query['element'].append(element_generator('unit_knowledge',uk[-2]))
            return query_interpreter(query)

    elif stats['Expression'] == 1:
        if stats['UK'] == 0:
            #input NULL
            #or simplify(expression)
            query['query_type'] = ""
            print("{}을 간단히 해달라는 말씀이신가요?".format(abstract['Expression'][0][0]))
            return query_interpreter(query)
        else:
            expression_josa = abstract['Expression'][0][1] + 1
            if expression_josa < len(parser) and parser[expression_josa][1] in ['JKS','JX']: #[은,는,이,가,도]
                #logic
                print('{}이 {}인지 물어보셨습니다.'.format(abstract['Expression'][0][0],abstract['UK'][-1][0]))
                query['query_type'] = "logic"
                query['element'].append(element_generator('unit_knowledge',abstract['UK'][-1][0]))
                query['element'].append(element_generator('expression',abstract['Expression'][0][0]))
                return query_interpreter(query)
            else:
                #action
                print("{}의 {}을 물어보셨습니다.".format(abstract['Expression'][0][0],abstract['UK'][-1][0]))
                query['query_type'] = "action"
                query['element'].append(element_generator('unit_knowledge',abstract['UK'][-1][0]))
                query['element'].append(element_generator('expression',abstract['Expression'][0][0]))
                return query_interpreter(query)
    else: # if Expr >= 2
        if stats['UK'] == 0:
            #input NULL
            #or simplify
            query['query_type'] = ""
            print("{}을 간단히 해달라는 말씀이신가요?".format(abstract['Expression'][0][0]))
            return query_interpreter(query)
        else:
            for i in range(len(parser)-1):
                if parser[i][1] == 'Expression' and parser[i+1][1] in ['JKS','JX']:
                    #logic
                    print('{}이 {}인지 물어보셨습니다.'.format(parser[i][0],abstract['UK'][-1][0]))
                    query['query_type'] = "logic"
                    query['element'].append(element_generator('unit_knowledge',abstract['UK'][-1][0]))
                    query['element'].append(element_generator('expression',parser[i][0]))
                    return query_interpreter(query)
            #if not returned
            #action
            query['query_type'] = "action"
            query['element'].append(element_generator('unit_knowledge',abstract['UK'][-1][0]))
            for i in range(len(parser)-1):
                if parser[i][1] == 'Expression' and parser[i+1][1] in ['JKB']:
                    query['element'].append(element_generator('expression',parser[i][0]))
            for i in range(len(parser)-1):
                if parser[i][1] == 'Expression' and parser[i+1][1] not in ['JKB']:
                    query['element'].append(element_generator('expression',parser[i][0]))
            if parser[-1][1] == 'Expression':
                query['element'].append(element_generator('expression',parser[-1][0]))
            print("{}에 대한 {}의 action을 요청하셨습니다.".format(query['element'][1]['data'],query['element'][0]['data']))
            return query_interpreter(query)


if __name__ == '__main__':
    # question = "선생님, 등식의 성질이 뭔가요?"
    # question = "선생님, 방정식이 등식일까요?"
    # question = "$2x$"
    # question = "선생님, $x + 0$에서 $0$가 상수항이 아닌가요?"
    # question = "쌤~ $3x+4y-5$에서 상수항이 머죠?"
    question = "$3x - 4y -5$에서 $x$의 계수는 뭘까요?"
    # question = "쌤! $2x + 3y -2 + 5z$에서 $6$을 $x$에 대입하면 어떻게 되나요?"
    # question = "하이하이 $4$를 $x+3$에서 $x$에 대입하면 결과는?"
    query = nlu_result(question)
    print(query)
