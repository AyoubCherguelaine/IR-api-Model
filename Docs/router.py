from fastapi import APIRouter


router = APIRouter()


@router.get('/{doc_id}/detail')
async def createDoc(doc_id:str):
    return doc_id
