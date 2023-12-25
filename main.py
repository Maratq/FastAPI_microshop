from fastapi import FastAPI, Body
from pydantic import EmailStr, BaseModel
import uvicorn


app = FastAPI()

@app.get("/")
def hello_world():
    return "hello" 

class CreateUser(BaseModel):
    email: EmailStr


@app.get("/items/")
def list_items():
    return ["item1",
            "item2",
            "item2",
            ]
    
@app.get("/hello/")
def hello(name: str = "Hello world"):
    name = name.strip().title()
    return {"message" : f"Hello {name}"}

@app.post("/users/")
def create_user(user: CreateUser):
    return {"message" : "Success",
            "email" : user.email
            }
    
@app.get("/items/latest/")
def get_latest_item():
    return {
            "item": {
                "id": 0,
                "name": "latest"
            },
        }

@app.get("/items/{item_id}/")
def get_item_by_id(item_id: int):
    return {
            "item": {
                "id": item_id
            },
        }

    
    
    
    
    
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)