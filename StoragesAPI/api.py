

import psutil
from flask import Flask , request , jsonify


from helper import is_password,is_bot,is_session,sorting_update_messages
from db.db import DB


api = Flask(__name__)

@api.route('/free_space',methods=['POST','GET'])
def get_free_space():
    
    if request.method == 'GET':
        try:
            password = request.get_json()['password']
        except:
            return "json must have 'password' key!"
        if is_password(password):
            return f"{psutil.disk_usage("C:").free / (1024**3):.3f}"
        else:
            return f"Password Wrong!({password})"
        
@api.route('/add_bot',methods=['POST','GET'])
def add_bot():
    if request.method == 'POST':
        try:
            data = request.get_json()
        except:
            return "you must send an json!"
        try:
            password = data['password']
        except:
            return "json must have 'password' key!"
        if is_password(password):
            try:
                bot_username = data['bot_username']
            except:
                return "json must have 'bot_username' key!"
            if is_bot(bot_username):
                try:
                    session_id = data['session_id']
                except:
                    return "json must have 'session_id' key"
                if is_session(bot_username,session_id):
                    return jsonify({"status":"OK","message":"session_id now in on server!"})
                else:
                    DB.add_session_to_client(bot_username,session_id)
                    return jsonify({"status":"OK","message":"session has been added to client!"})
            else:
                DB.add_bot_client(bot_username)
                return jsonify({"status":"OK","message":"bot client add now request for create session"})
        else:
            return f"Password Wrong!({password})"
    else:
        return "method must be post not get!"

@api.route("/update/sorting_messages",methods=['POST','GET'])
def sorting_messages():
    
    if request.method == 'POST':
        try:
            data = request.get_json()
        except:
            return "you must send an json!"
        try:
            bot_username = data['bot_username']
        except:
            return "json must have 'bot_username' key!"
        try:
            messages = data['messages']
        except:
            return "json must have 'messages' key!"
        sorted_messages = sorting_update_messages(bot_username,messages)
        return sorted_messages
    else:
        return "method must be post not get!"

@api.route("/update/sorting_message",methods=['POST','GET'])
def sorting_message():
    
    if request.method == 'POST':
        try:
            data = request.get_json()
        except:
            return "you must send an json!"
        try:
            message = data['message']
        except:
            return "json must have 'message' key!"
          
    else:
        return "method must be post not get!"








if __name__ =="__main__":
    api.run(debug=True)