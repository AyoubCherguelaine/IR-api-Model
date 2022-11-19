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
    d =doc()
    dic= doc.GetDoc(doc_id)
    d.initDict(dic)
    return d.text

@router.post("/search/all")
async def createDoc(queryBody:queryBody):
    q= query(queryBody.text)
    return action.calc(q)


@router.post("/search")
async def createDoc(queryBody:queryBody):
    q= query(queryBody.text)
    res = action.calc(q)
    re = [i for i in res  if i[1] != 0]
    return re
