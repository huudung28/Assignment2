from task12 import Employee


class ShiftEmployee(Employee):
    def __init__(self, name, id_number, department, job_title, shift_number, hourly_pay_rate):
        super().__init__(name, id_number, department, job_title)
        self.set_shift_number(shift_number)
        self.set_hourly_pay_rate(hourly_pay_rate)

    def set_shift_number(self, shift_number):
        self.shift_number = shift_number

    def get_shift_number(self):
        return self.shift_number

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.hourly_pay_rate = hourly_pay_rate

    def get_hourly_pay_rate(self):
        return self.hourly_pay_rate

    def __str__(self):
        return "---------- SHIFT EMPLOYEE INFOR ----------\nName: {}\nID number: {}\nDepartment: {}\nJob Title: {}\nShift number: {}\nHourly Pay Rate: {}".format(self.get_name(), self.get_id_number(), self.get_department(), self.get_job_title(), self.get_shift_number(), self.get_hourly_pay_rate())


def init_shift_employee_obj():
    print("----------------- SHIFT EMPLOYEE INPUT -----------------")
    name = input("Name: ")
    id_number = input("ID Number: ")
    department = input("Department: ")
    job_title = input("Job Title: ")
    shift_number = int(input("(1): day shift or (2): night shift: "))
    hourly_pay_rate = input("Hourly Pay Rate: ")

    return ShiftEmployee(name, id_number, department, job_title, shift_number, hourly_pay_rate)


dayShiftEmp = init_shift_employee_obj()
nightShiftEmp = init_shift_employee_obj()

print(dayShiftEmp)
print(nightShiftEmp)
