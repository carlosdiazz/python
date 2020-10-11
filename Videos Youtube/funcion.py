import os
os.system("cls")

def main():
    
    print(digital_root(493193 ))
    #print(to_camel_case("A-B-C"))
    #print(xo("xooxx"))
    #print(xo("ooxXm"))
    #print(xo("zpzpzpp"))
    #print(xo("zzoo"))
    
    #lista=[1,2,'aasf','1','123',123,14] 
    #print(sacar_numero(lista))
    #numeros_al100()
    #impimir()

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








        



main()