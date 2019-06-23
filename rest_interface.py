'''
Created on Jun 19, 2019

@author: ariel
'''

from flask import Flask, request
import interactor

app = Flask(__name__)
        
# Generate a JSON list of users with the specified attributes
@app.route('/api/query', methods=['GET'])
def find_user_by_general_query():
    # Build a dictionary of  search terms
    return interactor.handle_query(request.args) 
    
    
# Decided to use a GET request here to save some 
# time and avoid parsing the request body of a PUSH request    
@app.route('/api/add', methods=['GET'])
def create_new_user():  
    return interactor.handle_add_new_user(request.args["url"])

# Just for fun
@app.route('/api/cookie', methods=['GET'])
def cookie():
    return "<html><img src='https://media0.giphy.com/media/EKUvB9uFnm2Xe/giphy.gif'></html>"