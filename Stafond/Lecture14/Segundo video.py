import os
#Funcion para incremetar un año a la edad
def cumplir_ano(diccioanrio,nombre):
    #print("Te esta poniendo mas viejo "+ nombre +"!")
    diccioanrio[nombre]=diccioanrio[nombre]+1


def main():

    edad={
        "Juan":14,
        "Carlos":18,
        "Maria":16,
        "Martha":20,
        "Jose":41,
        "Juana":21,
        "Robert":74,
        "Marcos":12,
        "Joe":13

    }

    #Aqui Creo un diccioanrio
    Mat_20181141={'Nombre':'Carlos','Edad':'19','Sexo':'Masculino'}

    #Aqui Puedo cambiar el valor de una clave
    Mat_20181141['Nombre'] ='Juan'

    #Aqui asigno el valor de una clave en una variable
    nombre=Mat_20181141['Nombre']

    numeros={}

    #Aqui puedo agregar una nueva clave a mi diccionario
    numeros['Carlos '] = '809-573-7774'


    for a in numeros:
        print("\n")
        print("Su nombre es:    "+a+ "     Y su numero es:  "+numeros[a])

    cumplir_ano(edad,"Carlos")


    print("\n\n\n\n\n\n\n")

    #Para obtener el valor de una llave
    print(edad.get("Juan",False))

    for eda in edad.keys():
        print(eda+" y su edad es: "+str(edad[eda]))

    #Para conocer la clave
    print(edad.keys())

    #Para conocer los valores
    print(edad.values())



    #Para elimar la clave y el valor, y obtenemos el valor de la clave
    print(edad.pop('Juan'))

    #Para eliminar un diccionario entro
    #edad.clear()

    #Para obtener la cantidad de claves del diccionario
    print(len(edad))

    #Para borra una clave de un diccioanrio
    del edad["Carlos"]


    print("dd")
    print(edad)




if __name__ == '__main__':
    main()
