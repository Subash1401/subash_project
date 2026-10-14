def stu(**detail):
    for i,(key,values) in enumerate( detail.items(),start=1):
        print(i,key,values)



student = {
    "name": "Hari",
    "age": 25,
    "course": "Python",
    "city": "Chennai"
}

stu(**student)