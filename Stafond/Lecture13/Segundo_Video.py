

#Esta es una funcion para sacar numero de un string
def sacar_numeros(lista):

    """
    Para poder hacer la prueba se ejecutra el siguiente comando en la consola

    python -m doctest Segundo_Video.py -v

    >>> sacar_numeros("hola me llamo333 carlos")
    '333'

    """

    nume = ""
    for i in lista:

        if i.isdigit():
            nume=nume+i
    return(nume)

#Funcion para voltear texto
def voltear_letra(letra):
    text=""
    for i in letra:
        text=i+text
    return text

#Funcion 2 para voltear Texto
def voltear_texto(letra):
    return letra[::-1]

def main():
    ok="Mi nombre es Carlos y mi telefono es 829-802-5258"
    x=sacar_numeros(ok)
    print(x)


    ok=voltear_texto("hello!")
    print(ok)

if __name__ == '__main__':
    main()