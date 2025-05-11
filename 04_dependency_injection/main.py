from fastapi import FastAPI, Depends , Query , HTTPException , status
from typing import Annotated

app = FastAPI()

# Simple dependency function returning mission info
def get_mission():
    return {
        "mission": "Building future with AI."
    }

# Route using the dependency
@app.get("/get-mission")
async def mission(response: Annotated[dict, Depends(get_mission)]):
    return response  # Response injected from get_mission


# Dependency with Parameters


def get_user_status(username : str):
    return {
        "status" : "Mission Ready",
        "username" : username
    }
    
    
    
@app.get("/user-status")
async def user_status(response : Annotated[dict , Depends(get_user_status)]):
    return response



# Dependency function with query parameters
def get_user_info(age: int = Query(None), city: str = Query(None)):
    if age is None or city is None:
        return {"message": "Please provide both age and city."}
    
    if age > 18 and city.lower() == "karachi":
        return {
            "message": f"Hello, You are {age} years old and live in {city}. You are eligible!"
        }
    else:
        return {
            "message": f"Hello, You are {age} years old and live in {city}. You are not eligible."
        }

@app.get("/get-user-permission")
async def user_info(response: Annotated[dict, Depends(get_user_info)]):
    return response



#  Multiple Dependencies

def add_five(num1 :int):
    num1 = int(num1)
    num1 += 5
    return num1

def multiply_by_three(num1 : int):
    num1 = int(num1)
    num1 *= 3
    return num1

@app.get("/process/{num1}")
async def process_number(num1:int , num2 : Annotated[int , Depends(add_five)] , num3 : Annotated[int , Depends(multiply_by_three)]):
    result = num1 + num2 + num3
    return {
        "message": "Calculation successful",  
        "num1": num1,  
        "num2": num2,  
        "num3": num3,  
        "result": result 
    }
    
    
from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated

app = FastAPI()

# Sample books and users data
books = {
    "101": "Python Programming",
    "102": "Data Science Handbook",
    "103": "Machine Learning Basics"
}

users = {
    "8": "Ahmed",
    "9": "Mohammed",
    "10": "Sara",
    "11": "Ayesha"
}

# Class to handle 404 error for non-existing objects
class GetObjectOr404():
    def __init__(self, model) -> None:
        self.model = model  
    
    def __call__(self, id: str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object ID {id} not found")
        return obj

# Dependency for books
book_dependency = GetObjectOr404(books)

@app.get("/book/{id}")
def get_book(bookTitle: Annotated[str, Depends(book_dependency)]):
    return {
        "bookTitle": bookTitle
    }

# Dependency for users
user_dependency = GetObjectOr404(users)

@app.get("/user/{id}")
def get_user(userName: Annotated[str, Depends(user_dependency)]):
    return {
        "userName": userName
    }
