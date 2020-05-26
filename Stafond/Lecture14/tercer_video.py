
def agregar_numeros():

    numbers={}

    while True:
        name=input("Ingrese su nombre: ")

        if name =="":
            break

        else:
            number=int(input("Ingrese su numero: "))
            numbers[name]=number

    return  numbers

def separar_nombres(numbers):

    for name in numbers:

        print(name,"->",numbers[name])


def main():
    numero=(agregar_numeros())
    separar_nombres(numero)




if __name__ == '__main__':
    main()
