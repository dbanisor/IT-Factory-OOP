'''
O clasa abstracta este o clasa care are cel putin o metoda abstracta.
O metoda abstracta este o metoda fara corp (implementare).
'''

from abc import ABC, abstractmethod

# abc = abstract base class

class Animal(ABC):  # Animal este o clasa abstracta. Nu avem voie sa cream obiecte de tip Animal din acesta clasa deoarece nu are functii pe care sa le putem apela.
    @abstractmethod
    def sound(self):
        pass    # "pass" este o metoda prin care putem abstractiza o functie

    @abstractmethod
    def sleep(self):
        raise NotImplementedError   # "NotImplemented Error" este o alta metoda prin care putem abstractiza o functie. Diferenta este ca "raise" arunca eroare


class Dog(Animal):
    def sound(self):
        print("woof")

    def sleep(self):
        print("Zzz")

class Cat(Animal):
    def sound(self):
        print("meow")

    def sleep(self):
        print("Prrr")
