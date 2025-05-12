from fastapi import FastAPI, HTTPException
from model.user import UserCreate, UserRead, UserUpdate
from model.task import TaskCreate, TaskRead, TaskUpdate
import uuid

app = FastAPI()

Users = {}
Tasks = {}

# Create a new user
@app.post("/users/", response_model=UserRead)
async def create_user(user: UserCreate):
    user_id = str(uuid.uuid4())
    user_data = user.model_dump()
    user_data["id"] = user_id
    Users[user_id] = user_data
    return Users[user_id]

# Get a single user by ID
@app.get("/users/{user_id}", response_model=UserRead)
async def get_user(user_id: str):
    if user_id not in Users:
        raise HTTPException(status_code=404, detail="User not found")
    return Users[user_id]

# Get all users
@app.get("/users/", response_model=list[UserRead])
async def get_all_users():
    return list(Users.values())

# Update user
@app.put("/users/{user_id}", response_model=UserRead)
async def update_user(user_id: str, user: UserUpdate):
    if user_id not in Users:
        raise HTTPException(status_code=404, detail="User not found")

    # Perform the validation here for the update model
    user_data = Users[user_id]
    if user.name:
        user_data["name"] = user.name
    if user.email:
        user_data["email"] = user.email
    if user.password:
        user_data["password"] = user.password
    
    Users[user_id] = user_data
    return user_data


# Delete user
@app.delete("/users/{user_id}")
async def delete_user(user_id: str):
    if user_id not in Users:
        raise HTTPException(status_code=404, detail="User not found")
    del Users[user_id]
    return {"message": "User deleted successfully"}



# Create a new task
@app.post("/tasks/", response_model=TaskRead)
async def create_task(task: TaskCreate):
    task_id = str(uuid.uuid4()) 
    task_data = task.model_dump()
    task_data["id"] = task_id  
    Tasks[task_id] = task_data
    return task_data

# Get a single task by ID
@app.get("/tasks/{task_id}", response_model=TaskRead)
async def get_task(task_id: str):
    if task_id not in Tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return Tasks[task_id]

# Get all tasks
@app.get("/tasks/", response_model=list[TaskRead])
async def get_all_tasks():
    return list(Tasks.values())

# Update task
@app.put("/tasks/{task_id}", response_model=TaskRead)
async def update_task(task_id: str, task: TaskUpdate):
    if task_id not in Tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    task_data = Tasks[task_id]
    if task.title:
        task_data["title"] = task.title
    if task.description:
        task_data["description"] = task.description
    if task.due_date:
        task_data["due_date"] = task.due_date
    if task.status:
        task_data["status"] = task.status

    Tasks[task_id] = task_data  # Update the task
    return task_data

# Delete task
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    if task_id not in Tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del Tasks[task_id]  # Delete the task
    return {"message": "Task deleted successfully"}