from db.db import DB

clients = DB('client')

def addBot(bid):
    clients.setKey(bid,{'sessions':{},'messages':{}})

def addMessageToBot(bid,message):
    clients.setNested([bid,'messages'],message)
    
def addSessionToBot(bid,session):
    clients.setNested([str(bid),'sessions',str(session)],True)
    
def removeMessageFromBot(bid,message):
    clients.removeNested([bid,'messages',message])
    
def removeSessionFromBot(bid,session):
    clients.removeNested([bid,'sessions',session])
    
def getBots():
    return clients.getAll()

def getBotSessions(bid):
    return getBots()[str(bid)]['sessions']

def getBotMessages(bid):
    return getBots()[str(bid)]['messages']

def getBotSession(bid,session):
    return getBots()[str(bid)][str(session)]

def getBotMessage(bid,message_id):
    return getBots()[str(bid)][str(message_id)]

def existBot(bid):
    return bool(str(bid) in getBots())

def existSession(bid,session):
    return bool(str(session) in getBotSessions(bid))

def existMessage(bid,message_id):
    return bool(str(message_id) in getBotMessages(bid))