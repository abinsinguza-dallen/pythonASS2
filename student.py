class Student:
    def __init__(self,name,age,country,first_name,second_name):
        self.name=name
        self.age=age
        self.country=country
        self.first_name=first_name
        self.second_name=second_name
        
    def greet(self):
        return f"hello {self.name}, welcome to {self.school},How is {self.country} "
    def fullname(self):
        return f"Hello {self.first_name} {self.second_name}"
    def year_of_birth(self):
        year=2022-self.age
        return f"Hello {self.first_name} {self.second_name} you were born in {year}"
    def initials(self):
        return f"{self.first_name[0]} {self.second_name[0]}"   