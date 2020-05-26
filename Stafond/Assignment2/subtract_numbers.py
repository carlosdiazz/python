
def main():

    pares=0
    sumatorio=0
    for i in range(100):
        pares=pares+2
        sumatorio=pares+sumatorio
        if pares==100:
            break
    print("La sumatoria de los numeros pares del 0 al 100 es: ",sumatorio)

    sumatorio=0
    for i in range(0,101,2):
        sumatorio=sumatorio+i
    print("La sumaotria de los nuemros pares del 0 al 100 es: ",sumatorio)

    a = float(input("Ingrese su primer Numero: "))
    b = float(input("Ingrese su Segundo Numero: "))

    print("La Resta sera igual a: ",a-b)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
