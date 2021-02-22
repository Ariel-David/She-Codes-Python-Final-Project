import re


class Employee:
    def __init__(self, FirstName=None, LastName=None, ID=None, BirthDate=None, PhoneNumber=None, Position=None, Manager=None):
        self.ID = ID
        self.FirstName = FirstName
        self.LastName = LastName
        self.BirthDate = BirthDate
        self.PhoneNumber = PhoneNumber
        self.Position = Position
        self.Manager = Manager

    def updateID(self):
        txt = str(input("Please Enter your ID number: "))
        regular = re.search("\d{9}", txt)
        while not re.search("\d{9}", txt):
            txt = str(input("ID IS NOT CURRECT. Enter your ID number Again: "))
        else:
            self.ID = txt
            print("Id Update successfuly")

    def updateFirstName(self):
        txt = str(input("Please Enter your First Name: "))
        regular = re.search("[a-zA-Z]", txt)
        while not re.search("[a-zA-Z]", txt):
            txt = str(
                input("First Name IS NOT CURRECT. Enter your First Name number Again: "))
        else:
            self.FirstName = txt
            print("First Name Update successfuly")

    def updateLastName(self):
        txt = str(input("Please Enter your Last Name: "))
        regular = re.search("[a-zA-Z]", txt)
        while not re.search("[a-zA-Z]", txt):
            txt = str(
                input("Last Name IS NOT CURRECT. Enter your Last Name number Again: "))
        else:
            self.LastName = txt
            print("Last Name Update successfuly")

    def updateBirthDate(self):
        txt = str(input("Please Enter your Birth Date: "))
        regular = re.search("(\d{2}/\d{2}/\d{4})", txt)
        while not re.search("(\d{2}/\d{2}/\d{4})", txt):
            txt = str(
                input("Birth Date IS NOT CURRECT. Enter your Birth Date number Again(dd/mm/yyyy): "))
        else:
            self.BirthDate = txt
            print("Birth Date Update successfuly")

    def updatePhoneNumber(self):
        txt = str(input("Please Enter your Phone number: "))
        regular = re.search("\d{10}", txt)
        while not re.search("\d{10}", txt):
            txt = str(
                input("Phone Number IS NOT CURRECT. Enter your Phone Number Again: "))
        else:
            self.PhoneNumber = txt
            print("Phone Number Update successfuly")

    def updatePosition(self):
        txt = str(input("Please Enter your Position: "))
        regular = re.search("[a-zA-Z]", txt)
        while not re.search("[a-zA-Z]", txt):
            txt = str(
                input("Position IS NOT CURRECT. Enter your Position Again: "))
        else:
            self.Position = txt
            print("Position Number Update successfuly")

    def updateManager(self):
        txt = str(input("Please Enter your Manager: "))
        regular = re.search("[a-zA-Z]", txt)
        while not re.search("[a-zA-Z]", txt):
            txt = str(
                input("Manager IS NOT CURRECT. Enter your Manager Again: "))
        else:
            self.Manager = txt
            print("Manger Update successfuly")


em = Employee("Ariel", "David", 315581223, 4, 5)
# em.updateID()
# em.updateFirstName()
# em.updateLastName()
# em.updateBirthDate()
# em.updatePhoneNumber()
# em.updatePosition()
