import requests


req = requests.post("http://127.0.0.1:5000/add_bot",json={'password':"mamadmamadi",'bot_username':"Test"})

print (req.text)