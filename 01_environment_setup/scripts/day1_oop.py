class Dataset:
    def __init__(self, name, rows):
        self.name = name
        self.rows = rows
    def info(self):
        return f"Dataset '{self.name}' contains '{self.rows}' rows"
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def printDetails(self):
        print(f"Employee Name: {self.name} \nSalary: {self.salary}")
class Car:
    def __init__(self, brand, color, horsepower):
        self.brand = brand
        self.color = color
        self.horsepower = horsepower
    def output(self):
        return f"{self.color} {self.brand} {self.horsepower}"
class Hatch_Back(Car):
    def __init__(self, brand, color, horsepower):
        super().__init__(brand, color, horsepower)
    def output(self):
        return super().output()


class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class Patient:
    def __init__(self,name, age):
        self.name = name
        self.__age = age
    def getAge(self):
        return self.__age
    def setAge(self,age):
        if age > 0:
            self.__age = age
        else:
            print("Age can not be negative.")

class Bird:
    def sound(self):
        return "Chirp"

class Cat:
    def sound(self):
        return "Meow"

class Model:
    def train(self):
        raise NotImplementedError("Train method must be implemented by subclass")

class LinearRegression(Model):
    def train(self):
        print("Training Linear Regression...")

class DecisionTree(Model):
    def train(self):
        print("Training Decision Tree...")

models = [LinearRegression(), DecisionTree()]
for model in models:
    model.train()


"""for animal in [Bird(), Cat()]:
    print(animal.sound())


malik = Patient("Malik", 20)
print(f"Pateint name: {malik.name} \nPateint Age: {malik.getAge()}")


child = Child("BOb",  20)
print(f"{child.name} {child.age}")

hustler = Car("Suzuki", "Yellow", 68)
print(hustler.output())

swift = Hatch_Back("Suzuki", "Grey", 112)
print(swift.output())

data = Dataset("Sales", 5000)
print(data.info())

emp = Employee("Shahbaz", 50000)
emp.printDetails()

car1 = Car("Toyota", "Yellow", 200)
print(car1.output())"""