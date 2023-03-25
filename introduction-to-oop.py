class Company:
    def __init__(self, name, year):
        self.name = name
        self.year = year

class Ram:
    def __init__(self,model,size):
        self.model = model
        self.size = size

class Computer: 
    def __init__(self, name, color, ram, comp):
        self.name = name
        self.color = color
        self.ram = ram
        self.company = comp

class Person:
   def __init__(self, f_name , l_name, age, cmp): # Constructor
        self.first_name = f_name
        self.last_name = l_name 
        self.age = age
        self.computer = cmp

aljawharah = Person("aljawharah", "alqahtani", "14", Computer("macbook", "blue", Ram("abc", 8394), Company("khalid_law", 1876)))

print(aljawharah.first_name)
print(aljawharah.last_name)
print(aljawharah.age)
print(aljawharah.computer.name)
print(aljawharah.computer.color)
print(aljawharah.computer.ram.model)
print(aljawharah.computer.ram.size)
print(aljawharah.computer.company.name)
print(aljawharah.computer.company.year)


# oop class object instance __init__ self constructor attributes methods nested-objects
