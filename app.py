"""
Main Vultch30 Flask App
"""

# External imports
from flask import Flask
from flask import render_template, request, session
import yaml

# Internal imports
from src import database_interface

# Create app and database
app = Flask(__name__)
database = None

"""
Inital page with new user creation
"""
@app.route('/')
def home():
	return render_template('index.html')


"""
Login page
"""
@app.route('/login')
def login():
	return render_template('login.html')


"""
Handle new user request and send to login page
"""
@app.route('/newUser', methods=['POST'])
def newUser():
	# Check that all fields were filled
	username = request.form['username']
	email = request.form['email']
	password = request.form['password']

	if username and email and password:
		database.newUser(username, email, password)
		print "New profile created for %s" % username

		return render_template('login.html')
	else: 
		# TODO: Throw some sort of blank fields warning to the user
		return render_template('index.html')


"""
Handle user authentication
"""
@app.route('/auth', methods=['POST'])
def userAuth():
	# Check that both fields were filled
	user = request.form['username']
	password = request.form['password']
	
	if user and password:
		res = database.userAuth(user, password)
		if res == "Not Found":
			# TODO: Tell user to make a profile
			return render_template('login.html')
		elif res == "Incorrect":
			# TODO: Tell the user their pass was incorrect
			return render_template('login.html')
		else: 
			return render_template('main.html')
	else:
		# TODO: Throw some sort of blank fields warning to the user
		return render_template('login.html')


if __name__ == "__main__":
	# Read the config file
	uri = ''
	database = ''
	try:
		with open('config.yml', 'r') as f:
        		config = yaml.load(f)
			uri = config['mongo']['uri']
			database = config['mongo']['database']
	except yaml.YAMLError, exc:
        	print "Error in configuration file: %s" % exc

	if uri and database:
		# Set up the database and run the app
		database = database_interface.Database(uri, database)
	
		# database.deleteCollectionContents('users') # DEBUGGING	
		database.printCollection('users') # DEBUGGING
	
		app.run(debug=True)
	else:
		print "Error loading mongo config values"
	
