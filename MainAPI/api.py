from flask import Flask,request,jsonify

from db.bot import addBot

api = Flask(__name__)

@api.route('/vBeta/addMe',methods=['POST','GET'])
def addMe():
    if request.method == 'POST':
        try:
            data = request.get_json()
        except:
            return "you must send an json!"
        try:
            stoken = data['stoken']
        except:
            return "json must have 'stoken' key!"
        bid = addBot(stoken)
        return jsonify({
            'status':"ADDED",
            "bid":bid
        })
    else:
        return "Method Must Be POST"
