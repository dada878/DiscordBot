import json

class dataBase:
    def getDB():
        with open("coinDB","r") as f:
            return json.loads(f.read())
    def setDB(db):
        with open("coinDB","w") as f:
            return f.write(json.dumps(db))

db = dataBase.getDB()

for i in db:
    db[i] = {"coin":db[i],"diamond":0}

dataBase.setDB(db)