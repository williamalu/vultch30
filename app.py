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
Handle new user request and send to login page
"""
@app.route('/newUser', methods=['POST'])
def newUser():
	username = request.form['username']
	email = request.form['email']
	password = request.form['password']

	print username

	return render_template('main.html')


if __name__ == "__main__":
	# Read the config file
	try:
        	config = yaml.load('config.yml', 'r')
	except yaml.YAMLError, exc:
        	print "Error in configuration file: %s" % exc

	uri = config['mongo']['uri']
	database = config['mongo']['database']

	if uri and database:
		# Set up the database and run the app
		database = database_interface.Database(uri, database)
		app.run(debug=True)
	else:
		print "Error loading mongo config values"
	
