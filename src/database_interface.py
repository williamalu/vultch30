"""
Interface for the mongo database
"""

import pymongo
import json
import bcrypt
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
			print json.dumps(doc, sort_keys=True, indent=4)
			print '\n'


	"""
	Delete all documents in a collection
	"""
	def deleteCollectionContents(self, collectionName):
		collection = self.db[collectionName]
		collection.delete_many({})
		
		print "Deleted contents of collection %s" % collectionName


	"""
	Add a new user profile
	"""
	def newUser(self, username, email, password):
		# Get collection to write to
		usersCollection = self.db['users']
		
		# Hash the password
		hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

		# Assemble profile
		onboard = datetime.now()
		onboard = onboard.strftime('%m/%d/%Y')
		profile = {'_id': username,
				'pass': hashed,
				'email': email,
				'onboard': onboard,
				'type': 'player',
				'clubs': [],
				'teams': [],
				'stats': {}}

		# Insert profile into collection
		try:
			usersCollection.insert(profile)
			return "Success"
		except pymongo.errors.DuplicateKeyError, e:
			return "Duplicate"


	"""
	Authenticate a user login
	"""
	def userAuth(self, user, givenPass):
		# Find the user's profile
		userProfile = self.db['users'].find_one({'_id': user})
		givenPass = givenPass.encode('utf-8')

		if userProfile:
			profilePass = userProfile['pass']
			# Check password
			if bcrypt.checkpw(givenPass, profilePass.encode('utf-8')):
				return "Authenticated"
			else:
				return "Incorrect"
		else:
			return "Not Found"
