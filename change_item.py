employee ={
    "name": "mahfuza",
    "skills": ["python","django","java"],
    "experience": 1
}
#change item
employee["name"] = "test user"
print(employee["name"])

employee.update(
    {"name": "test user",
      "experience": 3
    }
)
print(employee)