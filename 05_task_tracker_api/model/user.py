from pydantic import BaseModel, EmailStr, constr, field_validator
from typing import Optional , Annotated

Username = Annotated[str, constr(min_length=3, max_length=20)]

class UserCreate(BaseModel):
    name: Username
    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def validate_pass(cls, value):
        if len(value) < 6:
            raise ValueError("Password must be greater than 6 characters")
        return value
    
class UserRead(BaseModel):
    id: str
    name: str
    email: EmailStr


class UserUpdate(BaseModel):
    name: Optional[Username] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

    @field_validator("password")
    @classmethod
    def validate_pass(cls, value):
        if value is not None and len(value) < 6:
            raise ValueError("Password must be greater than 6 characters")
        return value
