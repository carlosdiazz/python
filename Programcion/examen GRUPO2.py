topic={"1":"DEPORTE","2":"CULTURA GENERAL","3":"POLITICA","4":"MEDICINA"}
contra= "admin";user="usuario"
lista_preguntas=[];lista_con_opciones=[]
def inicio():
    print("*"*75);print("*"*75);print("*"*5," "*61,"*"*7)

    print("*"*5," "*9,"Digite 1 para ingresar una pregunta"," "*15,"*"*7)
    print("*"*5," "*3,"Digite 2 para ingresar las respuesta a su pregunta"," "*6,"*"*7)
    print("*"*5,"Digite 3 para imprimir todas las preguntas con su topico"," "*4,"*"*7)
    print("*"*5,"Digite 4 para imprimir las pregunta de un topico especifico  ","*"*7)
    print("*"*5," "*8,"Digite 5 si deseas visualizar el menu de nuevo"," "*5,"*"*7)
    print("*"*5," "*6,"Digite 6 para salir"," "*34,"*"*7)

    print("*"*5," "*61,"*"*7);print("*"*75);print("*"*75)

def registrar_preguntas():
    saber=0
    while True:
        
        if saber ==0:

            topi=str(input("Ingrese a cual topico deseas introducir una pregunta: "))
            print("\n"*5)
            if topi in topic.keys():
                saber=1
                print("Usted eligio el codigo de topico: ",topi,"Que equivale al topico: ",topic[topi])
                nombre_topico=topic[topi]

            elif topi in topic.values():
                print("Usted eligio el topico: ",topi)
                saber=1
                nombre_topico = topi
            else:
                print("Usted ingreso un topico que no existe ")

        elif saber==1:
            codigo_pre=str(input("Ingrese el codigo de su pregunta: "))
            preguntas=str(input("Ingrese una pregunta de acuerdo a su topico: "))
            lista_preguntas.append([nombre_topico,codigo_pre,preguntas])
            break

def registrar_respuestas():
    cuantos=len(lista_preguntas)
    sabe=0

    if cuantos==0:
        print("su lista de preguntas, no tienes preguntas aun")
        
    else:
        while True:
            if sabe==0:
                codigo=str(input("Ingrese el codigo de su pregunta, al que deseas agregar respuesta: "))

                for q in range(cuantos):
                    for t in (lista_preguntas[q]):
                        if codigo == t:
                            sabe=1

            elif sabe==1:

                codigo_opc=str(input("Ingrese el codigo de su respuestas: "))
                opcio1=str(input("ingrese opcion        #1: "))
                opcio2=str(input("ingrese opcion        #2: "))
                opcio3=str(input("ingrese opcion        #3: "))

                for p in range(cuantos):
                    for y in lista_preguntas[p]:
                        if y == codigo:
                            nombre_top=lista_preguntas[p][0]
                            codigo_pre=lista_preguntas[p][1]
                            pregunt=lista_preguntas[p][2]
                            lista_con_opciones.append([nombre_top,codigo_pre,pregunt,codigo_opc,opcio1,opcio2,opcio3])
                break
  
def mostrar_preguntas():
    saber= len(lista_preguntas)

    if saber==0:
        print("Esta lista no tiene datos")

    else:
        for q in range(saber):
            print("Del topico: ",(lista_preguntas[q][0])," Su pregunta es: ",(lista_preguntas[q][2]))     

def preguntas_topicos():
    saberr= len(lista_con_opciones)

    if saberr==0:
        print("Aun no ha registrado datos")

    else:
        saber=0
        while True:
            if saber ==0:
                
                topi=str(input("Ingrese de cual topi deseas conocer sus datos: "))

                if topi in topic.keys():
                    saber=1
                    print("Usted eligio el codigo de topico: ",topi,"Que equivale al topico: ",topic[topi])

                elif topi in topic.values():
                    print("Usted eligio el topico: ",topi)
                    saber=1
                else:
                    print("Usted ingreso un topico que no existe ")

            elif saber==1:

                print("\nSu topico se encuentra en el diccionario")
                print(" Su topico es:        ","Su Codigo de pregunta es:  ","     Su pregunta es:     ","      Su opcion 1 es:    ","      Su opcion 2 es:    ","      Su opcion 3 es:    ")
                for q in range(saberr):
                    if lista_con_opciones[q][0]==topi:
                            print("")                       
                            print("")
                            print("  ",lista_con_opciones[q][0]," "*20,lista_con_opciones[q][1]," "*20, lista_con_opciones[q][2]," "*10,lista_con_opciones[q][4]," "*15,lista_con_opciones[q][5]," "*15,lista_con_opciones[q][6])
                break

def cargando():
    for a in range(10):
        print("Cargando el programa va por ",a+1)
        print("\n"*5)

def cerrar_programa():
      
    print("El programa se cerrara a continuacion")

def mostrar_topicos():
    print("\n 1 - DEPORTE")
    print("\n 2 - CULTURA GENERAL")
    print("\n 3 - POLITICA")
    print("\n 4 - MEDICINA")

def login(intentos=1):  

    use=str(input("Escriba su user: "))
    cont=str(input("Escriba su contrsena : "))

    if (cont!=contra or use!=user):
        if intentos < 3:
            intentos = intentos + 1
            print("Datos erroneos, intentalo otra vez")

            login(intentos)
        else:
            print("Ya  no puedes entrar mas reinicia el programa...")
            
    else:
        inicio()
        while True:

            op=int(input("Ingrese un numero depediendo que deseas hacer: "))
            print("\n"*5)

            if op== 1:
                mostrar_topicos()
                registrar_preguntas()
                print("\n"*5)


            elif op ==2:
                print("\n"*5)
                registrar_respuestas()
                print("\n"*5)


            elif op==3:
                print("\n"*5)
                mostrar_preguntas()
                print("\n"*5)

            elif op==4:
                print("\n"*5)
                preguntas_topicos()
                print("\n"*5)

            elif op==5:

                inicio()

            elif op==6:
                cerrar_programa()
                break

def inicio_2():
    print("-"*65);print("-"*65);print("");print(" "*20,"UNIVERSIDAD CATOLICA DEL CIBAO")
    print(" "*30,"UCATECI");print(" "*27,"PROGRAMACION 1");print(" "*15,"2018-1141"," "*15,"CARLOS JOSE DIAZ");print("");print("-"*65);print("-"*65)

while True:
    try:
        inicio_2()
        hazlo=str(input("presione una tecla para continuar: "))
        cargando()
        login()
        break
    except:
        print("Ha ocurrido un eror, intente de nuevo, desde el comienzo...")