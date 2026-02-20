attendance_list = ()
employee_attendance = input("Enter the employee attendance (P for present, A for absent): ")
attendance_percentage = (employee_attendance.count('P') / len(employee_attendance)) * 100
if attendance_percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")