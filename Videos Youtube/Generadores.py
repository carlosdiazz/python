#Video 20
def de_ciud(*ciud):
    for ele in ciud:
        yield from ele

ciud_de=de_ciud("Hola","Como","Estas")
print(next(ciud_de))



def devu_ciudades(*ciudades):
    for elementos in ciudades:
        yield elementos

ciudade_devuel=devu_ciudades('LA VEGA',"Santiago","MOCA","Santo Domingo")

print(next(ciudade_devuel))

#Video 19
def pares3():

    for we in range(0,10,2):
        yield we

ok=pares3()
print("prueba con for")
print(next(ok))



#Sacar los numeros pares con Generadores
def pares2():
    num=1

    while num<10:
        yield num*2
        num=num+1

print("Otra prueba")
listo=pares2()
print(next(listo))
print("otro")
print(next(listo))

print("Aqui impirmie con for")
for i in listo:
    print(i)



#Sacar lso numeros pares con una funcion normal primero

def pares():
    lista=[]
    for i in range(0,10,2):
        lista.extend([i])
    return lista

print(pares())