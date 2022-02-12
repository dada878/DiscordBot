import json

dbName = "coinDB"

class dbTool:
    def get():
        with open(dbName,"r") as f:
            return json.loads(f.read())
    def set(db):
        with open(dbName,"w") as f:
            return f.write(json.dumps(db))

class dataBase:
    def get(member,key):
        db = dbTool.get()

        if not member in db:
            db[member] = {}
        if not key in db[member]:
            db[member][key] = 0
        
        return db[member][key]

    def set(member,key,value):
        db = dbTool.get()

        if not member in db:
            db[member] = {}
        if not key in db[member]:
            db[member][key] = 0
        
        db[member][key] = value

        dbTool.set(db)

    def add(member,key,value):
        db = dbTool.get()

        if not member in db:
            db[member] = {}
        if not key in db[member]:
            db[member][key] = 0
        
        db[member][key] += value

        dbTool.set(db)

# class coin:

#     def add(member,count):
#         member = str(member)
#         db = dataBase.getDB()
#         if not member in db:
#             db[member] = {"coin":0,"diamond":0}
#         db[member]["coin"] += count
#         dataBase.setDB(db)

#     def get(member):
#         member = str(member)
#         db = dataBase.getDB()
#         if not member in db:
#             db[member] = {"coin":0,"diamond":0}
#         return db[member]["coin"]

# class diamond:

#     def add(member,count):
#         member = str(member)
#         db = dataBase.getDB()
#         if not member in db:
#             db[member] = {"coin":0,"diamond":0}
#         db[member]["diamond"] += count
#         dataBase.setDB(db)

#     def get(member):
#         member = str(member)
#         db = dataBase.getDB()
#         if not member in db:
#             db[member] = {"coin":0,"diamond":0}
#         return db[member]['diamond']