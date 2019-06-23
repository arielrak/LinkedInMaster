'''
Created on Jun 19, 2019

@author: ariel
'''

class User:
    
    def __init__(self):
        self.set_name("")
        self.set_title("")
        self.set_position("")
        self.set_summary("")
        self.set_skills("")
        self.set_experience("")
        self.set_education("")
    
    def set_name(self, name):
        self.name = name
         
    def set_title(self, title):
        self.title = title
        
    def set_position(self, position):
        self.position = position
        
    def set_summary(self, summary):
        self.summary = summary
        
    def set_skills(self, skills):
        self.skills = skills
        
    def set_experience(self, experience):
        self.experience = experience
        
    def set_education(self, education):
        self.education = education
    
    def get_name(self):
        return self.name
         
    def get_title(self):
        return self.title
        
    def get_position(self):
        return self.position
        
    def get_summary(self):
        return self.summary
        
    def get_skills(self):
        return self.skills
        
    def get_experience(self):
        return self.experience
        
    def get_education(self):
        return self.education
    
    # TODO Make this based on something real
    # Score is based on third letter of name, a scientifically
    # proven indicator of talent
    def get_score(self):
        if self.name is not None and len(self.name)>2:
            return ord(self.name[2])-ord('a')
        else:
            return 0
        
        
    def to_dict(self):
        user_dict = {"name":self.get_name(),
                     "title":self.get_title(),
                     "position":self.get_position(),
                     "summary":self.get_summary(),
                     "skills":self.get_skills(),
                     "experience":self.get_experience(),
                     "education":self.get_education(),
                     "score":self.get_score()}
        return user_dict
    
    def create_user_from_dict(self, user_dict):
        if("name" in user_dict):
            self.set_name(user_dict["name"])
        if("title" in user_dict):
            self.set_title(user_dict["title"])
        if("position" in user_dict):
            self.set_position(user_dict["position"])
        if("summary" in user_dict):
            self.set_summary(user_dict["summary"])
        if("skills" in user_dict):
            self.set_skills(user_dict["skills"])
        if("experience" in user_dict):
            self.set_experience(user_dict["experience"])
        if("education" in user_dict):
            self.set_education(user_dict["education"])
        
        
        
        
        
        
        