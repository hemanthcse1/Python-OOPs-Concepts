

class Person:

    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person created")
        Person.population +=1

    def __str__(self):
        return f"My name is {self.name}, and my age is  {self.age}"

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __del__(self):
        print("Person deleted")
        Person.population -= 1

    @classmethod
    def get_population(cls):
        return Person.population


person1 = Person("Hemanth",30)
person2 = Person("Kumar",32)
person3 = Person("Ritchie",33)

print(person1)
print(person2)
print(person3)

print(f"Population is {Person.get_population()}")
