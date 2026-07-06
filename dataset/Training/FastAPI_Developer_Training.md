# TechNova Solutions Pvt. Ltd.

# FastAPI Developer Training Manual

**Training Version:** 1.0
**Department:** Learning & Development (L&D) and Engineering
**Duration:** 4 Weeks
**Target Audience:** Backend Developers, Full-Stack Developers, AI/ML Engineers, Data Engineers, Interns, and Freshers

---

# 1. Introduction to FastAPI

FastAPI is a modern, high-performance Python web framework used for building APIs. It is based on Python type hints and provides automatic API documentation.

Benefits of FastAPI:

* High performance
* Automatic API documentation
* Type checking
* Asynchronous programming support
* Data validation
* Easy integration with databases
* Built-in dependency injection

---

# 2. Installing FastAPI

Install FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn
```

Verify installation:

```bash
pip show fastapi
```

---

# 3. Creating the First FastAPI Application

Create file:

```text
main.py
```

Example:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}
```

Run application:

```bash
uvicorn main:app --reload
```

Default URL:

```text
http://localhost:8000
```

---

# 4. Automatic Documentation

FastAPI automatically generates API documentation.

Swagger UI:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

Benefits:

* Interactive testing
* API exploration
* Automatic documentation generation

---

# 5. Path Parameters

Example:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

Request:

```text
GET /users/101
```

Response:

```json
{
    "user_id": 101
}
```

---

# 6. Query Parameters

Example:

```python
@app.get("/search")
def search(name: str, age: int):
    return {
        "name": name,
        "age": age
    }
```

Request:

```text
/search?name=Aditi&age=21
```

---

# 7. Request Body

Example:

```python
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int

@app.post("/students")
def create_student(student: Student):
    return student
```

Example request:

```json
{
    "name": "Aditi",
    "age": 21
}
```

---

# 8. Response Models

Example:

```python
class UserResponse(BaseModel):
    id: int
    name: str

@app.get("/user", response_model=UserResponse)
def get_user():
    return {
        "id": 1,
        "name": "Aditi"
    }
```

Benefits:

* Validation
* Documentation
* Type safety

---

# 9. HTTP Methods

FastAPI supports:

| Method | Purpose                  |
| ------ | ------------------------ |
| GET    | Retrieve data            |
| POST   | Create data              |
| PUT    | Update complete resource |
| PATCH  | Partial update           |
| DELETE | Delete resource          |

Example:

```python
@app.delete("/users/{id}")
def delete_user(id: int):
    return {"deleted": id}
```

---

# 10. Status Codes

Example:

```python
from fastapi import status

@app.post(
    "/users",
    status_code=status.HTTP_201_CREATED
)
def create_user():
    return {"message": "Created"}
```

Common status codes:

* 200 OK
* 201 Created
* 400 Bad Request
* 401 Unauthorized
* 404 Not Found
* 500 Internal Server Error

---

# 11. Dependency Injection

Example:

```python
from fastapi import Depends

def get_db():
    return "database"

@app.get("/employees")
def employees(db=Depends(get_db)):
    return {"db": db}
```

Benefits:

* Reusability
* Cleaner code
* Better testing

---

# 12. Exception Handling

Example:

```python
from fastapi import HTTPException

@app.get("/products/{id}")
def get_product(id: int):
    if id != 1:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    return {"id": id}
```

---

# 13. Middleware

Example:

```python
@app.middleware("http")
async def middleware(request, call_next):
    response = await call_next(request)
    return response
```

Common middleware:

* Logging
* Authentication
* CORS
* Security headers

---

# 14. CORS Configuration

Example:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
```

---

# 15. Authentication

FastAPI supports:

* OAuth2
* JWT
* API Keys
* Session authentication

Example JWT setup:

```python
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)
```

---

# 16. Password Hashing

Example:

```python
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"]
)

hashed = pwd_context.hash("password")
```

Passwords should never be stored in plain text.

---

# 17. File Uploads

Example:

```python
from fastapi import UploadFile, File

