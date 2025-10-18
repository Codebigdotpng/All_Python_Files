# Makes the Dictionary in line 2,3,4,5 & 6
student={
    "name":"Karan",
    "age":10,
    "grade":"5th"
}
#Prints grade in line 8
print(student["grade"])
#updates age in line 10
student["age"]=11
#removes grade in line 12
student.pop("grade")
#Checks for score in line 14 & 15
if "score" not in student:
    student["score"]=90
#checks for "teacher" in line 17,18 and 19
student.get("teacher")
teacher = student.get("teacher", "No teacher assigned")
print(teacher)
#Loops through dictionary keys and values in line 21 & 22
for key, value in student.items():
    print(f"{key}: {value}")
#clears dictionary in line 24
student.clear()
