'''
Polimorfismul se refera la abilitatea unui obiect de a se comporta in mai multe moduri, in functie de context.
In esenta, polimorfismul permite obiectelor de acelasi tip sa aiba comportamente diferite fara a fi necesar sa se stie tipul lor exact inainte de executie.
'''

from abc import ABC, abstractmethod
from pprint import pprint


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Creature(ABC):
    @abstractmethod
    def eat(self):
        pass


class Animal(Creature):
    def __init__(self, age, weight, species):
        self.age = age
        self.weight = weight
        self.species = species

    def eat(self):
        return f"I am an eating {self.__class__.__name__}"  # I am an eating animal.


class DomesticAnimal(Animal):
    def __init__(self, age, weight, species, owner):
        super().__init__(age, weight, species)
        self.owner = owner


class Pet(DomesticAnimal):
    def __init__(self, age, weight, species, owner, name):
        super().__init__(age, weight, species, owner)
        self.name = name


class WildAnimal(Animal):
    def __init__(self, age, weight, species, location):
        super().__init__(age, weight, species)
        self.location = location


p1 = Person("Sergiu", 24)
p2 = Person("Valentina", 23)
animals = [
    DomesticAnimal(age=5, weight=130, owner=p1, species="Cow"),
    Pet(name="Puffi", age=3, weight=4, owner=p2, species="Dog"),
    Pet(name="Pisu", age=1, weight=3, owner=p2, species="Cat"),
    Pet(name="Rexi", age=2, weight=3, owner=p1, species="Dog"),
    WildAnimal(age=25, weight=230, species="Bear", location="forest"),
    WildAnimal(age=18, weight=67, species="Wolf", location="forest"),
    WildAnimal(age=10, weight=59, species="Wolf", location="forest"),
    WildAnimal(age=40, weight=310, species="Elephant", location="jungle"),
    WildAnimal(age=33, weight=99, species="Giraffe", location="jungle"),
    DomesticAnimal(age=1, weight=2, owner=p1, species="Chicken"),
    DomesticAnimal(age=1, weight=145, owner=p2, species="Pig"),
    WildAnimal(age=2, weight=2, species="Squirrel", location="forest")
]


def animals_eat(animals):
    for x in animals:
        print(x.eat())


animals_eat(animals)


# Sa se scrie o functie care primeste ca parametru o lista de animale si returneaza doar animalele domestice din acea lista.

def get_all_domestic_animals(animals):
    li = []
    for x in animals:
        # if isinstance(x, DomesticAnimal) and type(x) == DomesticAnimal:  # -----> daca vrem doar obiecte strict de tip DomesticAnimal
        if isinstance(x,
                      DomesticAnimal):  # -----> asa arata daca x este DomesticAnimal dar si orice altceva (Pet spre exemplu)
            li.append(x)
    return li


pprint(get_all_domestic_animals(animals))
