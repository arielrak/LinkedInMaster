'''
Created on Jun 20, 2019

@author: ariel
'''

import user
import db_interface

def delete_DB():
    db_interface.debug_self_destruct()

def create_some_users():
    print("\n-----Create Users--------\n")
    user1 = user.User()
    user1.create_user_from_dict({"name": "Bob", "skills":"Working hard", "summary":"Princeton"})
    user2 = user.User()
    user2.create_user_from_dict({"name": "Tim", "skills":"Working hard", "summary":"Princeton"})
    user3 = user.User()
    user3.create_user_from_dict({"name": "Jane", "skills":"Hardly working", "summary":"Columbia"})
    user4 = user.User()
    user4.create_user_from_dict({"name": "Jill", "skills":"aidoc", "summary":"IDF"})
    user5 = user.User()
    user5.create_user_from_dict({"name":"Ariel", "skills":"listening to music"})
    with db_interface.DBInstance() as db:
        db.new_user(user1.to_dict())
        db.new_user(user2.to_dict())
        db.new_user(user3.to_dict())
        db.new_user(user4.to_dict())
        db.new_user(user5.to_dict())
        db.debug_print()

def test_add_new_partial_user():
    print("\n------Add New Partial User-------\n")
    my_user = user.User()
    my_user.create_user_from_dict({"name":"Ariel", "skills":"Working hard, listening to music"})
    with db_interface.DBInstance() as db:
        db.new_user(my_user.to_dict())
        db.debug_print()
        
def test_get_user_by_name():
    print("\n-------Get User By Name------\n")
    with db_interface.DBInstance() as db:
        user_list = db.query_user_by_name("ari")
        for entry in user_list:
            print(entry)
            
def test_get_user_by_skill():
    print("\n-------Get User By Skill------\n")
    with db_interface.DBInstance() as db:
        user_list = db.query_user_by_skills("music")
        for entry in user_list:
            print(entry)

def test_general_query():
    print("\n-------General Query------\n")
    with db_interface.DBInstance() as db:
        user_list = db.query({"skills":"work"})
        for entry in user_list:
            print(entry)
    