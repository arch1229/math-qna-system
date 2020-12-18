import logging
import json
from _constant._string import ASK_TYPE

def dummy_db_getter(url, query):
	# TODO: 나중엔 쿼리엔진에 REST API를 fetch하는 코드를 db_getter 함수에 
	logger = logging.getLogger("dummy_db_getter")

	db_json_data = json.load(open(url, 'r', encoding='UTF8'))
	task = query["task"]
	result = {
		"result_type": "db_success",
		"message": "db_success"
	}

	try:
		if task == ASK_TYPE["KNOWLEDGE"]:
			unit_knowledge = query["uk"]
			attribute = query["attribute"]
			query_result = db_json_data[unit_knowledge][attribute]["content"]
			result["message"] = query_result

		elif task == ASK_TYPE["RELATION"]:
			unit_knowledge_master = query["unit_knowledge_master"]
			unit_knowledge_slave = query["unit_knowledge_slave"]
			master_child = db_json_data[unit_knowledge_master]["child"]
			
			logger.debug("master_child: "+ str(master_child))
			logger.debug("unit_knowledge_slave: "+ str(query["unit_knowledge_slave"]))
			if query["unit_knowledge_slave"] in master_child or \
				unit_knowledge_master == unit_knowledge_slave:
				query_result = "true"	
			else : 
				query_result = "false"

			result["message"] = query_result

	except Exception as e:
		logger.info(e)
		result["result_type"] = "db_fail"
		result["message"] = e

	return result


def db_getter(url, query):
	# TODO: Query engine
	# 우리의 쿼리엔진으로 할때는 여기에 짜주세요.
	pass