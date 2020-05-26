import os,time ; os.system("cls")
#VIDEO 26
print("\n==================     Video 26        ==================")
class celular():
    
    #Esto funciona como estado inicial
    def __init__(self):
        #Al colocar dos __ se enclausan su valor, no se puede cambiar de afuera
        self.__color="Rojo"
        self.__grosor=50
        self.__altura=100
        self.__peso=2
        self.__conectividad=False
        self.__musica=False

    def internet(self):
        self.__conectividad=True
    
    def estado(self):
        if(self.__conectividad==False):

            return "El celular no tiene conexión, intente de nuevo "
        else:
            return "El celular tiene conexion a internet"

    def music(self,musica2):
        self.__musica=musica2
        
        if self.__musica==True:
           chequeo=self.__cheque()

        if (self.__musica==True and chequeo==True):
            print("Su celular permite reproducir musica")
        
        elif (self.__musica==True and chequeo==False):
            print("Algo fallo en su celular...")

        else:
            print("Su celular no permite reproducir musica")

    def propiedades(self):
        print("EL color del celular es: ",self.__color)
        print("La Altura del celular es: ",self.__altura)
        print("EL peso del celular es: ",self.__peso)
        print("")


    #Al poner __ estoy enclasurando este metodo, que solo puede cambiar desde dentro de la clase
    def __cheque(self):
        print("Realizando chequeo interno");time.sleep(2)

        self.bocina="listo"
        self.microfono="listo"
        self.camara="apagada"

        if (self.bocina=="listo" and self.microfono=="listo" and self.camara=="apagada"):
            return True

        else:
            return False


#--------------Objeto 1
celu=celular()
celu.propiedades()
celu.internet();print(celu.estado())
(celu.music(True))

#VIDEO 27
#--------------Objeto 2
print("\n==================     Video 27        ==================")
celu2=celular()
celu2.propiedades()
print(celu2.estado())
(celu2.music(False))
