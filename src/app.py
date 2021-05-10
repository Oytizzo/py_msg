# python oop

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    @property
    def email(self):
        return self.first + '.' + self.last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith', 40000)
emp_2 = Employee('Devid', 'Hobarmann', 30000)

print(emp_1)
print(emp_2)
print(emp_1.fullname())
print(emp_1.email)

emp_1.first = 'lisa'
print(emp_1.fullname())
print(emp_1.email)
