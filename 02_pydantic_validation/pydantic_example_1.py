from pydantic import BaseModel, ValidationError

# Define the User model
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None

    class Config:
        strict = True  # This will disable type coercion

# Example 1: Valid data
user_data = {
    "id": 12,
    "name": "Alice",
    "email": "alice@gmail.com",
    "age": 24
}

user = User(**user_data)
print(user)  # Expected output: id=12 name='Alice' email='alice@gmail.com' age=24
print(user.model_dump())  # Expected output: {'id': 12, 'name': 'Alice', 'email': 'alice@gmail.com', 'age': 24}

# Example 2: Valid data (string "12" will be coerced to int if strict=False)
try:
    valid_user = User(id="12", name="Bob", email="bob@example.com")
    print(valid_user)
except ValidationError as e:
    print(e)

# Example 3: Invalid data (This will raise an error because "not_an_integer" can't be converted to int)
try:
    invalid_user = User(id="not_an_integer", name="Bob", email="bob@example.com")
except ValidationError as e:
    print(e)  # Expected error message: Input should be a valid integer
