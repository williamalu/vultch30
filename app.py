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
		res = database.newUser(username, email, password)

		if res == "Duplicate":
			warn = "That username is already taken.  Please choose another."
			return render_template('index.html', warning=warn)

		print "New profile created for %s" % username
		return render_template('login.html')
	else: 
		warn = "Some fields were left blank. Please try again."
		return render_template('index.html', warning=warn)


"""
Handle user authentication
"""
@app.route('/userAuth', methods=['POST'])
def userAuth():
	# Check that both fields were filled
	user = request.form['username']
	password = request.form['password']
	
	if user and password:
		res = database.userAuth(user, password)
		if res == "Not Found":
			warn = "That username does not exist.  Please try again or create a profile."
			return render_template('login.html', warning=warn)
		elif res == "Incorrect":
			warn = "Incorrect password.  Please try again." 
			return render_template('login.html', warning=warn)
		else: 
			return render_template('main.html')
	else:
		warn = "Some fields were left blank.  Please try again."
		return render_template('login.html', warning=warn)


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
	
