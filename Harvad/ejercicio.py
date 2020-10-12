from time import sleep
import os

os.system("cls")

def main():
    #mario()
    lista(5)

    #positivo = get_positive()
    #print(positivo)




def get_positive():
    while True:
        n = int(input("Ingrese un numero: "))

        if n>0:
            break
    return n

def mario():
    for i in range(3):
        for j in range(3):
            print("#", end="")
        print()

def lista(n):
    numeros=[]

    for i in range(n):
        a=int(input("Ingrese un numero: "));sleep(1);os.system("cls")
        numeros.append(a)
    print(f"Promedio: {sum(numeros)/len(numeros)}")

main()