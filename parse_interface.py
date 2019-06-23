from Naked.toolshed.shell import muterun_js
import yaml

class LinkedInParser:
    
    # Accepts URL of a public LinkedIn page
    def __init__(self, url):
        print("Fetching data. Please wait...")
        
        raw_data = muterun_js('scraper.js', url)
        
        print("Done fetching data.")
        
        # Handle error executing script
        if raw_data.exitcode != 0:
            print(raw_data.exitcode)
            raise RuntimeError("Error executing node script: ",raw_data.exitcode)
            return
        
        raw_data = raw_data.stdout
        data = self._clean_data(raw_data)
        self._find_useful_fields(data)
        
    def _clean_data(self, raw_data):
        raw_data = raw_data.decode('utf-8')
        raw_data = raw_data.replace("\'","\"")
        raw_data = raw_data.replace("\n", "")
        raw_data = raw_data.replace("\'","\"")
        raw_data = raw_data.replace("\xe2\x80\x93", "-")
        # TODO yaml.load deprecated, update
        raw_data = yaml.load(raw_data)
        return raw_data

    def _find_useful_fields(self, data):
        self.name = self._find('name', data)
        self.title = self._find('positions', data)[0]["title"]
        self.current_position = self._find('positions', data)[0]
        self.summary = self._find('summary', data)
        self.skills = self._find('skills', data)
        self.experience = self._find('positions', data)
        self.education = self._find('educations', data)

    # Recursive method for finding the first instance of a key in a nested dict
    # Adapted from Stack Overflow:s https://tinyurl.com/y4qmzdj3   
    def _find(self, target_key, dictionary):
        if target_key in dictionary: return dictionary[target_key]
        for _ , value in dictionary.items():
            if isinstance(value,dict):
                return self._find(target_key, value)
            
    def get_name(self):
        return str(self.name)
         
    def get_title(self):
        return str(self.title)
        
    def get_position(self):
        return str(self.current_position)
        
    def get_summary(self):
        return str(self.summary)
        
    def get_skills(self):
        return str(self.skills)
        
    def get_experience(self):
        return str(self.experience)
        
    def get_education(self):
        return str(self.education)