class Employee:
    raise_amt=1.04
    def _init_(self,first,last,empid,pay):
        self.first=first
        self.last=last
        self.empid=empid
        self.pay=pay
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)
    def display_details(self):
        print("First name of employee is"+" "+ str(self.first))
        print("Last name of employee is"+" "+ str(self.last))
        print("Employee id of employee is"+" "+ str(self.empid))
        print("Pay of the employee is"+" "+ str(self.pay))
class Developer(Employee):
    raise_amt=1.05
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)
class Manager(Employee):
    raise_amt=1.06
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)
f=1
while(f):
    print("1.Developer \n 2.Manager \n 3.Exit")
    ch=int(input("Enter your choice"))
    if(ch==1):
        print("Enter the number of developers you want to enter")
        dev=int(input("enter the number"))
        for i in range(0,dev):
            first=input("Enter first name")
            last=input("Enter last name")
            empid=input("Enter employee id")
            pay=float(input("enter your pay"))
            emp1=Developer(first,last,empid,pay)
            emp1.apply_raise()
            emp1.display_details()
    elif(ch==2):
        man=int(input("Enter the  number of Managers"))
        for i in range(0,man):
           
            first=input("Enter first name")
            last=input("Enter last name")
            empid=input("Enter employee id")
            pay=float(input("enter your pay"))
            emp2=Manager(first,last,empid,pay)
            emp2.apply_raise()
            emp2.display_details()
    elif(ch==3):
        f=0
    else:
        print("Invalid Input")
        