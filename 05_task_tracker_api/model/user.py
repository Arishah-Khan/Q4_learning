from pydantic import BaseModel, EmailStr, field_validator

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    
    @field_validator("name")
    def validate_name(cls, value):
        if 3 <= len(value) <= 20:
            return value
        else:
            raise ValueError("Name must be between 3 to 20 characters long")

    @field_validator("password")
    def validate_pass(cls, value):
        if len(value) < 6:
            raise ValueError("Password must be greater than 6 characters")
        return value

class UserRead(BaseModel):
    id: str
    name: str
    email: EmailStr

# Model for update with validation
class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None

    @field_validator("name")
    def validate_name(cls, value):
        if value is not None and not (3 <= len(value) <= 20):
            raise ValueError("Name must be between 3 to 20 characters long")
        return value

    @field_validator("password")
    def validate_pass(cls, value):
        if value is not None and len(value) < 6:
            raise ValueError("Password must be greater than 6 characters")
        return value
