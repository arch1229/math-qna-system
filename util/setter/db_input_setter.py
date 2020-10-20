def db_input_setter(task, master, slave):
	
	input_data = {}
	input_data["task"] = task
	if task == "component":
		input_data["unit_knowledge"] = master
		input_data["component"] = slave["data_en"]
	
	elif task == "implication": 
		input_data["unit_knowledge_master"] = master
		input_data["unit_knowledge_slave"] = slave

	

	return input_data