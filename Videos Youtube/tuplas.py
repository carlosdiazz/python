tupla=("Carlos","jose",14,2000,13,13,13)

#Aqui imprimimos el valor que se encuentra en el indice 1
print(tupla[1])

#Aqui convertimos la tupla en lista
lista=list(tupla)
print(lista)

#Aqui convertimos una lista en un tupla
tupla2=tuple(lista)
print(tupla2)

#Aqui nos dira si un valor esta en una tupla
print ("Carlos" in tupla2)

#Aqui sabremos cuantas veces se repite un valor en una tupla
print(tupla2.count(13))

#Aqui sabremos cuantos elementos hay en una lista
print(len(tupla2))

#Aqui ene sta dupla podemos nombrar el valor de varias variables
tupla3=("Carlos",14,8,2000)
nombre,dia,mes,año=tupla3
print(nombre)
print(dia)