attendance = ["P", "P", "A", "P", "P"]
total_classes = len(attendance)
present_count = attendance.count("P")
attendance_percentage = (present_count / total_classes) * 100
print(f"Attendance Percentage: {attendance_percentage:.2f}%")