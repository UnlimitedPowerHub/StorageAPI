

import json


db_file = 'data/db.json'
utf8 = "utf-8"


class DB:
    
    @staticmethod
    def load():
        
        with open(db_file,'r',encoding=utf8) as file:
            return json.load(file)
        
    @staticmethod
    def save(data):
        
        with open(db_file,'w',encoding=utf8) as file:
            json.dump(data,file,indent=4)
    
    @staticmethod
    def get_apis():
        
        return DB.load()
    
    @staticmethod
    def add_api(api_data):
        
        db_data = DB.load()
        
        apidata = {
            "link": api_data['link'],
            "free_space": api_data['space']
        }
        
        db_data[str(api_data['name'])] = apidata
        
        DB.save(db_data)
    
    @staticmethod
    def get_api_link(api_name):
        
        return DB.load()[str(api_name)]['link']
        
    @staticmethod
    def get_api_free_space(api_name):
        
        return DB.load()[str(api_name)]['free_space']
    
    @staticmethod
    def remove_api(api_name):
        
        api_data = DB.load()
        
        del api_data[str(api_name)]
        
        DB.save(api_data)


