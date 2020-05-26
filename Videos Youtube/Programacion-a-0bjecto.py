import os
os.system("cls")

#Video 26
class Coche():

    #Constructodo, metodo inicial
    # al poner __ estamos encazuplando una variable que no se puede modificar desde fuera
    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos

        if (self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif (self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo el carro no puede arrancar"
        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche tiene ",self.__ruedas, " Ruedas.  Un ancho de ",self.__anchoChasis,
        "Y un largo de ",self.__largoChasis)

    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gazolina="ok"
        self.aceite="ok"
        self.puerta="cerradas"

        if (self.gazolina=="ok" and self.aceite=="ok" and self.puerta=="cerradas"):
            return True

        else:
            return False

miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()

#Video 27

print("-----------------------------2 do objecto------------------------")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()