from fastapi import FastAPI , Path , Query , Body
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name : str
    age : int

@app.put("/students/{student_id}")
async def updated_student(
    student_id: int = Path(... , title = "Student Id" , ge = 1),
    filter: str | None = Query(None, title="Filter criteria"),  
    student: Student = Body(..., description="Student data to update")   
):
    result = {
        "student_id" : student_id
    }
    
    if filter:
        result.update({"filter": filter})

    result.update({"updated_student": student.dict()})

    return result