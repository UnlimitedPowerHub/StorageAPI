from db.db import DB

bots = DB('bots')

def addBot(stoken):
    bid = bots.generateID()
    bots.setKey(bid,stoken)
    return bid