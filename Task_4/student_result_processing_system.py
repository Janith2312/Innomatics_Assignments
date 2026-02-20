marks = []

for i in range(1, 6):
    mark = int(input(f"Enter marks for subject {i}: "))
    marks.append(mark)
average_marks = sum(marks) / len(marks)
if average_marks >= 50:
    print("Student passed!")
else:
    print("Student failed.")