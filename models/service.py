import os.path
import time
import json
import response
from sqlalchemy import *

class service(object):
	def __init__(self, store):
		self.db = create_engine(store, echo=False)
		metadata = MetaData(self.db)
		
		self.users = Table('users', metadata, autoload=True)
		self.records = Table('records', metadata, autoload=True)
	
	def modified(self):
		row = self.db.execute("select start, finish from records order by start desc, finish desc limit 1").fetchone()
		start = row['start']
		end = row['finish']
		return start if (end is None or start > end) else end
		
	def started(self):
		return (self.db.execute("select start from records order by start asc, finish asc limit 1").fetchone())['start']
		
	def get(self, user=None):
		return response.response(response.STATUS, {'status': self.toastStatus(), 'count': int(self.toastCount()), 'last': self.modified(), 'started': self.started()}).json()
		
	def toastStatus(self):
		row = self.db.execute("select start, finish from records order by start desc, finish desc limit 1").fetchone()
		if row['finish'] is None:
			return True
		else:
			return False
	
	def toastCount(self):
		return (self.db.execute("select count(*) as toastCount from records").fetchone())['toastCount'];
		
	def on(self, key=None):
		return self.set(key=key, toasting='on')
		
	def off(self, key=None):
		return self.set(key=key, toasting='off')
		
	def reset(self, key=None):
		return self.set(key=key, toasting='reset')
		
	def set(self, key=None, toasting=None):
		errors = []
		toasting = toasting.lower()
		js = ''
		if key == None:
			errors.append('Empty key.')
		
		keyrow = self.db.execute("select * from users where secret = '" + key.upper() + "' limit 1").fetchone();
		
		if keyrow == None:
			errors.append('Invalid key.')
		else:
			name = keyrow['name']
		
		if toasting == None:
			errors.append('Empty toasting command.')
		elif toasting != 'on' and toasting != 'off' and toasting != 'reset':
			errors.append('Invalid toasting command.')
		
		if len(errors) > 0:
			js = response.response(response.ERROR, errors).json()
		else:
			if toasting == 'reset':
				self.db.execute("delete from records")
			else:
				timing = str(time.localtime())
				if toasting == 'on':
					self.records.insert().execute(user='Adam', start=timing)
				else:
					row = self.db.execute("select rowid from records order by start desc, finish desc limit 1").fetchone()
					id = row['rowid']
					self.db.execute("update records set finish = '" + timing + "' where rowid = " + id)
			js = response.response(response.SUCCESS, {"toasting": toasting, "effective:": timing}).json()
		return js