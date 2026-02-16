employees = {
    "Ravi": 75000,
    "Anita": 68000,
    "Kiran": 72000
}
highest_salary = max(employees.values())
for name, salary in employees.items():
    if salary == highest_salary:
        print(f"Highest Salary: {name} - {salary}")
