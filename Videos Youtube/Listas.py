lista=["Carlos","Jose","Marcos","Jesus",57]
listan=[1,2,9,7,6,5]
#Esta es una forma para unir 2 lista, creando otra lista 
lista2=[1,2,3]*3
lista3=lista+lista2
print(lista3[:])

#Aqui eliminamos el ultimo valor de una lista
lista.pop()

#Aqui eliminamos un valor especifico de una lista
lista.remove("Marcos")

#Aqui sabemos si un elemento o valor especifico, se encuentra en una lista
print("Carlos" in lista)

#Aqui sabemos en que indice se encuentra el valor que deseamos buscar
print(lista.index("Jose"))

#Aqui agregamos varios valores a la lista
lista.extend([True,5,"Adrian"])

#Aqui con esta funcion en el indice puesto me agregara un nombre
lista.insert(1,"Diaz")

#Aqui con esta funcion al final de la lista me agregara este nombre
lista.append("Mateo")

#Aqui ordenaer la lista
listan.sort()

ordenar=[[50,"pan"],[80,"queso"],[74,"batata"]]

#Aqui imprime la lsita sin ordenar
print("original",(ordenar))

#Aqui imprime la lista ordeanda
ordenar.sort()
print("ordenada",(ordenar))

#Aqui impirme la lista completa
print (lista[:])

#Aqui imprime los valores desde el indice seleccionado hasta el final
print (lista[2:])

#Aqui imprime del indice 0 al 1
print (lista[0:3])

#Aqui solo imprime el valor del indice 3
print (lista[3])

#Si el índice es negativo, cuenta desde el último elemento.
print (lista[-1])

print(listan)

#Aqui agreagmos una lsita dentro de otra lista y luegos la podemosordenar con su valor
listae=[]
for r in range(3):
    precio=int(input("Ingrese su valor: "))
    hey=input("Ingrese un Nombre: ")
    lista2=[precio,hey]
    listae.extend([lista2])

print(listae)