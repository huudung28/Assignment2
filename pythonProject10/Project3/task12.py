class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.set_name(name)
        self.set_id_number(id_number)
        self.set_department(department)
        self.set_job_title(job_title)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_id_number(self, id_number):
        self.id_number = id_number

    def get_id_number(self):
        return self.id_number

    def set_department(self, department):
        self.department = department

    def get_department(self):
        return self.department

    def set_job_title(self, job_title):
        self.job_title = job_title

    def get_job_title(self):
        return self.job_title

    def __str__(self):
        return f"--------- EMPLOYEE INFORMATION ---------\nName: {self.name}\nID Number: {self.id_number}\nDepartment: {self.department}\nJob Title: {self.job_title}"


emp1 = Employee("Susanna Myer", "47899", "Accounting", "Vice President")

emp2 = Employee("Mark Joseph", "39119", "Info Tech", "Programmer")

emp3 = Employee("Joyce Roberts", "81774", "Manufacturing", "Engineer")

# print(emp1)
# print(emp2)
# print(emp3)