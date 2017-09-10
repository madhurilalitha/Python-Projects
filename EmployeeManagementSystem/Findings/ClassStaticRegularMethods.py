#class methods vs regular methods vs static methods
#regular methods -automatically take the instance as the first argument ("self" by convention)
#class methods - takes "cls" as the first argument ("a decorator class-method should be used)
#static methods - dont pass anything automatically - behave just like regular functions just because they have some connection
# with the classes
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
    @classmethod
    def set_raise_amount(cls,amount): #"cls should be used as convention not class as it is a python keyword"
        cls.raise_amount=amount
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)
    #Few people write class methods and regular methods which should be static methods
    # usually the giveaway is that when a method does not access the instance anwhere within the function - staticmethod should be used
    # we can pass arguments that we are going to work with
    @staticmethod #decorator
    def is_workday(day):#this has a logical connection to the Employee class but it does not specifically depend on any instance or class variable
        if day.weekday() == 5 or day.weekday()==6:
            return False
        return True

import datetime
my_date = datetime.date(2017,9,9)
print ("Whether the entered day is a weekday or not")
print (Employee.is_workday(my_date))

print ("Employee 3 details")
emp3 = 'John-Doe-70000'
emp3 = Employee.from_string(emp3)
print(emp3.email)
print (emp3.epay)

emp1 = Employee('Manoj','Kumar',1000)
emp2 = Employee('Lalitha','Madhuri',2000)

print (Employee.raise_amount)
print(emp1.raise_amount)
print (emp2.raise_amount)

print ("After calling the raise_amount function")

Employee.set_raise_amount(1.05) # modifying the class variable by calling a function - all instances are modified
print (Employee.raise_amount)
print(emp1.raise_amount)
print (emp2.raise_amount)

print ("Important : Calling through instance also modifies the class variable")
emp2.set_raise_amount(1.05) # modifying the class variable by calling a function by instance- all instances are modified
print (Employee.raise_amount)
print(emp1.raise_amount)
print (emp2.raise_amount)

# Class Methods may also be used as alternative constructors. Class methods provides multiple of ways of creating our object

