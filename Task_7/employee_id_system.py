class Employee:
    def __init__(self, name, emp_id, dept):
        self.name = name
        self.emp_id = emp_id
        self.dept = dept

    def display(self):
        print("Employee ID Card")
        print("Name:", self.name)
        print("ID:", self.emp_id)
        print("Department:", self.dept)


emp = Employee("Rahul", "EMP102", "IT")
emp.display()