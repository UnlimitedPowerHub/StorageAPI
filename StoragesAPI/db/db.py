

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
        
        with open(db_file,'w',encoding='utf-8') as file:
            json.dump(data,file,indent=4)
        
    @staticmethod
    def get_password():
        
        return DB.load()['password']
    
    @staticmethod
    def get_bots():
        
        return DB.load()['clients']
            
    
    @staticmethod
    def add_bot_client(bot_username):
        
        db_data = DB.load()
        
        bot_data = {
            'sessions':{},
            'messages':{}
        }
        
        db_data['clients'][str(bot_username)] = bot_data
        
        DB.save(db_data)
        
    @staticmethod
    def get_messages_from_client(bot_username):
                
        return DB.load()['clients'][str(bot_username)]['messages']
    
    @staticmethod
    def get_sessions_from_client(bot_username):
        
        return DB.load()['clients'][str(bot_username)]['sessions']
        
    @staticmethod
    def add_message_to_client(bot_username,message):
        
        db_data = DB.load()
        
        db_data['clients'][str(bot_username)]['messages'][str(message['id'])] = message
        
        DB.save(db_data)
        
    @staticmethod
    def add_session_to_client(bot_username,session):
        
        db_data = DB.load()
        
        db_data['clients'][str(bot_username)]['sessions'] = session
        
        DB.save(db_data)
        
    @staticmethod
    def remove_session_from_client(bot_username,session_id):
        
        db_data = DB.load()
        
        del db_data['clients'][str(bot_username)]['sessions'][str(session_id)]
        
        DB.save(db_data)