import os,time, random
topicos={"1":"DEPORTE","2":"MEDICINA","3":"EDUCACION","4":"TECNOLOGIA"}
datos=[];codigo_acceso=random.randint(100,1000)

def cargando():
    z="."
    for a in range(10):
        print("cargando"+z)
        print("     ",a,"       ")
        z=z+"."
        time.sleep(0.15);os.system("cls")
    
def cerrar_programa():
    for a in range(10+1):
        print("El programa se cerrara en: ",a)
        time.sleep(0.25);os.system("cls")

def mostrar_topicos():
    os.system("cls")
    print("Los topicos disponibles son:")
    print(" 1-  Deporte")
    print(" 2-  Medicina")
    print(" 3-  Educacion")
    print(" 4-  Tecnologia")
    time.sleep(5)

def login():
    contra1="admin";user1="usuario";intentos=1
    cargando()
    confirmar=False
    while True:
        user=str(input("Ingrese su nombre: "))
        contra=str(input("Ingrese su contraseña: "))
        if (user == user1 and contra == contra1):
            cargando()
            print("Ingresaste Correctamente")
            print("Su codigo de Autorizacion es: ",codigo_acceso)
            confirmar=True
            return confirmar

        else:
            if intentos < 3:
                intentos=intentos + 1
                print("Introdujo unos datos incorrecto")
                time.sleep(2);os.system("cls")
            else:
                print("Ya no puedes entrar mas al programa, REINICIE TODO")
                time.sleep(4);os.system("cls")
                return confirmar

def menu():
    print("               Menu Principal      ")
    print("\n     0-Para vizualizar los topicos disponibles.   ")
    print("     1-Para ingresar preguntas a su topico.       ")
    print("     2-Para imprimir todas las preguntas ingresada.   ")
    print("     3-Para imprimir los datos de un topico ingresado.       ")
    print("     4-Si deseas vizualizar este menu de nuevo   ")
    print("     5-Para salir       ")
    print("")

def ingresar_pregtuntas_y_res():
    os.system("cls");seguir="si";conocer_topico=""

    while True:
        topi=str(input("Ingrese a cual topico deseas añadirle preguntas: "))
        topic=topi.upper()

        if topic in topicos.values():
            conocer_topico=topic
            break

        elif topic in topicos.keys():
            conocer_topico=topicos[topi]
            break

        else:
            print("Introdujo un topico que no esta disponible")
            time.sleep(3);os.system("cls")

    while True:

        if seguir=="si":
            time.sleep(3);os.system("cls")
            print("El topico que selecciono es: ",conocer_topico)
            pre=str(input("     Ingrese una pregunta: "));time.sleep(2);os.system("cls")
            Res1=str(input("    Ingrese la respuesta #1: "));time.sleep(2);os.system("cls")
            Res2=str(input("    Ingrese la respuesta #2: "));time.sleep(2);os.system("cls")
            Res3=str(input("    Ingrese la respuesta #3: "));time.sleep(2);os.system("cls")

            datos.append([conocer_topico,pre,Res1,Res2,Res3])
            seguir=str(input("Si deseas añadir otra pregunta a este topico, escriba si: "))
        
        else:
            break

def imprimir_preg():
    saber=len(datos)

    os.system("cls");time.sleep(2)

    if saber==0:
        print("Esta base de datos no tien valores, intente mas tarde")
        time.sleep(2)

    else:
        for q in range(saber):
            print("Del topico: ",datos[q][0]," Su pregunta es: ",datos[q][1])
            print("-"*55)

def imprimir_topic():
    saber=len(datos)
    os.system("cls");time.sleep(2)
    cono=False

    if saber==0:
        print("Esta base de datos no tien valores, intente mas tarde")
        time.sleep(2)

    else:
        conocer=str(input("De cual topico deseas conocer sus datos: "));time.sleep(2)

        if conocer in topicos.values():
            conocer_topico=conocer
            cono=True

        elif conocer in topicos.keys():
            conocer_topico=topicos[conocer]
            cono=True

        if cono==True:
            #print("su topico es",conocer_topico);time.sleep(3)
            print(" Su topico es:           Su pregunta es:      Su respuesta #1 es:     Su Respuesta #2:    Su respuesta #3: ")

            for q in range(saber):
                if datos[q][0] == conocer_topico:
                    print("         ",datos[q][0],"             ",datos[q][1],"                 ",datos[q][2],"         ",datos[q][3],"         ",datos[q][4])

        else:
            print("introdujo un topico que no existe");time.sleep(3)

while True:
    os.system("cls");sab=login()

    if sab ==True:
        codigo_entrar=int(input("Ingrese el codigo de Autorizacion que obtuvo para poder ingresar: "))
    
        if codigo_acceso==codigo_entrar:
            cargando();os.system("cls");menu()
            while True:
                op=int(input("Ingrese un numero depediendo que deseas hacer: "))
                os.system("cls")
                time.sleep(2)

                if op==0:
                    mostrar_topicos()
            
                elif op==1:
                    ingresar_pregtuntas_y_res()

                elif op==2:
                    imprimir_preg()

                elif op==3:
                    imprimir_topic()

                elif op==4:
                    time.sleep(2)
                    menu()
                    time.sleep(5)
            
                elif op==5:
                    cerrar_programa()
                    break

                else:
                    print("introdujo un codigo invalido")
        else:
            print("Introdujo el codigo de verificacion incorrecto")
            break
                
    else:
        
        print("No pudiste entrar al sistema ")
        time.sleep(3);cerrar_programa()
        break