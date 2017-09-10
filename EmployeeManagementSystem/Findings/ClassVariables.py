#class variables are shared among all instances of a class
#Instances variables are unique like name and pay

class Employee:

    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self,first,last,pay):
        self.fname = first
        self.lname = last
        self.epay = pay
        self.email = first+"."+last+"@company.com"
        Employee.num_of_emps+=1 #it is good to have class name value instead of instance depends upon logic
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)

    def apply_raise(self):
        self.epay = int(self.epay* self.raise_amount) #we can also use Employee.raise_amount
        #When we try to access attribute of an instance it first checks if that instance has the attribute,
        #if it doesn't, it checks if its class or its parent class contains the attribute

print ("Num of Employees before creation",Employee.num_of_emps)

emp1 = Employee('Manoj','Kumar',10000)
print("Emp1 pay before raise",emp1.epay)
emp1.apply_raise()
print("Emp1 pay after raise",emp1.epay)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp1.__dict__) #printing the namespace of emp1 instance --> returns a dictionary
print(Employee.__dict__)

print ("If we want to change the raise_amount variables using instance - changes for only instance")
emp1.raise_amount=1.05
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp1.__dict__)

print ("If we want to change the raise_amount variables using class - changes for both class and instances")
Employee.raise_amount=1.05
print(Employee.raise_amount)
print(emp1.raise_amount)

emp2 = Employee('Lalitha','Madhuri',20000)

print ("Num of Employees after creation",Employee.num_of_emps) #Count incremented whenever a new employee is instantiated
