import os; import time
lista=[]

def inscribir():

    empleado=str(input("Ingrese el nombre del Empleado: "))
    sueldo=int(input("Ingrese el sueldo del Empleado anterior: "))

    lista.append([sueldo,empleado])

def sueldo_mas_alto():
    saber=len(lista)
    if saber== 0:
        print("La lista esta en blanco")
    else:
        alto=max(lista)
        print("Su nombre es: ",alto[1],"Su sueldo es: ",alto[0])

def mayor_a_menor():
    saber=len(lista)
    if saber== 0:
        print("La lista esta en blanco")
    else:
        lista.sort(reverse=True)
        for a in range (saber):
            print("Su nombre es: ",lista[a][1]," y su sueldo es de: ",lista[a][0])
    
def aumentar_sueldos():
    saber=len(lista)
    if saber== 0:
        print("La lista esta en blanco")
    else:
        subir=int(input("Que porcentaje deseas subirle a sus empleado: "))
        
        for a in range (saber):
            lista[a][0]=(lista[a][0]+(lista[a][0]*subir/100))

def aumentar_sueldo_espe():
    saber=len(lista)
    ok=False
    if saber== 0:
        print("La lista esta en blanco")
        
    else:
        emple=str(input("Ingrese el nombre del empleado: "))

        for a in range(saber):
            for q in (lista[a]):
                if q == (emple):
                    if lista[a][1]==(emple):
                        ok=True
                        aumentar=int(input("Cuantos quieres aumentarle, el aumento se hara porcentaje en base a su sueldo: "))
                        lista[a][0]=(lista[a][0]+(lista[a][0]*aumentar/100))

        if ok == False:
            print("Su empleado no esta en la lista")

def eliminar_empleado():
    saber=len(lista)
    ok=False
    if saber== 0:
        print("La lista esta en blanco")
        
    else:
        emple=str(input("Ingrese el nombre del empleado que deseas eliminar: "))

        for a in range(saber):
            for q in (lista[a]):
                if q == (emple):
                    if lista[a][1]==(emple):
                        ok=True
                        elimar=a
        del(lista[elimar])

        if ok == False:
            print("Su empleado no esta en la lista")

def eliminar_todo():
    saber=len(lista)
    if saber== 0:
        print("La lista esta en blanco")
        
    else:
        time.sleep(1);os.system("cls")       
        print("Borrando lista Completa en 5")
        time.sleep(1);os.system("cls")       
        print("Borrando lista Completa en 4")
        time.sleep(1);os.system("cls")       
        print("Borrando lista Completa en 3")
        time.sleep(1);os.system("cls")       
        print("Borrando lista Completa en 2")
        time.sleep(1);os.system("cls")       
        print("Borrando lista Completa en 1")
        lista.clear()
        time.sleep(1);os.system("cls") 
        print("La lista fue borrada exitosamente")

def cerrar_programa():
    time.sleep(1);os.system("cls")       
    print("El programa se cerrara en 5")
    time.sleep(1);os.system("cls")
    print("El programa se cerrara en 4")
    time.sleep(1);os.system("cls")
    print("El programa se cerrara en 3")
    time.sleep(1);os.system("cls")
    print("El programa se cerrara en 2")
    time.sleep(1);os.system("cls")
    print("El programa se cerrara en 1")
    time.sleep(1);os.system("cls")
    
def inicio():
    print("*"*70);print("*"*70);print("*"*5," "*56,"*"*7)

    print("*"*5," "*10,"Digite 1 para ingresar un Empleado"," "*10,"*"*7)
    print("*"*5," "*10,"Digite 2 para imprimir lista con empleado"," "*3,"*"*7)
    print("*"*5," "*6,"Digite 3 para imprimir sueldo mas alto"," "*10,"*"*7)
    print("*"*5," "*1,"Digite 4 para imprimir del sueldo mas alto a el menor ","*"*7)
    print("*"*5," "*8,"Digite 5 para aumentar todos los sueldos"," "*6,"*"*7)
    print("*"*5," "*6,"Digite 6 para aumentar un sueldo en especifico"," "*2,"*"*7)
    print("*"*5," "*2,"Digite 7 para eliminar un sueldo en especifico "," "*5,"*"*7)
    print("*"*5," "*16,"Digite 8 para borrar toda la lista"," "*4,"*"*7)
    print("*"*5," "*16,"Digite 9 para salir"," "*19,"*"*7)

    print("*"*5," "*56,"*"*7);print("*"*70); print("*"*70)

def cargando():
    print("Cargando")
    time.sleep(0.20);os.system("cls")
    print("Cargando.")
    time.sleep(0.20);os.system("cls")
    print("Cargando..")
    time.sleep(0.20);os.system("cls")
    print("Cargando...")
    time.sleep(0.20);os.system("cls")
    print("Cargando....")
    time.sleep(0.20);os.system("cls")
    print("Cargando.....")
    time.sleep(0.20);os.system("cls")    

def imprimir_lista():
    print(lista)
    saber=len(lista)
    if saber==0:
        print("Esta lista aun no tiene valores")
    else:
        print("Aqui estan todos los valores de la lista: ")
        for a in range (saber):
            print("\nSu nombre es: ",lista[a][1],"\nSu sueldo es: ",lista[a][0])
            time.sleep(0.50)

while True:
    try:
        time.sleep(4);cargando();os.system("cls");inicio()

        op=int(input("Digite un numero depediendo que deseas hacer: "))

        if op == 1:
            inscribir()
        
        elif op == 2:
            imprimir_lista()
        
        elif op == 3:
            sueldo_mas_alto()
        
        elif op == 4:
            mayor_a_menor()

        elif op == 5:
            aumentar_sueldos()
        
        elif op == 6:
            aumentar_sueldo_espe()

        elif op == 7:
            eliminar_empleado()
        
        elif op == 8:
            eliminar_todo()

        elif op == 9:
            cerrar_programa()
            break
        else:
            print("......")
            print("\nIntrodujo una letra invalida\n")
            print("......")
       
    except:
        print("Ha ocurrido un error, intente de nuevo, \nVerifique que introdujo correctamente lo que se le pide")
