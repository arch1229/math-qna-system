import logging
import json

logger = logging.getLogger("inference_engine/db_caller")
stream_hander = logging.StreamHandler()
logger.addHandler(stream_hander)
LOGGING_LEVEL = logging.DEBUG
logger.setLevel(LOGGING_LEVEL)

def dummy_db_getter(url, query):
	db_json_data = json.load(open(url, 'r', encoding='UTF8'))
	task = query["task"]
	result = {
		"result_type": "db_success",
		"message": "db_success"
	}

	try:
		if task == "component":
			unit_knowledge = query["unit_knowledge"]
			component = query["component"]
			query_result = db_json_data[unit_knowledge][component]["content"]

			result["message"] = query_result

		elif task == "implication":
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
		logger.debug(e)
		result["result_type"] = "db_fail"
		result["message"] = e

	return result

def db_getter(url, query):
	pass