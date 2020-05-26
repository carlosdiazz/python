def main():

    lista=["hola","como","esta","Carlos"]
    lista2=[1,2,3,4,0,99,324,23423,435]

    #Eliminar el Ultimo elemento de la lista
    lista.pop()

    #Aregar un unico elmento a la lista
    lista.append("hey")


    #Eliminar de la lista en un lugar especifico
    lista.pop(1)


    #Eliminar un valor especifico dentro de la lista
    lista.remove("hola")

    #Conocer si un valor esta en una lista y luego elimianrlo sin errores
    if "holda" in lista:
        lista.remove("hdola")

    #Agregar una lista en una lista o agregar varios elementos
    lista.extend(lista2)

    #Aqui unimos varias listas
    lista3= lista+lista2+lista


    #Conocer el inidice de un elemento
    print(lista.index("hey"))

    #Aqui insertamos un valor en un indice especifico
    lista.insert(1,"hola")

    #Aqui creamos una copia de la lista
    lista4=lista.copy()

    #Conocer el valor Maximo de la lista
    print(max(lista2))

    #Conocer el valor minimo de la lista
    print(min(lista2))

    #Concoer la sumatoria toal de una lsita
    print(sum(lista2))

    print(lista)



if __name__ == '__main__':
    main()
