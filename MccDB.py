import json

dbName = "coinDB"

f = open(dbName,"r")
file = json.loads(f.read())
f.close()

class dbTool:
    def get():
        with open(dbName,"r") as f:
            return json.loads(f.read())

    def set(db):
        with open(dbName,"w") as f:
            f.write(json.dumps(db))

class dataBase:
    async def get(member,key):
        if not isinstance(member,str):
            member = str(member)
        db = dbTool.get()

        if not member in db:
            db[member] = {}
        if not key in db[member]:
            db[member][key] = 0
        
        dbTool.set(db)

        return db[member][key]

    async def set(member,key,value):
        if not isinstance(member,str):
            member = str(member)
        db = dbTool.get()

        if not member in db:
            db[member] = {}
        if not key in db[member]:
            db[member][key] = 0
        
        db[member][key] = value

        dbTool.set(db)
        return

    async def add(member,key,value):
        if not isinstance(member,str):
            member = str(member)
        db = dbTool.get()

        if not member in db:
            db[member] = {}
        if not key in db[member]:
            db[member][key] = 0
        
        db[member][key] += value

        dbTool.set(db)
        return

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