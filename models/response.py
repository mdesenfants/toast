import json

ERROR = 'error'
STATUS = 'status'
SUCCESS = 'success'

class response(dict):
	def __init__(self, type, data):
		self['type'] = type
		self['data'] = data
	
	def json(self):
		return json.dumps(self)