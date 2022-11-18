
from mongoConnector.db import db


db_= db("")


class vector:

    vector=[]
    inline=[]

    @staticmethod
    def toDict(inline:list):
        objs=[]
        for i in inline:
            o={
                "word":i,
                "index":vector.vector.index(i),
                "count":1
            }
            objs.append(o.copy())
        return objs    

    @staticmethod
    def uploadWords():
        objs= vector.toDict(vector.inline)
        vector.CleanWords()
        db_.AddDocuments("vocab",objs)
        print("upload words ")
        

    @staticmethod
    def CleanWords():
        vector.inline = []

    @staticmethod
    def checkOrAdd(word):
        if word not in vector.vector:
            vector.vector.append(word)
            vector.inline.append(word)
        
        return vector.vector.index(word)  

    @staticmethod    
    def checkOrNot(word):
        if word not in vector.vector:
            return -1
        
        return vector.vector.index(word)   

def downloadWords():
    rs = db_.GetDocs("vocab",{})
    #[ print(i) for i in rs ]
    return rs

def init():
    rs = downloadWords()    

    [vector.vector.append(str(i["word"])) for i in rs ]

#init()

