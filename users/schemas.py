from pydantic import BaseModel, EmailStr, Field
from typing import Annotated
from annotated_types import MinLen, MaxLen


class CreateUser(BaseModel):
    username: Annotated[str, MinLen(5), MaxLen(20)]
    email: EmailStr
