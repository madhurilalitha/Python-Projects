#Creating and instantiating python classes
#classes - they allow us to logically group data(attributes) and functions (methods)
'''class Employee:
    pass
print ("Class (Blueprint) vs Instance")
emp1 = Employee()
emp2 = Employee()
print (emp1)
print (emp2)

print ("instance variables contains data unique to each instance")
emp1.first ='Manoj'
emp1.last = 'Putchala'
emp1.email = 'manojkumar@gmail.com'
emp1.pay = 5000

emp2.first ='Lalitha'
emp2.last = 'Putchala'
emp2.email = 'Lalithakumar@gmail.com'
emp2.pay = 6000

print (emp1.email)
print (emp2.email)

'''
class Employee:
    #Constructor or Initializer #Instance is called as self(by default should be used)
    #Name, email and pay are attributes
    def __init__(self,first,last, pay):
        self.fname = first
        self.lname = last
        self.epay = pay
        self.email = first+'.'+last+'@company.com'

    def fullname(self): #method for code reuse #self should not be forgotten (one common mistake)
        return '{} {}'.format(emp1.fname,self.lname)


emp1 = Employee('Manoj','Kumar',100000)
print (emp1.epay)
print (emp1.fullname())

print (Employee.fullname(emp1)) # another way of calling the instance using class