@app.post("/upload")
async def upload(
    file: UploadFile = File(...)
):
    return {
        "filename": file.filename
    }
```

---

# 18. Background Tasks

Example:

```python
from fastapi import BackgroundTasks

def send_email():
    pass

@app.post("/notify")
def notify(
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(send_email)
```

---

# 19. Async Programming

Example:

```python
@app.get("/async")
async def async_function():
    return {"message": "async"}
```

Benefits:

* Better performance
* Higher concurrency
* Efficient I/O operations

---

# 20. Database Integration

Install SQLAlchemy:

```bash
pip install sqlalchemy
```

Example:

```python
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://localhost/db"
)
```

Supported databases:

* PostgreSQL
* MySQL
* SQLite
* MongoDB

---

# 21. SQLAlchemy ORM

Example:

```python
class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
```

Benefits:

* ORM support
* Database abstraction
* Migration support

---

# 22. Database Migrations

Install Alembic:

```bash
pip install alembic
```

Initialize:

```bash
alembic init migrations
```

Create migration:

```bash
alembic revision --autogenerate
```

Apply migration:

```bash
alembic upgrade head
```

---

# 23. Project Structure

Recommended structure:

```text
project/

├── app/
│   ├── routers/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── database/
│   └── utils/
│
├── tests/
├── requirements.txt
└── main.py
```

---

# 24. Testing FastAPI

Install pytest:

```bash
pip install pytest
```

Example:

```python
def test_home():
    response = client.get("/")
    assert response.status_code == 200
```

Testing types:

* Unit tests
* Integration tests
* API tests

---

# 25. Logging

Example:

```python
import logging

logging.basicConfig(
    level=logging.INFO
)
```

Log levels:

* DEBUG
* INFO
* WARNING
* ERROR
* CRITICAL

---

# 26. Security Best Practices

Developers should:

* Validate inputs
* Use JWT authentication
* Hash passwords
* Store secrets securely
* Enable HTTPS
* Implement rate limiting
* Perform security testing

---

# 27. Docker Deployment

Dockerfile example:

```dockerfile
FROM python:3.12

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app"]
```

Build:

```bash
docker build -t fastapi-app .
```

Run:

```bash
docker run -p 8000:8000 fastapi-app
```

---

# 28. Kubernetes Deployment

Deploy using:

```bash
kubectl apply -f deployment.yaml
```

Components:

* Pods
* Services
* Deployments
* ConfigMaps
* Secrets

---

# 29. Production Deployment

Recommended production stack:

| Component     | Technology       |
| ------------- | ---------------- |
| API           | FastAPI          |
| Server        | Uvicorn/Gunicorn |
| Database      | PostgreSQL       |
| Cache         | Redis            |
| Container     | Docker           |
| Orchestration | Kubernetes       |

---

# 30. FastAPI Best Practices

Developers should:

* Use Pydantic models
* Implement dependency injection
* Write tests
* Use async functions
* Document APIs
* Follow project structure
* Use logging
* Implement security controls

---

# 31. Mini Projects

Recommended projects:

* Employee Management API
* Authentication System
* E-Commerce API
* Banking API
* Weather API
* AI Chatbot Backend
* RAG Backend API
* Document Search API

---

# 32. Assessment

Evaluation criteria:

| Component   | Weightage |
| ----------- | --------- |
| Assignments | 20%       |
| Labs        | 30%       |
| Project     | 40%       |
| Viva        | 10%       |

Minimum passing score:

```text
70%
```

---

# 33. Frequently Asked Questions

### Q1. Is FastAPI asynchronous?

Yes.

### Q2. Does FastAPI generate documentation automatically?

Yes.

### Q3. Which database is preferred?

PostgreSQL.

### Q4. Is Docker mandatory?

Yes, for production applications.

### Q5. Should APIs be tested?

Yes, all APIs require testing.

---

# 34. Training Ownership

This FastAPI Developer Training Manual is maintained jointly by the Learning & Development Department and Engineering Department of TechNova Solutions Pvt. Ltd.
