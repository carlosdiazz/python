

#Esto es una funcion para sumarle a todos los numeros de la lista un numero comun
def agregar_num(lista,numero):
    for i in range (len(lista)):
        lista[i]=lista[i]+numero

    return lista

def main():

    lista=[5,6,7,8,9]
    print(lista)
    agregar_num(lista,10)
    print(lista)


if __name__ == '__main__':
    main()
