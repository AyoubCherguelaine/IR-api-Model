from . import model
from mongoConnector.db import db
from os import walk
from bson.objectid import ObjectId

db_ =db("")


class doc:
    def __init__(self,text):
        self.text= text
        self.index= self.indexing()

    def indexing(self):
        tokens=model.PreProcessing(self.DocText)
        return model.indexVect(tokens)
    
    def toDict(self):
        return {
            "text":self.text,
            "index":self.index
        }

    def uploadDoc(self):
        obj=self.toDict()
        db_.AddDocument("doc",obj)

    @staticmethod
    def getIds():
        return db_.GetIds("doc")    

    @staticmethod
    def GetDoc(id:str):
        return db_.GetDocument("doc",{"_id":ObjectId(id)})

        


class upload:
    @staticmethod
    def __uploadFromFolder(url):
        FileList=[]
        for (dirpath, dirnames, filenames) in walk(url):
    
            FileList.extend(filenames)

        FileList.sort()
        return FileList
 
    @staticmethod
    def __readDoc(url,filename):
        url = url+"/"+filename
        #this method can read .txt files only
        f = open(url, "r")
        return f.read()


    @staticmethod
    def doProcessIntoDocs(url):
        filesList = upload.__uploadFromFolder(url)

        for filename in filesList:
            text = upload.__readDoc(url,filename)
            d = doc(text)
            d.uploadDoc()

           
    

