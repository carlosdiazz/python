import os
os.system("cls")

class vehiculos():

    def __init__ (self,marca,modelo):

        self.marca=marca
        self.modelo=modelo
        self.enmcarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):      
        self.enmcarcha=True
    
    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True
    
    def estado(self):
        print("Marca: ",self.marca)
        print("\nModelo: ",self.modelo)
        print("\nEn marcha: ",self.enmcarcha)
        print("\nAcelerando: ",self.acelera)
        print("\nFrena: ",self.frena)

class furgoneta(vehiculos):
    
    def carga(self,cargar):
        self.cargado=cargar

        if self.cargado==True:
            return "La furgoneta esta cargada"
        
        else:
            return "La furgoneta no esta cargada"

class Moto(vehiculos):
    hcaballito="No estoy haciendo caballito"

    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"
    
    def estado(self):
        print("Marca: ",self.marca)
        print("\nModelo: ",self.modelo)
        print("\nEn marcha: ",self.enmcarcha)
        print("\nAcelerando: ",self.acelera)
        print("\nFrena: ",self.frena)
        print("\n",self.hcaballito)

class vehi_eletricos():

    def __init__(self):
        self.autonomia=100

    def cargar_energia(self):
        self.cargando=True

class bici_ele(vehi_eletricos,vehiculos):
    pass


mifurgoneta=furgoneta("Toyota","Kang")

mifurgoneta.arrancar()
mifurgoneta.acelerar()
mifurgoneta.estado()

print(mifurgoneta.carga(True))

print("--------------------------------------")
mimoto= Moto("Honda","Civic")
#mimoto.caballito()
mimoto.estado()

print("----------------------------------------")

mibici=bici_ele()