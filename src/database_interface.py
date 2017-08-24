"""
Interface for the mongo database
"""

from pymongo import MongoClient

class Database():
	"""
	Create a mongo client inst and connect to the db
	"""
	def __init__(self, uri, database):
		print "Connecting to mongo ..."
		self.client = MongoClient(uri)
		self.db = self.client[database]


	"""
	Add a new user profile
	"""
	def newUser(self, username, email, password):
		pass


	"""
	Authenticate a user login
	"""
	def userAuth(self, user, givenPass):
		pass
		
		
