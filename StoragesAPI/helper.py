
from db.db import DB

def is_password(password):
    
    return bool(str(password) == str(DB.get_password()))

def is_bot(bot_username):
    
    return bool(str(bot_username) in DB.get_bots())

def is_session(bot_username,session_id):
    
    return  bool(str(session_id) in DB.get_sessions_from_client(bot_username))


def sorting_update_messages(bot_username,messages):
    
    msg = {
        'id': None,
        'text': None,
        'time': None
    }
    
    for message in messages:
        
        msg['id'] = message['id']
        msg['text'] = message['text']
        msg['time'] = message['time']
        
        DB.add_message_to_client(bot_username,msg)
        
        