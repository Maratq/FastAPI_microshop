from fastapi import FastAPI
from pydantic import EmailStr, BaseModel
import uvicorn
from items_views import router as items_router
from users.views import router as users_router
from contextlib import asynccontextmanager
from core.models import Base, db_helper

app = FastAPI()
app.include_router(items_router, tags=["items"])
app.include_router(users_router, tags=["users"])


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


@app.get("/")
def hello_world():
    return "hello"


@app.get("/hello/")
def hello(name: str = "Hello world"):
    name = name.strip().title()
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
