from fastapi import APIRouter
from pydantic import BaseModel
from app.query import query
from app import action
from app.document import doc

router = APIRouter()

class queryBody(BaseModel):
    text :str

@router.get('/{doc_id}/detail')
async def createDoc(doc_id:str):
    
    dic= doc.GetDoc(doc_id)
    
    
    return dic["text"]

@router.post("/search/all")
async def createDoc(queryBody:queryBody):
    q= query(queryBody.text)
    return action.calc(q)


@router.post("/search")
async def createDoc(queryBody:queryBody):
    q= query(queryBody.text)
    res = action.calc(q)
    re = [i for i in res  if i[2] != 0]
    return re


#calcby10
@router.post('/search/10')
async def createDoc(queryBody:queryBody):
    q= query(queryBody.text)
    res = action.calcby10(q)
    re = [i for i in res  if i[2] != 0]
    return re

@router.post("/search/{n}")
async def searchDocs(queryBody:queryBody,n:int):
    
    q= query(queryBody.text)
    res = action.calcbyn(q,n)
    re = [i for i in res  if i[2] != 0]
    return re