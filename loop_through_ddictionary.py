employee ={
    "name": "mahfuza",
    "skills": ["python","django","java"],
    "experience": 1
}

print(employee.keys())

print(employee.values())

print(employee.items())

for current_key in employee.keys():
    print(current_key, employee[current_key])