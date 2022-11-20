from .query import query
from .model import similarity
from .document import doc

from bson.objectid import ObjectId


def calc(query:query):
    ids = doc.getIds()
    result = []
    for i in ids:
        n=[]
        d= doc()
        d.initDict(doc.GetDoc(i))
        n.append(str(i))
        n.append(similarity.dice(d,query))
        result.append(n)

    
    result.sort(key= lambda result:result[1],reverse=True)

def calcby10(query:query):
    ids = doc.getIds()
    result = []
    l = len(ids)
    p = 10
    b=-1
    e=0
    ep=0
    print(l)

    while not (ep == l-1) :
        b=b+1
        e=e+1
        ep= e*p
        if (e*p)>=l:
            ep=l-1
        
        g = ids[b*p:ep]

        
        ids_list = [ObjectId(id) for id in g]

        docs = doc.getDocs(ids_list)
        
        for do in docs:
            
            n=[]
            d=doc()
            d.initDict(do)
            n.append(str(do["_id"]))
            n.append(str(d.text))
            n.append(similarity.dice(d,query))
            result.append(n)
    
    print(result)
    result.sort(key= lambda result:result[2],reverse=True)
    
    return result

 
def calcbyn(query:query,n):
    ids = doc.getIds()
    result = []
    l = len(ids)
    p = n
    b=-1
    e=0
    ep=0
    print(l)

    while not (ep == l-1) :
        b=b+1
        e=e+1
        ep= e*p
        if (e*p)>=l:
            ep=l-1
        
        g = ids[b*p:ep]

        
        ids_list = [ObjectId(id) for id in g]

        docs = doc.getDocs(ids_list)
        
        for do in docs:
            
            n=[]
            d=doc()
            d.initDict(do)
            n.append(str(do["_id"]))
            n.append(str(d.text))
            n.append(similarity.dice(d,query))
            result.append(n)
    
    print(result)
    result.sort(key= lambda result:result[2],reverse=True)
    
    return result   