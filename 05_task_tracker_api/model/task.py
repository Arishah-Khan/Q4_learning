from pydantic import BaseModel, field_validator
from datetime import date
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: date
    status: str = "in-progress"

    @field_validator("due_date")
    def validate_due_date(cls, value):
        if value < date.today():
            raise ValueError("Due date must be today or in the future.")
        return value


class TaskRead(BaseModel):
    id: str
    title: str
    description: Optional[str]
    due_date: date
    status: str


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: Optional[str] = None

    @field_validator("due_date")
    def validate_due_date(cls, value):
        if value is not None and value < date.today():
            raise ValueError("Due date must be today or in the future.")
        return value

  
