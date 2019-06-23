'''
Created on Jun 23, 2019

@author: ariel
'''

import rest_tester
import db_tester
import parser_tester

# Rest Tester
print("Testing Query -- REST API")
rest_tester.test_query()
print("Testing Create User -- REST API")
rest_tester.test_create_user()
print("Testing Cookie -- REST API")
rest_tester.test_cookie()

# DB Tester
print("Testing Create Users -- DB")
db_tester.create_some_users()
print("Test General DB Query -- DB")
db_tester.test_general_query()

# Parser Test
print("Testing Basic Query -- Parser")
parser_tester.test_basic_query()