import os, random

# 1. Haga un programa en el cual se digiten la temperatura para cada hora del día. Imprima por pantalla la temperatura promedio para ese día, la temperatura mayor y menor informando la hora a la cual ocurrieron.
def ejercicio_1():
    temperatura=[]
    for i in range(0,25,1):
        if i==0:
            hora=int(input(f"Introduzca la temperatura en Celcius, para las: 12:00:00 horas: "))
            temperatura.append(hora)
        else:

            hora=int(input(f"Introduzca la temperatura en Celcius, para las: {i}:00:00 horas: "))
            temperatura.append(hora)
    os.system("cls")
    mayor=max(temperatura)
    print(f"La temperatura Mayor ingresada es: {mayor} °C y fue a las {(temperatura.index(mayor))}:00:00 ")

    menor=min(temperatura)
    print(f"La temperatura Menor ingresada es: {menor} °C y fue a las {(temperatura.index(menor))}:00:00 ")

    promedio=sum(temperatura)/len(temperatura)
    print(f"La temperatura promedio es: {promedio} °C")


# 2. En un programa se declara un arreglo de 50 elementos de tipo enteros y se inicializa con valores aleatorios entre 0 y 300. Con dicho arreglo, crear funciones para cada operación, haga lo siguiente:

#       Imprima por pantalla el menor y el mayor valor del arreglo.
#       Calcule el promedio, desviación estándar, moda y mediana de los valores.
#       Identifique los grupos de 3 que sean números adyacentes (27, 28 y 29 es un grupo de adyacentes)


def moda(lista):
    dicc={}
    for i in lista:
        if i in not dicc:




def ejercicio_2():
    arreglo=[]
    for i in range(50):
        arreglo.append(random.randint(0,300))
    
    print(arreglo)

    print(f"El numero mayor es {max(arreglo)}.")
    print(f"El numero menor es {min(arreglo)}.")
    print(f"El promedio de los numeros es: {sum(arreglo)/50}")

    #Quede en la moda
    print(f"{moda(arreglo)}")

    

def main():
    
    #ejercicio_1()
    ejercicio_2()


if __name__ == '__main__':
    os.system("cls")
    main()
