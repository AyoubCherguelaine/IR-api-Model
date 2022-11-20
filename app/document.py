from . import model
from mongoConnector.db import db
from os import walk
from bson.objectid import ObjectId

db_ =db("")


class doc:
    
    def __init__(self):
        self.text=""
        self.index=[]

    def init(self,text):    
        self.text= text
        self.index= self.indexing()

    def getIndex(self):
        return self.index

    def initDict(self,dict):
        self.text= dict['text']
        self.index = dict["index"]

    def indexing(self):
        tokens=model.PreProcessing(self.text)
        return model.indexVect(tokens)

    @staticmethod
    def toDict(docObj):
        return {
            "text":docObj.text,
            "index":docObj.index
        }
    @staticmethod
    def uploadDoc(docObj):
        obj=doc.toDict(docObj)
        db_.AddDocument("doc",obj)

    @staticmethod
    def getIds():
        return db_.GetIds("doc")    

    @staticmethod
    def GetDoc(id:str):
        return db_.GetDocument("doc",{"_id":ObjectId(id)})

    @staticmethod
    def getDocs(ids_list:list):
        r = db_.agregate("doc",ids_list)  
        
        return r


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
        print(filesList)
        l = len(filesList)
        i=1
        for filename in filesList:
            print("upload : ",i,"/",l,"     ",filename)
            text = upload.__readDoc(url,filename)
            d = doc()
            d.init(text)
            doc.uploadDoc(d)
            i=i+1
           
    

