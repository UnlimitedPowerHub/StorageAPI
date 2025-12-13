import psutil
from flask import Flask , request , jsonify

from db.client import *

api = Flask(__name__)

passw = "password"

def is_password(password_):
    return bool(str(password_) == str(passw))

def addMessages(bid,messages):
    for message in messages:
        addMessageToBot(bid,message)
    return getBotMessages(bid)

@api.route('/vBeta/getFreeSpace',methods=['POST','GET'])
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
    else:
        return "Method Must Be GET!"
        
@api.route('/vBeta/addBot',methods=['POST','GET'])
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
                bid = data['bid']
            except:
                return "json must have 'bid' key!"
            if existBot(bid):
                try:
                    session_id = data['session_id']
                except:
                    return "json must have 'session_id' key"
                if existSession(bid,session_id):
                    return jsonify({"status":"OK","message":"session_id now in on server!"})
                else:
                    addSessionToBot(bid,session_id)
                    return jsonify({"status":"OK","message":"session has been added to client!"})
            else:
                addBot(bid)
                return jsonify({"status":"OK","message":"bot client add now request for create session"})
        else:
            return f"Password Wrong!({password})"
    else:
        return "Method Must Be Post!"

@api.route("/vBeta/addMessages",methods=['POST','GET'])
def sorting_messages():
    
    if request.method == 'POST':
        try:
            data = request.get_json()
        except:
            return "you must send an json!"
        try:
            bid = data['bid']
        except:
            return "json must have 'bid' key!"
        try:
            messages = data['messages']
        except:
            return "json must have 'messages' key!"
        sorted_messages = addMessages(bid,messages)
        return sorted_messages
    else:
        return "method must be post not get!"

@api.route("/vBeta/addMessage",methods=['POST','GET'])
def sorting_message():
    if request.method == 'POST':
        try:
            data = request.get_json()
        except:
            return "you must send an json!"
        try:
            bid = data['bid']
        except:
            return "json must have 'bid' key!"
        try:
            message = data['message']
        except:
            return "json must have 'message' key!"
        addMessages(bid,message)
    else:
        return "method must be post not get!"

if __name__ =="__main__":
    api.run(debug=True)