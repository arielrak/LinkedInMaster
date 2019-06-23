'''
Created on Jun 23, 2019

@author: ariel
'''

import requests

def test_query():
    request = requests.get("http://127.0.0.1:5000/api/query")
    print(request.text)

def test_create_user():
    request = requests.get("http://127.0.0.1:5000/api/add?url='https://www.linkedin.com/in/bob-sherwood-8ba7b28/'")
    print(request.text)
    assert(request.text == "Success")
    
def test_cookie():
    request = requests.get("http://127.0.0.1:5000/api/cookie")
    print(request.text)
    assert(request.text == "<html><img src='https://media0.giphy.com/media/EKUvB9uFnm2Xe/giphy.gif'></html>")
