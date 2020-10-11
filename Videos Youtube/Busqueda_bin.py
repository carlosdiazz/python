
saber=int(input("Escriba hasta que numero deseas contar: "))
i=1

numeros=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
saber= int(input("Ingrese un numero que deseas Buscar: "))
   
def busqueda_bina(numeros,saber):
    izquierda = 0
    derecha = len(numeros)-1

    
    while izquierda<=derecha:
        medio=(izquierda+derecha)//2

        if numeros[medio]==saber:
            return print( "Su numero se encontro en la lista y es el: ",medio,"de la lista ")
            

        elif numeros[medio] > saber:
            derecha=medio-1
            #print(derecha)

        else:
            izquierda=medio+1
            #print(izquierda)
    return ("Su numero no se encuentra")

def busqueda_lineal(numeros,saber):
    for a in numeros:
        if numeros[a]==saber:
            return saber 
    else:
        return  "No lo encontraste"

print(busqueda_lineal(numeros,saber))
    
print(busqueda_bina(numeros,saber))

def ordenar_numeros(lista):
    n = len(lista)

    for i in range(0,n-1):
        k = i
        t = lista[i]
        for j in range(i,n):
            if lista[j] < t:
                k = j
                t = lista[j]
        lista[k] = lista[i]
        lista[i] = t

    return lista