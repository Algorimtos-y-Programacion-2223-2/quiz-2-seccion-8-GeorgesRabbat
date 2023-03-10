
class Edificio:
    def __init__(self, nombre, pisos, calle, ciudad, código_postal, apartamentos):
        self.nombre = nombre
        self.pisos = pisos
        self.calle = calle
        self.ciudad = ciudad
        self.codigo_postal = código_postal
        self.apartamento = apartamentos

    def mostrar_direccion (self):
        print (f'calle = {self.calle}')
        print (f'ciudad = {self.ciudad}')
        print (f'codigo_postal = {self.codigo_postal}')
    
    def mostrar_apartamento (self):
        print (f'nombre')




