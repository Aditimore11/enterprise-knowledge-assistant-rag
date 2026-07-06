# TechNova Solutions Pvt. Ltd.

# Python Bootcamp Training Manual

**Training Version:** 1.0
**Department:** Learning & Development (L&D)
**Duration:** 8 Weeks
**Target Audience:** Software Engineers, Data Analysts, Data Scientists, AI/ML Engineers, Interns, and Freshers

---

# 1. Introduction to Python

Python is a high-level, interpreted, object-oriented programming language developed by Guido van Rossum and released in 1991.

Python is widely used for:

* Web Development
* Data Science
* Artificial Intelligence
* Machine Learning
* Automation
* Cloud Computing
* Cybersecurity
* DevOps
* Data Analytics

---

# 2. Features of Python

Python provides several advantages:

* Easy syntax
* Open source
* Cross-platform compatibility
* Large community support
* Extensive libraries
* Dynamic typing
* Object-oriented programming support
* Rapid development capabilities

---

# 3. Installing Python

Steps:

1. Download Python from the official website.
2. Install Python 3.12 or above.
3. Verify installation.

Example:

```bash id="7jv4qk"
python --version
```

Output:

```text id="yx7lcb"
Python 3.12.1
```

---

# 4. Python IDEs

Recommended IDEs:

| IDE              | Usage                  |
| ---------------- | ---------------------- |
| VS Code          | Recommended            |
| PyCharm          | Enterprise development |
| Jupyter Notebook | Data Science           |
| Spyder           | Analytics              |
| Google Colab     | Cloud notebooks        |

---

# 5. Writing Your First Program

Example:

```python id="btj89x"
print("Hello World")
```

Output:

```text id="p3r87y"
Hello World
```

---

# 6. Variables

Variables store data values.

Example:

```python id="k8cmf5"
name = "Aditi"
age = 21
salary = 50000
```

Python variables are dynamically typed.

---

# 7. Data Types

Python supports:

| Data Type | Example |
| --------- | ------- |
| int       | 10      |
| float     | 10.5    |
| str       | "Hello" |
| bool      | True    |
| list      | [1,2,3] |
| tuple     | (1,2,3) |
| set       | {1,2,3} |
| dict      | {"a":1} |

Example:

```python id="9t1vzc"
x = 10
y = 3.14
z = "Python"
```

---

# 8. Operators

Types of operators:

* Arithmetic
* Comparison
* Logical
* Assignment
* Bitwise

Example:

```python id="v4obmt"
a = 10
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
```

---

# 9. Conditional Statements

Example:

```python id="3keo2a"
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Nested conditions are supported.

---

# 10. Loops

## For Loop

```python id="g5jqpi"
for i in range(5):
    print(i)
```

---

## While Loop

```python id="6wthyu"
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

# 11. Break and Continue

Example:

```python id="sp9kxa"
for i in range(10):
    if i == 5:
        break
```

Example:

```python id="ztm4yf"
for i in range(10):
    if i == 5:
        continue
```

---

# 12. Functions

Functions improve code reusability.

Example:

```python id="j4b8np"
def greet(name):
    print("Hello", name)

greet("Aditi")
```

---

# 13. Function Arguments

Example:

```python id="mezk6w"
def add(a,b):
    return a+b

print(add(10,20))
```

Types:

* Positional arguments
* Keyword arguments
* Default arguments
* Variable arguments

---

# 14. Lambda Functions

Example:

```python id="vwb70f"
square = lambda x: x*x
print(square(5))
```

Output:

```text id="0mrpgd"
25
```

---

# 15. Lists

Example:

```python id="3h5zxy"
numbers = [10,20,30,40]
numbers.append(50)
print(numbers)
```

Common operations:

* append()
* remove()
* pop()
* sort()
* reverse()

---

# 16. Tuples

Example:

```python id="7dvw8l"
student = ("Aditi",21)
print(student)
```

Tuples are immutable.

---

# 17. Sets

Example:

```python id="r8z6ol"
data = {1,2,3,4}
data.add(5)
```

