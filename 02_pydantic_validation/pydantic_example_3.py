from pydantic import BaseModel, EmailStr, field_validator, ValidationError
from typing import List

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr
    addresses: List[Address]  

    @field_validator("name")
    @classmethod
    def name_must_be_at_least_two_char(cls, v):
        if len(v) < 2:
            raise ValueError("Name must be at least 2 characters long")
        return v

    @field_validator("id")
    @classmethod
    def id_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("ID must be a positive integer")
        return v

# Valid User
try:
    valid_user = UserWithAddress(
        id=1,
        name="Alice",
        email="alice@example.com",
        addresses=[{"street": "123 Main St", "city": "New York", "zip_code": "10001"}],
    )
    print("Valid user created successfully:")
    print(valid_user.model_dump())
except ValidationError as e:
    print("Error in valid user data:")
    print(e)

# Invalid User
try:
    invalid_user = UserWithAddress(
        id=-5,
        name="A",
        email="not-an-email",
        addresses=[]
    )
    print("Invalid user passed unexpectedly:")
    print(invalid_user.model_dump())
except ValidationError as e:
    print("Error in invalid user data:")
    print(e)
