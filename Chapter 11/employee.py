#Write a class called Employee. 
#first_name, last_name, and annual_salary should be attributes.
#Write a method called give_raise() that adds $5000 to the annual salary by default but also accepts a different raise amount.
class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        self.annual_salary += raise_amount