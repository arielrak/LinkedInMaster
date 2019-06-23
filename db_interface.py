'''
Created on Jun 19, 2019

@author: ariel
'''

import sqlite3
import os


def debug_self_destruct():
        os.remove("sqlite3_db")

class DBInstance:
    
    def __enter__(self):
        
        # Does DB exist?
        DB_did_exist = os.path.isfile('sqlite3_db')
        
        self.db = sqlite3.connect('sqlite3_db')
        self.db_cursor = self.db.cursor()
        
        # If DB did not exist, create user table
        if not DB_did_exist:
            self.db_cursor.execute('''CREATE TABLE users
                (name text, title text, position text, 
                summary text, skills text, experience text, 
                education text)''')

        return self    
    
    def __exit__(self, *exc):
        self.db.commit()
        self.db.close()
        pass
        
    # User info must be in the form of dictionary object
    def new_user(self, user):
        user_info_list=[]
        accepted_fields = ["name", "title", "position", 
                           "summary", "skills", "experience", 
                           "education"]
        for key , value in user.items():
            if key in accepted_fields:
                user_info_list.append(value)
        self.db_cursor.execute('''INSERT INTO users VALUES 
            (?,?,?,?,?,?,?)''', user_info_list)
        
    # Query terms must be in the form of a dictionary object
    # Query terms do not have to be real user attributes stored in DB
    # These unsupported terms do nothing    
    def query(self, query_terms):
        formatted_terms_list = self._format_query_terms(query_terms)
        
        self.db_cursor.execute('''SELECT * FROM users 
            WHERE name LIKE (?) 
            AND title LIKE (?) 
            AND position LIKE (?) 
            AND summary LIKE (?) 
            AND skills LIKE (?)
            ''', formatted_terms_list)
        
        return self._package_and_return_results_of_query(self.db_cursor.fetchall())
        
    def _format_query_terms(self, query_terms):
        formatted_terms = {}
        formatted_terms_list = []
        if "name"  in query_terms:
            formatted_terms["name"] = "%"+query_terms["name"]+"%"
        else:
            formatted_terms["name"]="%"
        if "title"  in query_terms:
            formatted_terms["title"] = "%"+query_terms["title"]+"%"
        else:
            formatted_terms["title"]="%"
        if "position"  in query_terms:
            formatted_terms["position"] = "%"+query_terms["position"]+"%"
        else:
            formatted_terms["position"]="%"
        if "summary"  in query_terms:
            formatted_terms["summary"] = "%"+query_terms["summary"]+"%"
        else:
            formatted_terms["summary"]="%"
        if "skills"  in query_terms:
            formatted_terms["skills"] = "%"+query_terms["skills"]+"%"
        else:
            formatted_terms["skills"]="%"
        
        for _ , value in formatted_terms.items():
            formatted_terms_list.append(value)  
            
        return formatted_terms_list
        
    def _package_and_return_results_of_query(self, query_list):
        categories_list = ["name","title","position","summary","skills","experience","education"]
        list_of_dicts = []
        for row in query_list:
            list_of_dicts.append(dict(zip(categories_list, row)))
        return list_of_dicts
    
    
    # Print all contents of DB, useful for debugging but not production    
    def debug_print(self):
        print("Printing!")
        for row in self.db_cursor.execute('SELECT * FROM users ORDER BY name'):
            print(row)
        pass

        
    