from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from collections import Counter, defaultdict
import spacy
import re
import numpy as np
from .vector import vector
from .query import query
from .document import (doc,upload)
import numpy

def RM_Punc(text):
    punctuation_pattern = re.compile('[^A-z ]')
    no_punct_text = [re.sub(punctuation_pattern, '', token) for token in text]
    return ''.join([token for token in no_punct_text if token != ''])

def preSomthing(text):
    text = text.lower()
    text = RM_Punc(text)
    return text
def RM_Stop_Word(tokens):
    # check in lowercase 
    t = [token for token in tokens if token.lower() not in stopwords.words("english")]
      
    return t

nlp = spacy.load('en_core_web_sm')
def Lemm(text):
    
    doc = nlp(text)
    return [i.lemma_ for i in doc]

def PreProcessing(text):
    text = preSomthing(text)
    tokens= Lemm(text)
    return RM_Stop_Word(tokens)

def removeAll(li=[],item=object):
    while( li.count(item) >0 ):
        li.remove(item)


def indexVect(token):
    tokens= token.copy()
    
    index=[]
    som = len(tokens)
    i=0
    while (len(tokens)>0):
        i = tokens[0]
        indexVal = tokens.count(i)
        indinv  =vector.checkOrAdd(i)
        removeAll(tokens,i)    
        index.append([indinv,indexVal/som])
        
    vector.uploadWords()    
    return index   



def indexVectQuery(token):
    tokens= token.copy()
    vectQuery=[]
    index=[]
    som = len(tokens)
    i=0
    while (len(tokens)>0):
        i = tokens[0]
        indexVal = tokens.count(i)
        indinv  =vector.checkOrNot(i)
        removeAll(tokens,i)    
        if indinv == -1 :
            if vectQuery.count(i) ==0:
                vectQuery.append(i)

            indinv = - vectQuery.index(i)

        index.append([indinv,indexVal/som])
        
      
    return (index,vectQuery)


class similarity:

    @staticmethod
    def inner(doc:doc,query:query):
        ardoc = numpy.array(doc.index)
        arQue = numpy.array(query.index)

        inner = 0.0
        
        for i in arQue[:,:1]:
            if i in ardoc[:,:1]:
                qi= np.where(arQue[:,:1]==i)
                di= np.where(ardoc[:,:1]==i)
                inner = inner + (arQue[di[0]][:,1:2][0][0] * ardoc[qi[0]][:,1:2][0][0]  )

        return inner

    @staticmethod
    def dice(doc:doc,query:query):
        ardoc = numpy.array(doc.index)
        arQue = numpy.array(query.index)

        inner = similarity.dice(doc,query)
        p1=0.0
        p2-0.0

        qindexs = [r[0] for r in arQue[:,1:2] ]
        for i in qindexs:
            p2=p2 + i**2

        dindexs = [ r[0] for r in ardoc[:,1:2] ]
        for i in dindexs:
            p1=p1 + i**2
            
        if (p1+p2 )   ==0.0 :
            return 0  

        return (2*inner) / (p1+p2 )      