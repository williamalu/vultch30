"""
Interface for the mongo database
"""

from pymongo import MongoClient
from datetime import datetime

class Database():
	"""
	Create a mongo client inst and connect to the db
	"""
	def __init__(self, uri, database):
		print "Connecting to mongo ..."
		self.client = MongoClient(uri)
		self.db = self.client[database]
		self.collections = self.db.collection_names()
		print "Mongo connected"
		print "Database: %s" % database
		print "Collections: %s" % self.collections


	"""
	Print out the contents of a collection for debugging
	"""
	def printCollection(self, collectionName):
		collection = self.db[collectionName]
		cursor = collection.find({}) 
		for doc in cursor:
			print doc
			print '\n'


	"""
	Add a new user profile
	"""
	def newUser(self, username, email, password):
		# Get collection to write to
		usersCollection = self.db['users']
		
		# Assemble profile
		onboard = datetime.now()
		profile = {'_id': username,
				'pass': password,
				'email': email,
				'onboard': onboard,
				'type': 'player',
				'clubs': [],
				'teams': [],
				'stats': {}}

		# Insert profile into collection
		try:
			usersCollection.insert(profile, safe=True)
		except pymongo.errors.DuplicateKeyError, e:
			print "User already exists: %s" % e


	"""
	Authenticate a user login
	"""
	def userAuth(self, user, givenPass):
		pass
