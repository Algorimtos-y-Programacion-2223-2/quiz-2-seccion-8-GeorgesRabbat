from Data import products
from Ropa import Ropa
from Hogar import Hogar
from Gaming import Gaming


class Main:
    def __init__ (self):
        self.ropa_lista = []
        self.gaming_lista = []
        self.hogar_lista = []


    def constructor (self):
        for k, lista in products.items():
            for diccionario in lista:
                new_hogar = Hogar (diccionario)
                self.hogar_lista.append(new_hogar)

        for k, lista in products.items():
            for diccionario in lista:
                new_gaming = Gaming (diccionario)
                self.gaming_lista.append(new_gaming)

        for k, lista in products.items():
            for diccionario in lista:
                new_ropa = Ropa (diccionario)
                self.ropa_lista.append(new_ropa)






