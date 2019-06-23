'''
Created on Jun 20, 2019

@author: ariel
'''
import parse_interface 
import user 

def test_basic_query():
    parser = parse_interface.LinkedInParser("https://www.linkedin.com/in/hwicheong")
    new_user = user.User()
    new_user.set_name(parser.get_name())
    new_user.set_title(parser.get_title())
    new_user.set_position(parser.get_position())
    new_user.set_summary(parser.get_summary())
    new_user.set_skills(parser.get_skills())
    new_user.set_experience(parser.get_experience())
    new_user.set_education(parser.get_education())
    print(new_user.to_dict())
    
