
Num_Meses=12
Num_Semana=7

#Esta funcion es para saber si un ano es Visiestro
def ano_bisiestro(ano):
    #Si es divisible entre 4 y su residuo es 0 y aparte de esto no es divisible entre 100... es visiestro
    #O si es divisible entre 400 y su residuo es 0
    return ((ano%4==0) and (ano % 100 != 0)) or (ano % 400 == 0)

#Esta funcion es para saber la cantidad de dia de un mes
def cant_dia_mes(mes,ano):
    if mes==2:
        if ano_bisiestro(ano):
            return 29
        else:
            return 28
    elif mes==4 or mes==6 or mes ==9 or mes==11:
        return 30
    else:
        return 31

#Con esta funcion vamos a impirmir el Nombre Del mes
def nombre_mes(mes):
    print("Mes #"+str(mes))
    print("Dom Lum Mar Mie Jue Vie Sab")




def main():

    print(100%5)
    #print(ano_bisiestro(2000))
    #print(ano_bisiestro(2020))
    #print(ano_bisiestro(1990))
    #print(ano_bisiestro(1900))
    #print(cant_dia_mes(2,1900))
    #nombre_mes(2)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
