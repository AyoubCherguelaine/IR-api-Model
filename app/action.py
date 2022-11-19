from .query import query
from .model import similarity
from .document import doc

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
    
    return result