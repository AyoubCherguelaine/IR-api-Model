from . import model

from os import walk



class query:
    def __init__(self,text):
        self.text= text
        self.index , self.VectQuery= self.indexing()

    def indexing(self):
        tokens=model.PreProcessing(self.DocText)
        return model.indexVectQuery(tokens)
    


 