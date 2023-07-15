employee ={
    "name": "mahfuza",
    "skills": ["python","django","java"],
    "experience": 1
}

employee["company name"] ="cefalo bangladesh ltd"

print(employee)

employee.update(
    {
        "address":"bangladesh"
    }
)
print(employee)


#del keyword diye remove kora jay
del employee["address"] 
print(employee)


employee.pop("skills")
print(employee)