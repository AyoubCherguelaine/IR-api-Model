
import pymongo
from bson.objectid import ObjectId
from . import env #this file comtaine a connection ket for mongo 



class db :
    def __init__(self ,key:str):
        key = env.key
        client = pymongo.MongoClient(key)
        self.db = client.gettingStarted
        
        
        
        
    
    def CreateCollection(self,name):
        col = self.db.create_collection(name)
        
        return col

    def GetCollection(self,ColName):
        
        return self.db.get_collection(ColName)
        

    def AddDocument(self,ColName,obj):
        
        col = self.db.get_collection(ColName)
        
        r =col.insert_one(obj) 
        return r
    
    def AddDocuments(self,colname,objs:list):
        col = self.db.get_collection(colname)
        r = col.insert_many(objs)
        return r

    def GetDocument(self,ColName,search):
        #search is a dict : { "name.last": "Turing" }
        col = self.db.get_collection(ColName)
        doc = col.find_one(search)
        return doc

    def GetDocs(self,ColName,query={}):
        col=self.db.get_collection(ColName)    
        d = col.find(query)
        
        return d    


    def CountDoc(self,ColName,query={}):
        col=self.db.get_collection(ColName)    
        v = col.count_documents(query)
        return v


    def DeleteOne(self,ColName,id):
        #{ "_id" : ObjectId("563237a41a4d68582c2509da") }
        try:
            col = self.db.get_collection(ColName)
            
            return col.delete_one({"_id":ObjectId(id)})
        except:
            return "Error"

         
    def GetIds(self,colName):
        col = self.db.get_collection(colName)
        return col.distinct('_id')     

    def GetField(self,colName,docId,Field):
        col = self.db.get_collection(colName)
        return col.distinct(Field, { '_id': ObjectId(docId) })     
                     

    def addItemInArray(self,colName,id,field,newitem):
        col = self.GetCollection(colName)
        col.update_one({ '_id':  ObjectId(id) },{ '$addToSet':{ field:newitem} })
    #{ $each: [ "camera", "electronics", "accessories" ] }

    def addItemsInArray(self,colName,id,field,newitems:list):
        col = self.GetCollection(colName)
        col.update_one({ '_id':  ObjectId(id) },{ '$addToSet':{ field:{ "$each": newitems}} })

    def modifyDocument(self,colname:str,id:str,query={}):
        col= self.GetCollection(colname)
        result =col.update_one({'_id':ObjectId(id)},{ "$set": query})
        return result