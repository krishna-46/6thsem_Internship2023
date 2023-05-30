class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_salary(self):
        return self.salary
    def get_salary_increase(self, percentage):
        self.salary *= (1 + percentage / 100)
    def is_elderly(self):
        return self.age >= 60
employees = [
    Employee("John Doe", 45, 5000.0),
    Employee("Jane Smith", 55, 6000.0),
    Employee("Bob Johnson", 65, 7000.0),
    Employee("Alice Williams", 70, 8000.0),
]
salary_increase_percentage = 10
list(map(lambda emp: emp.get_salary_increase(salary_increase_percentage), employees))
elderly_employees = list(filter(lambda emp: emp.is_elderly(), employees))
for emp in elderly_employees:
    print("Name:", emp.get_name())
    print("Age:", emp.get_age())
    print("Salary:", emp.get_salary())
    print()
