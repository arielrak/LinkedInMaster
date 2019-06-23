'''
Created on Jun 19, 2019

@author: ariel
'''

import json
import db_interface
import parse_interface
import user


def _format_results(results):
    json_of_users = ""    
    for result in results:
        new_user = user.User()
        new_user.create_user_from_dict(result)
        if json_of_users is not "":
            json_of_users+=","
        json_of_users+=json.dumps(new_user.to_dict()) 
    json_of_users += "]"
    json_of_users = "["+json_of_users
    
    return json_of_users

# Accepts a dictionary of valid and invalid query terms
def handle_query(query_terms):
    with db_interface.DBInstance() as db:
        results = db.query(query_terms) 
    
    return _format_results(results)

def handle_add_new_user(url):
    try:
        parser = parse_interface.LinkedInParser(url)
        new_user = user.User()
        new_user.set_name(parser.get_name())
        new_user.set_title(parser.get_title())
        new_user.set_position(parser.get_position())
        new_user.set_summary(parser.get_summary())
        new_user.set_skills(parser.get_skills())
        new_user.set_experience(parser.get_experience())
        new_user.set_education(parser.get_education())
        with db_interface.DBInstance() as db:
            db.new_user(new_user.to_dict())
        return "Success"
    except Exception as e:
        e = str(e)
        return "An error occurred: "+e
        
    
    