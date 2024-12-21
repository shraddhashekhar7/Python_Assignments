# Single Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is an Animal. It makes a sound")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} is a dog. It's a {self.breed}. It barks")


dog = Dog("Buddy","Golden retriver")
dog.speak()

animal = Animal("Coli")
animal.speak()


 # Multiple Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is an Animal. It makes a sound")


class Color:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        print(f"The color is {self.color}")


class Dog(Animal, Color):
    def __init__(self, name, color, breed):
        Animal.__init__(self, name)
        Color.__init__(self, color)
        self.breed = breed

    def speak(self):
        print(f"{self.name} is a Dog. It barks. It's color is {self.color}")


dog = Dog("Buddy", "Golden", "Retriever")
dog.speak()
dog.display_color()


# Multilevel Inheritance

class Company:
    def __init__(self, name):
        self.name = name

    def show_company(self):
        print(f"Company: {self.name}")


class Department(Company):
    def __init__(self, name, department_name):
        super().__init__(name)
        self.department_name = department_name

    def show_department(self):
        print(f"Company: {self.name}  Department: {self.department_name}")


class Employee(Department):
    def __init__(self, name, department_name, employee_name):
        super().__init__(name, department_name)
        self.employee_name = employee_name

    def show_employee(self):
        print(f"Employee Name: {self.employee_name}")


employee = Employee("Meta", "Engineering", "John Wick")
employee.show_company()
employee.show_department()
employee.show_employee()

