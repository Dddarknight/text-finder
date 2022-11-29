from fastapi import APIRouter
from fastapi.responses import JSONResponse


def create_router(textService):
    router = APIRouter()

    @router.get("/texts", response_class=JSONResponse)
    async def find_texts(text_to_find: str):
        try:
            texts = textService.find_db_texts(text_to_find)
            return JSONResponse({'texts': texts})
        except Exception as e:
            return JSONResponse({'texts': str(e)})

    return router
