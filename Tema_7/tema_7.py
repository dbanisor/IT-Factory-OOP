from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print("Cel mai probabil am colturi.")


class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        print("Se seteaza latura")
        return self.__latura

    @latura.getter
    def latura(self):
        print("Se returneaza latura")
        return self.__latura

    @latura.setter
    def latura(self, dimensiune):
        print("Se modifica dimensiunea")
        self.__latura = dimensiune

    @latura.deleter
    def latura(self):
        print("Se sterge latura.")
        self.__latura = None

    def aria(self):
        return self.__latura ** 2


patrat = Patrat(10)

print(patrat.latura)  # ---> getter
patrat.latura = 5  # ---> setter
print(patrat.latura)  # ---> getter
del patrat.latura  # ---> deleter
patrat.latura = 10  # ---> setter
print(patrat.latura)  # ---> getter
print(patrat.aria())  # ---> getter


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza


    @property
    def raza(self):
        print("Se seteaza raza")
        return self.__raza

    @raza.getter
    def raza(self):
        print("Se printeaza raza")
        return self.__raza

    @raza.setter
    def raza(self, valoare):
        print("Se modifica raza")
        self.__raza = valoare

    @raza.deleter
    def raza(self):
        print("Se sterge raza")
        self.__raza = None

    def aria(self):
        return FormaGeometrica.PI * (self.__raza ** 2)

    def descrie(self):
        print("Eu nu am colturi.")


cerc = Cerc(5)
print(cerc.aria())
cerc.descrie()