Sets remove duplicate values automatically.

---

# 18. Dictionaries

Example:

```python id="j1n0kq"
employee = {
    "name":"Aditi",
    "age":21,
    "salary":50000
}
```

Access:

```python id="u4hxb8"
print(employee["name"])
```

---

# 19. String Operations

Example:

```python id="hy2npa"
name = "Python"

print(name.upper())
print(name.lower())
print(len(name))
```

Common functions:

* upper()
* lower()
* split()
* replace()
* strip()

---

# 20. File Handling

Writing file:

```python id="i3rzuv"
with open("sample.txt","w") as file:
    file.write("Hello")
```

Reading file:

```python id="f4k8st"
with open("sample.txt","r") as file:
    print(file.read())
```

---

# 21. Exception Handling

Example:

```python id="2n1efz"
try:
    a = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Blocks:

* try
* except
* else
* finally

---

# 22. Object-Oriented Programming

Python supports:

* Classes
* Objects
* Inheritance
* Polymorphism
* Encapsulation
* Abstraction

---

# 23. Classes and Objects

Example:

```python id="kj0n6e"
class Student:
    def __init__(self,name):
        self.name = name

student = Student("Aditi")
print(student.name)
```

---

# 24. Inheritance

Example:

```python id="s1cfb5"
class Animal:
    pass

class Dog(Animal):
    pass
```

---

# 25. Modules

Example:

```python id="4ix2du"
import math

print(math.sqrt(25))
```

Popular modules:

* math
* random
* datetime
* os
* sys

---

# 26. Virtual Environments

Create environment:

```bash id="jlwm0k"
python -m venv .venv
```

Activate:

```bash id="smp90h"
.venv\Scripts\activate
```

---

# 27. Logging

Example:

```python id="kq06tp"
import logging

logging.info("Application started")
```

Log levels:

* DEBUG
* INFO
* WARNING
* ERROR
* CRITICAL

---

# 28. Python Libraries

Popular libraries:

| Category      | Libraries           |
| ------------- | ------------------- |
| Data Science  | Pandas, NumPy       |
| Visualization | Matplotlib, Plotly  |
| ML            | Scikit-learn        |
| Deep Learning | TensorFlow, PyTorch |
| Web           | FastAPI, Flask      |
| Database      | SQLAlchemy          |

---

# 29. Introduction to Pandas

Example:

```python id="znjlwm"
import pandas as pd

df = pd.read_csv("employees.csv")
print(df.head())
```

Common operations:

* read_csv()
* head()
* tail()
* groupby()
* merge()

---

# 30. Introduction to NumPy

Example:

```python id="0cg64q"
import numpy as np

arr = np.array([1,2,3])
print(arr)
```

NumPy supports:

* Arrays
* Matrix operations
* Statistics
* Linear algebra

---

# 31. Python Project Best Practices

Developers should:

* Follow PEP8
* Use type hints
* Write tests
* Document code
* Use Git
* Use virtual environments
* Handle exceptions
* Implement logging

---

# 32. Mini Projects

Recommended projects:

* Calculator
* Student Management System
* Expense Tracker
* Weather App
* REST API
* Chatbot
* Data Analytics Dashboard
* RAG Application

---

# 33. Assessment

Evaluation criteria:

| Component        | Weightage |
| ---------------- | --------- |
| Assignments      | 20%       |
| Coding Tests     | 30%       |
| Project          | 30%       |
| Final Assessment | 20%       |

Passing score:

```text id="jcgkzt"
70%
```

---

# 34. Frequently Asked Questions

### Q1. Which Python version is recommended?

Python 3.12.

### Q2. Is object-oriented programming mandatory?

Yes.

### Q3. Should virtual environments be used?

Yes.

### Q4. Is Git required?

Yes.

### Q5. Are projects mandatory?

Yes.

---

# 35. Training Ownership

This Python Bootcamp Training Manual is maintained by the Learning & Development Department and Engineering Department of TechNova Solutions Pvt. Ltd.
