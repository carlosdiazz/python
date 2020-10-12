import os
#En este codigo se encuetran varios algortimos de la pagina https://www.codewars.com/dashboard nivel Basico

def main():
    hacer=int(input("Ingrese que quieres hacer: "))
    while True:
        os.system("cls")       

        if hacer == 0:
            break

        elif hacer == 1:
            palabra=input("Ingrese una palabra para saber su composicion: ")
            repetir(palabra)
        
        elif hacer == 2:
            palabra=input("Ingrese una palabra para saber la palabra que se repite: ")
            print(saber_repetidas(palabra))
        
        elif hacer == 3:
            print(friend(["Ryan", "Kieran", "Mark","jose","Maria","Cecilia","Carlos"]))

        elif hacer == 4:
            print(digital_root(132189 ))
            print(digital_root(493193 ))
        
        elif hacer == 5:
            print(to_camel_case("A-B-C"))
        
        elif hacer == 6:
            print(xo("xooxx"))
            print(xo("ooxXm"))
            print(xo("ooxXm"))
            print(xo("zzoo"))
        
        elif hacer == 7:
            lista=[1,2,'aasf','1','123',123,14] 
            print(sacar_numero(lista))
        
        hacer=int(input("Ingrese que quieres hacer: "))

def numeros_al100():
    i=0
    while i<100:
        i=i+1
        print(f"El numero es: {i}")

def impimir():
    hola="Hola Mundo"
    for i in hola:
        print(i)

def is_number(n):
       
        try:
	        entero = int(n)
	        return True
        except ValueError:
	        return False

def sacar_numero(lista):
    lista2=[]
    
    for i in lista:
        
        if is_number(i) == True:
            lista2.append(int(i))

    return list(set(lista2))
    #return lista2

#Aqui una funcion que si tiene x y o, igual devuelve True en cambio devuelve False, y si no tiene ni x ni o devuelve True
def xo(s):
    s=s.lower();o=0;x=0

    for i in s:        
        if i == "x":          
            x=x+1   
            
        elif i == "o":        
            o=o+1
            
    if x == o:
        return True

    else:
        if "x" not in  s:
            if "o" not in  s:
                return True
        return False

#Aqui una funcion que si hay un - o un _ , la siguiente letra sera mayuscula     
def to_camel_case(s):
    nueva=[]
    mayus=False
    for i in s:
        
        if i == "-" or i =="_":
            mayus=True

        else:

            if mayus==False:
                nueva.append(i)
            elif mayus==True:
                nueva.append(i.capitalize())
                mayus=False

    return "".join(nueva)

#Esta funcion suma los numeros de un string, y lo convierte a int el string
def sumar_numero(lista):
    sumatoria=0
    for i in lista:
        sumatoria=sumatoria+int(i)
    return sumatoria

#Esta funcion se encarga de sumar los numeros, hasta que quede solo un numero Ej: 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
def digital_root(n):

    detener=len(str(n))
    solo=str(n)
    
    while detener != 1:
        solo=sumar_numero(str(solo))
        detener=len(str(solo))
        
    return solo

#Esta funcion sacas solo la palabras de 4 digitos de una lista
def friend(x):
    nueva=[]
    for i in x:
        saber=len(i)
        if saber == 4:
            nueva.append(i)
    return nueva

#Esta funcion va a descomponer una palabra y decir cuantas veces se repite, en caso de que se repita
def repetir(palabra):
    nueva=list(palabra.lower())
    palabra2=""

    print(f"La palabra que ingreso es: {palabra}")
    for i in palabra:

        if i not in palabra2:
            palabra2=palabra2.lower()+i
    
    for i in palabra2:
        
        saber_si_es_una=nueva.count(i)
        if saber_si_es_una == 1:
            print(f"La letra {i} se encuentra {nueva.count(i)} vez")
        else:
            print(f"La letra {i} se encuentra {nueva.count(i)} veces")

#Este algortimo, solo imprime si una palabra se repite, e indica cual palabra se repitio
def saber_repetidas(palabra):
    nueva=list(palabra.lower())
    salida=""

    repetida=0

    for i in palabra:
        saber=nueva.count(i)
        if saber>=2:
                 
            if i not in salida:
                repetida=repetida+1
                salida=salida+i

    if salida=="":
        return repetida
    else: 
        return repetida,salida
  
main()