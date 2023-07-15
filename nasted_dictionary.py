courses={
    1:{
        "name":"c",
        "duration":3
    },
    2:{
        "name": "python",
        "duration":4
    }
}

print(courses[1]["name"])

print(courses[2]["duration"])

courses[2]["duration"] = 3
print(courses[2])

courses[2]["instructor"] = "mahfuza"
print(courses[2])