import sys
import json
from task12 import *

try:
    with open("data.json", "r") as f:
        employees = json.load(f)
except:
    employees = {}


def print_employees():
    for v in employees.values():
        print(v)


def get_employee():
    id_number = input("ID number = ")

    print(employees.get(id_number, "Id number is invalid!"))


def add_employee():
    name = input("Employee's name: ")
    id_number = input("Employee's ID number: ")
    department = input("Employee's department: ")
    job_title = input("Employee's Job Title: ")

    employee = Employee(name, id_number, department, job_title)

    employees.update({id_number: employee.__dict__})
    print_employees()


def update_employee():

    id_number = input("ID number = ")

    if id_number in employees.keys():
        name = input("Employee's name: ")
        department = input("Employee's department: ")
        job_title = input("Employee's Job Title: ")

        employee = Employee(name, id_number, department, job_title)

        employees[id_number] = employee.__dict__
        print_employees()
    else:
        print("Id number is invalid!")


def delete_employee():
    id_number = input("ID number = ")

    if id_number in employees.keys():
        del employees[id_number]
        print_employees()
    else:
        print("Id number is invalid!")


def write_to_file():
    with open("data.json", "w") as fp:
        json.dump(employees, fp, indent=4)


def quit():

    write_to_file()
    sys.exit(0)


choices = {
    1: get_employee,
    2: add_employee,
    3: update_employee,
    4: delete_employee,
    5: quit
}


def menu():
    print("""---------------- EMPLOYEE MANAGEMENT ----------------
1. Get employee
2. Add employee
3. Update employee
4. Delete employee
5. Quit 
-----------------------------------------------------""")
    while True:
        choice = int(input("Enter your choice: "))
        if choice in choices:
            choices[choice]()
        else:
            print("Choice is invalid!")


menu()
