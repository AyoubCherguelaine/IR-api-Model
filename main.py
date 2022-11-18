from typing import Union

from fastapi import FastAPI

from Docs import router

app = FastAPI()


app.include_router(router.router,prefix="/docs",
    tags=["docs"],
)


