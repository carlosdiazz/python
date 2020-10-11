import os
os.system("cls")

def main():
    
    
    print(xo("232dsfx"))
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
    
    

main()