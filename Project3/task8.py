from task12 import Employee


class Contractor(Employee):
    def __init__(self, name, id_number, department, job_title, contract_end_date, abn, fixed_salary):
        super().__init__(name, id_number, department, job_title)
        self.set_contract_end_date(contract_end_date)
        self.set_abn(abn)
        self.set_fixed_salary(fixed_salary)

    def set_contract_end_date(self, contract_end_date):
        self.contract_end_date = contract_end_date

    def get_contract_end_date(self):
        return self.contract_end_date

    def set_abn(self, abn):
        self.abn = abn

    def get_abn(self):
        return self.abn

    def set_fixed_salary(self, fixed_salary):
        self.fixed_salary = fixed_salary

    def get_fixed_salary(self):
        return self.fixed_salary

    def __str__(self):
        return "---------- CONTRACTOR INFOR ----------\nName: {}\nID number: {}\nDepartment: {}\nJob Title: {}\nContract end date: {}\nAbn: {}\nFixed salary: {}".format(
            self.get_name(), self.get_id_number(), self.get_department(), self.get_job_title(),
            self.get_contract_end_date(), self.get_abn(), self.get_fixed_salary())


def main():
    contractor1 = Contractor("John", "400123", "IT", "Manager", "2022/10/23", "51824753556", "4000$")

    print(contractor1)

    contractor2 = Contractor("Kenny", "500156", "HR", "Leader", "2024/09/23", "50110219460", "6000$")

    print(contractor2)


main()
