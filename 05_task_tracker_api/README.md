# Task Tracker API (FastAPI)

A simple Task Tracker API built using FastAPI. It allows users to manage tasks and user accounts with full CRUD operations.

---

## Features

- Create, Read, Update, Delete (CRUD) operations for:
  - **Users**
  - **Tasks**
- Input validation using Pydantic
- Unique ID generation using `uuid`
- Simple in-memory data storage (no database)

---

## Endpoints

### Users

| Method | Endpoint        | Description          |
|--------|------------------|----------------------|
| POST   | `/users/`        | Create a new user    |
| GET    | `/users/`        | Get all users        |
| GET    | `/users/{id}`    | Get user by ID       |
| PUT    | `/users/{id}`    | Update user info     |
| DELETE | `/users/{id}`    | Delete user          |

### Tasks

| Method | Endpoint         | Description         |
|--------|-------------------|---------------------|
| POST   | `/tasks/`         | Create a new task   |
| GET    | `/tasks/`         | Get all tasks       |
| GET    | `/tasks/{id}`     | Get task by ID      |
| PUT    | `/tasks/{id}`     | Update task         |
| DELETE | `/tasks/{id}`     | Delete task         |

---

## Data Validation

- Email format checked using `EmailStr`
- Password must be at least 6 characters
- Name must be 3 to 20 characters
- Task due date cannot be in the past

---


