'''
3 tipuri de metode si atribute:

- public -> accesibile peste tot
- protected -> accesibile doar in ierarhia de mostenire (_atribut)
- private -> accesibile doar in clasa (__atribut)
'''


class Car:
    __model = "Dacia"

    # pt a putea accesa totusi atributele private ale clasei trebuie implementate functiile "getter" si "setter"

    def get_model(self):  # Getter ----> Returneaza datele
        return self.__model

    def set_model(self, new_model):  # Setter ----> Modifica sau actualizeaza datele
        self.__model = new_model


car = Car()
# print(car.__model)  # nu te va lasa sa il accesezi pt ca este un atribut privat, doar pt ca am pus "__" inainte de numele atributului

print(car.get_model())
print(car.set_model("BMW"))
print(car.get_model())

#                   *********************** Incapsulare folosind properties (in loc de SETTER si GETTER) ***********************

class Car:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        print("Setting as property")
        return self.__color

    # @color.getter         # va merge chiar daca nu setam getter-ul deoarece va merge unde am setat @property si va putea astfel printa culoarea deci nu e obligatoriu sa setam getter-ul
    # def color(self):
    #     print("Getting value")
    #     return self.__color

    @color.setter
    def color(self, value):
        print("Setting new value")
        self.__color = value

    @color.deleter
    def color(self):
        print("Deleting value")
        self.__color = None

    @property
    def is_painted(self):
        return self.__color is not None and self.__color != "white"

car = Car("blue")
print(car.color)   # ----> pt a apela @color.getter sau @property (in cazul in care nu am definit un setter)
# pt ca am setat property de color, doar prin apelarea atributului "color" este apelata functia "color getter". Nu este nevoie de paranteze la print(car.color) deoarece color este un atribut

car.color = "red"  # ----> pt a apela @color.setter
print(car.color)

print(car.is_painted)
del car.color  # ----> pt a apela @color.deleter
print(car.color)

print(car.is_painted)  # ----> pt a apela @property is_painted (fara paranteze pt ca este o proprietate)
