#Video 18, continue, pass, else

cooro=str(input("Ingresar un correo: "))
for we in cooro:

    if we =="@":
        arroba=True
        break
else:
    arroba= False

print(arroba)

for letra in "python":

    if letra=="h":
        continue
    print("La letra es: ",letra)


#Aqui cuenta cuentas cuantas letras hat, incluyendo espacios
nombre="Carlos Diaz"
print(len(nombre))

#aqui contamos las palabras pero evitamos contar el espacio
contadorr=0
for rt in nombre:
    if rt==" ":
        continue
    contadorr+=1

print(contadorr)




#VIDEO 17; CICLO WHILE

#Sacar raiz
import math
numero=int(input("Ingrese un numero: "))
intentos=0

while numero<0:
    print("El numero no puede ser menor que 0")
    numero=int(input("Ingrese un numero: "))
    if numero<0:
        intentos=intentos+1
    
    if intentos==3:
        print("Ya no tienes mas intentos intentas mas tarde...")
        break

if intentos<3:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de:",numero, " es : ",solucion)
    
#Prueba con edad
edad=int(input("Introduce su edad: "))
while (edad<0 or edad>100):
    print("ingresaste una edad incorrecta vuelva y intente")
    edad=int(input("Cual es su edad: "))
print("Su edad es: ",edad)

a=1
while a<=10:
    print("El numero es: "+str(a))
    a=a+1
    
#VIDEO 16; 

#Aqui dice si es correo es correcto solo con una arroba
valido=False
mail=str(input("Introduce tu Correo: "))

for z in range (len(mail)):
    if mail[z]=="@":
        valido= True
if valido:
    print("El mail es correcto ")
else:
    print("el correo es invalido")



#Aqui va de 0 a 100, contando de dos en dos
for g in range (0,10+1,2):
    print(g)

#aqui estamos uniendo la variable t con el texto
for t in range (5):
    print(f"El numero es: {t}")




#VIDEO 15; CICLO FOR
email=False
email2=str(input("Ingrese su correo eletronico: "))

for q in email2:
    if q=="@":
        for w in email2:
            if w==".":
                email=True

if email == True:
    print("el correo es correcto")
else:
    print("El correo es incorrecto")
for a in [2,3,4,5]:
    print("QLOQ ", end="")
for w in "mariposa":
    print("dime")


#Video 14; Ciclo For

#aqui por cada paalabra imprime hola
for i in ["Carlos","Jose", "Maria","Jose"]:
    print("Hola: "+i)

for a in ["\nUno","\nDos","\nTres","\nCuatro\n"]:
    print(a)

