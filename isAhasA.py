# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass


# Animal is-a instance of class Dog and ha-a name
class Dog(Animal):
    def __init__(self, name):
        self.name = name


# Animal is-a instance of class Cat and has-a name
class Cat(animal):
    def __init__(self, name):
        self.name = name


# Class person has-a name
class Person(object):
    def __init__(self, name):
        self.name = name

        self.pet = None


# Person is-a object of class Employee.
class Employee(Person):
    def __init__(self, name, salary):
        # Which is-a part of class super which has-a object Employee
        super(Employee, self).__init__(name)
        # This instance of Employee has-a salary and is-a super employee and is-a employee
        self.salary = salary


# class fish has-a object
class Fish(object):
    pass


# Fish is-a object of class Salmon
class Salmon(Fish):
    pass


# Fish is-a object of class Halibut
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")


# satan is-a Cat
satan = Cat("Satan")


# mary is-a person
mary = Person("Mary")

# mary is-a person that has-a cat satan
mary.pet = satan

# Frank is-a employee and has-a salary 120000
frank = Employee("Frank", 120000)

# frank is-a person that has a dog
frank.pet = rover

# flipper is-a fish
flipper = fish()

# crouse is-a salmon
crouse = Salmon()

# harry is-a halibut
harry = halibut()
