## API Usage: 

To run:
1. Navigate to project directory
1. Execute npm i scrapedin
1. Execute pip install naked
1. Execute pip install flask
1. Execute: export FLASK_APP=./rest_interface.py
1. Execute: flask run

## Endpoints:

http://localhost:5000/api/query?[attr=]
	Query users in the system by attribute
	Available search terms are:
		name, title, position, summary, skills
	Example: http://localhost:5000/api/query?name=Ariel&skills='ABCs'
	
http://localhost:5000/api/add?url=
	Add a LinkedIn Profile by url
	
http://localhost:5000/api/cookie
	Try it and find out!

## Implementation Details:

	sqllite3 used for backend. Simply a file stored on the device. 
	Because all database logic is written in SQL, this can be easily 
	scaled up to a production server.
	
	Flask to implement the REST API
	
	Naked to run a Node.js script from a python script. Node.js 
	script is the LinkedIn scraper.
	Credits to https://github.com/linkedtales/scrapedin
	
	API returns information, for the most part, as JSON