


def main():
    hola="hola como estas"
    num3="2"

    #Para separar un texto por espacio
    x=hola.split(" ")
    print(x)

    #Para poner un texto en mayuscula
    print(hola.upper())

    #Para poner un texto en minuscula
    print(hola.lower())

    #Para reemplazar
    print(hola.replace("hola","Hi"))

    #Para buscar una letra y saber su posicion
    print(hola.find("h"))

    #Para quitar espacio al comeinzo y a final
    print(hola.strip())

    #para saber si comienza con una letra especifica
    print(hola.startswith("hol"))

    #Para saber si termina de una manera
    print(hola.endswith("fin"))

    #Para saber si es un digito la varianle
    print(num3.isdigit())

    







if __name__ == '__main__':
    main()