'''
NOT USING THIS MODULE ANYMORE, WILL BE DELETED SOON
'''

import json
from json import JSONEncoder

class BnfJson:
	def __init__(self):
		self.expr = ''
		self.expr_type = ''
		self.expr_n = ''
		self.expr_elem = []


	def reader(self, bnf_json_data):
		self.expr = bnf_json_data['expr']
		self.expr_type = bnf_json_data['expr_type']
		self.expr_n = bnf_json_data['expr_n']
		self.expr_elem = bnf_json_data['expr_elem']


class BnfJsonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
