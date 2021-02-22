from Employee import Employee
import EmployeeFunctions as ef


def add_employee():

    ID = str(input("Please enter employee's ID: "))
    return ef.AddEmployee(ID)


def delete_employee():
    ID = str(input("Please enter employee's ID: "))
    return ef.DeleteEmployee(ID)


def print_employees():
    return ef.PrintEmployee()


add_employee()
print_employees()
# delete_employee()
