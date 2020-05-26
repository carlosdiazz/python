comida=["manzana","Pera","Coocolate"]
import datetime

# MODULOS O BIBLIOTECAS

print(datetime.date.today()) #Aqui imprime la fecha exacta
print(datetime.timedelta(minutes=990)) # Aqui cambia de minuto a hora

#Crear un modulo
#modulo_propio.add(5,10)


for i in comida:
    print(i)


#Tipos de datos

texto=str("Hola")

entero=int(3)

flotante=float(3.5)

booleano= True, False

lista=["hola",32,"como",32.43,True]

tuplas=("como estas",322,"ok gracias")

Set={"Rojo", "Azul"}


diccionario={"Canada":"Toronto","Francia":"Paris","Colmbia":"Bogota"}

dici={
    "nombre":"Jose",
    "Apellido":"Diaz"
}

#Variables

hey=" "+str(int(32+54))
sumar=3+2

nombre,apellido,edad="jose","diaz",13

# Usando print(dir(apellido))... puedo conocer todas las propiedades y metodos de mi str
print(apellido.title())

texto= "Hola Mundo"
print(f"Aqui dira esto {texto}")    #Usando la f para unir dos texto

print(texto.upper())        #Todo en mayuscula
print(texto.lower())        #Todo en minuscula
print(texto.swapcase())     #primera inical en minuscula
print(texto.capitalize())   #primer inicial enmayuscula
print(texto.split())        #separa el tesxto a partir de algo
print(len(texto))           #conocer longitud

print(texto.isnumeric())    #para conocer si es numerico 
print(texto.isalpha())      #Para saber si es alfanumerico

#############################################################################

print("Condicionales- \n \n \n")

print(3==3)

name="Carlos"
last_name="Diaz"
edad=12
ciudad="LV"

if name=="Carlos":
    if last_name=="Diaz":
        if edad==12:
            if ciudad=="LV":
                print("Entraste bien")

x=3
if x > 2 and x < 10:    #Aqui es verdadero si la dos son verdaderos
    print("Hola")   

if x > 2 or x < 10:     #Aqui se cumple solo con una condicon
    print("Hey")

if  x>2:
    if not (x==3):
        print("Algo mas")



comida=["Hola","Como","Estas"]

for i in comida:
    if i=="Hola":
        print("hasta aqui")
        break

for letras in "Car":
    print(letras)

x=0
while x<=4:
    print(x)
    x=x+1

def correr(name="Persona"):
    print("Hola, Señor: ",name)

# def sumar(nu1=0,nu2=0):
#     return nu1+nu2
# ju=sumar(10,20)         
# print(ju)


sum= lambda nu1,nu2: nu1+nu2
print(sum(15,15))

nombre="Carlos"

correr()
correr(nombre)

