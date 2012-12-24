import datetime

class page(object):
	def __init__(self, api):
		self.api = api
	
	def color(self):
		return 'red' if self.api.isToasting == True else 'black'
		
	def answer(self):
		return 'Yes.' if self.api.isToasting == True else 'No.'
		
	def date(self):
		return datetime.date.fromtimestamp(self.api.started()//1000).strftime("%B %d, %Y")
		
	def count(self):
		return self.api.toastCount()