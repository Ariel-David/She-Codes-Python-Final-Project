from Employee import Employee
import csv
from csv import DictReader
import os.path
from prettytable import from_csv


def AddEmployee(ID):

    employee = Employee()
    employee.ID = ID
    employee.updateFirstName()
    employee.updateLastName()
    employee.updateBirthDate()
    employee.updatePhoneNumber()
    employee.updatePosition()
    employee.updateManager()

    file_exist = os.path.isfile('employee_file.csv')
    if file_exist:
        # Check if this employye exist in the csv file
        with open('employee_file.csv', mode='r') as csv_read:
            csv_dict_reader = DictReader(csv_read)
            for row in csv_dict_reader:
                if(row['id'] == employee.ID):
                    print("Employee already exist")
                    return

    values = [employee.ID, employee.FirstName, employee.LastName,
              employee.BirthDate, employee.PhoneNumber, employee.Position, employee.Manager]

    with open('employee_file.csv', mode='a', newline='') as csv_file:

        fieldnames = ['id', 'first_name', 'last_name',
                      'birth_date', 'phone_number', 'position', 'manager']

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        if not file_exist:
            writer.writeheader()

        writer.writerow(dict(zip(fieldnames, values)))
        print("Employee successfully added")

        csv_file.close()


def DeleteEmployee(ID):
    lines = list()

    with open('employee_file.csv', mode='r') as csv_read:
        reader = csv.reader(csv_read)
        for row in reader:
            lines.append(row)
            for field in row:
                if(field == ID):
                    lines.remove(row)

    with open('employee_file.csv', mode='w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(lines)

    print("Employee successfully deleted")


def PrintEmployee():
    with open('employee_file.csv') as fp:
        mytable = from_csv(fp)
    print(mytable)
