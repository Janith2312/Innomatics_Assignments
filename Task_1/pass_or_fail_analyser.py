marks = [45, 78, 90, 33, 60]
pass_students = []
for i in marks:
    if i >= 50:
        pass_students.append(i)

print("Number of students who passed:", len(pass_students))
print("Number of students who failed:", len(marks) - len(pass_students))