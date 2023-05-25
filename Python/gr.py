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
        self.salary += (self.salary * percentage) / 100

    def is_elderly(self):
        if self.age >= 60:
            return True
        else:
            return False


employees = [Employee("John", 45, 50000), Employee("Mary", 65, 60000), Employee("Bob", 55, 70000)]


list(map(lambda x: x.get_salary_increase(10), employees))


elderly_employees = list(filter(lambda x: x.is_elderly(), employees))
