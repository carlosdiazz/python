import time, os, random

curso={"MAT1":"MATEMATICA 1","MAT2":"MATEMATICA 2","SOC":"SOCIOLOGIA","PRO":"PROGRAMACION 1","PRO2":"PROGRAMACION 2"}

datos_estudiantes=[];datos_ins=[]

def cargando():
    z="."
    for a in range(10):
        print("cargando"+z)
        print("     ",a,"       ")
        z=z+"."
        time.sleep(0.15);os.system("cls")

def inicio_2():
    print("-"*65);print("-"*65);print("");print(" "*20,"UNIVERSIDAD CATOLICA DEL CIBAO")
    print(" "*30,"UCATECI");print(" "*27,"PROGRAMACION 1");print(" "*15,"2018-1141"," "*15,"CARLOS JOSE DIAZ");print("");print("-"*65);print("-"*65)

def curso_disp():
    time.sleep(2)
    print("         Cursos Disponibles      ");time.sleep(0.50)
    print("")
    print("     Codigo                  Materia");time.sleep(0.50)
    print("")
    print("     MAT1                      MATEMATICA 1");time.sleep(0.50)
    print("     MAT2                      MATEMATICA 2");time.sleep(0.50)
    print("     SOC                       SOCIOLOGIA");time.sleep(0.50)
    print("     PRO                       PROGRAMACION");time.sleep(0.50)
    print("     PRO2                      PROGRMACION 2");time.sleep(4)
    os.system("cls")            

def menu():
    print("               Menu Principal      ")
    print("\n     0-Para vizualizar el menu.   ")
    print("     1-Registrar datos de estudiantes.       ")
    print("     2-Registrar Inscripiones.   ")
    print("     3-Consultar datos de estudiantes.       ")
    print("     4-Consultar inscritos por curso.   ")
    print("     5-Para vizualizar los cursos disponible.       ")
    print("     6-Para reiniciar el programa.       ")
    print("")

def login():
    contra1="admin";user1="usuario";intentos=1
    cargando()
    confirmar=False
    codigo_acceso=random.randint(100,1000)

    while True:
        user=str(input("Ingrese su usuario: "))
        contra=str(input("Ingrese su contraseña: "))
        if (user == user1 and contra == contra1):
            time.sleep(2)
            cargando()
            print("Ingresaste Correctamente");time.sleep(2)
            print("Su codigo de Autorizacion es: ",codigo_acceso);time.sleep(2)
            while True:
                codigo=int(input("Ingrese su codigo de verificacion: "))
                if codigo_acceso==codigo:
                    print("Entro perfectamente");time.sleep(2)
                    confirmar=True
                    return confirmar
                else:
                    print("Introdujo su codigo de verificacion incorrecto, tendras que reiniciar");time.sleep(2)
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

def cerrar_programa():
    for a in range(10+1):
        print("El programa se cerrara en: ",a)
        time.sleep(0.25);os.system("cls")

def registrar_datos_estu():
    time.sleep(0.50)

    #introucior matricula
    while True:
        saber_matri=len(datos_estudiantes)
        if saber_matri==0:
            while True:
                matricula=int(input("Ingrese su matricula, solo se permiten matricula de 4 digitos: "))
                cantidad_matri=len(str(matricula))
                if cantidad_matri==4:
                    matricula_con_ano="2018-"+str(matricula)
                    print("La matricula que introdujo es: ",matricula_con_ano)
                    time.sleep(2);os.system("cls")
                    break          
                else:
                    time.sleep(1)
                    print("Solo puedes introducir matricula de 4 digitos. ")
                    time.sleep(2);os.system("cls")
            break
        
        else:       
            while True:
                matricula=int(input("Ingrese su matricula, solo se permiten matricula de 4 digitos: "))
                cantidad_matri=len(str(matricula))
                if cantidad_matri==4:
                    matricula_con_ano="2018-"+str(matricula)
                    print("La matricula que introdujo es: ",matricula_con_ano);time.sleep(2);os.system("cls")

                    for a in range(saber_matri):
                        if matricula_con_ano == datos_estudiantes[a][0]:
                            print("Introdujo una matricula repetida, intente de nuevo")
                            time.sleep(3);os.system("cls");break
                    else:
                        break                  
                                     
                else:
                    time.sleep(1)
                    print("Solo puedes introducir matricula de 4 digitos. ")
                    time.sleep(2);os.system("cls")
            break
   
    #introducir nombre
    while True:
        nombre=str(input("Ingrese su nombre: "))
        saber_nombre=len(nombre)
        if saber_nombre>=15:
            print("Su nombre no puede tener mas de 15 caracteres, intente de nuevo")
            time.sleep(2);os.system("cls")
        else:
            print("Su nombre es: ",nombre)
            time.sleep(2);os.system("cls")
            break

    #Introducir Sexo
    while True:
        sexo=str(input("Ingrese su Sexo, recuerde solo se permite F o M: ")).upper()
        saber_sexo=len(sexo)
        
        if saber_sexo==1:
            if sexo=="M":
                print("Su sexo es: ",sexo)
                time.sleep(2);os.system("cls")
                break
            elif sexo=="F":
                print("Su sexo es: ",sexo)
                time.sleep(2);os.system("cls")
                break

            else:
                #print("Su sexo es: ",sexo)
                #time.sleep(2);os.system("cls")
                #break
                print("Introdujo un sexo invalido, intente de nuevo...")
                time.sleep(2);os.system("cls")

        else:
            time.sleep(1)
            print("Solo puedes introducir un digito. ")
            time.sleep(2);os.system("cls")
    
    #Introducir edad
    while True:
        edad=int(input("Introduce su edad: "))

        if edad>0 and edad<100:
            print("La edad que introdujo es: ",edad);time.sleep(2);os.system("cls")
            break
        else:
            print("Introdujo una edad invalidad, intente de nuevo...");time.sleep(2);os.system("cls")

    datos_estudiantes.append([matricula_con_ano,nombre,sexo,edad])

def imprimir_datos():
    saber=len(datos_estudiantes)

    if saber==0:
        print("Aun no hay estudiantes inscito para imprimir...");time.sleep(2);os.system("cls")
    
    else:
        print(" Matricula         Sexo       Edad           Nombre    ")
        print("------------------------------------------------------------------")
        for a in range(saber):
            print(datos_estudiantes[a][0],"         ",datos_estudiantes[a][2],"       ",datos_estudiantes[a][3],"          ",datos_estudiantes[a][1],"     ");time.sleep(1.5)    

def registrar_datos_insc():
    
    saber_lista=len(datos_estudiantes)
    if saber_lista==0:
        time.sleep(1)
        print("Aun no has inscrito ningun estudiante");time.sleep(0.50)
        print("")
        print("Primero inscribe un estudiante, para luego poderlo matricular en un curso");time.sleep(3);os.system("cls")
    
    else:
        terminar=False
        
        #Aqui es para encontrar la matricula
        while True:
            if terminar==False:
                matricula=str(input("Ingrese su matricula con el año: "))
                for a in range (saber_lista):
                    if matricula==datos_estudiantes[a][0]:
                        print("Su matricula fue encontrada")
                        print("")
                        nombre=datos_estudiantes[a][1]
                        edad=datos_estudiantes[a][3]
                        sexo=datos_estudiantes[a][2]
                        print("Su nombre es: ",nombre," Su matricula es: ",datos_estudiantes[a][0]);terminar=True
                        time.sleep(3)
                        break
                else:
                    print("Su matricula no fue enontrada")
                    time.sleep(3);os.system("cls")
            
            elif terminar == True:
                os.system("cls")
                break
                    
        #Aqui es para encontrar el curso
        while True:
            topi=str(input("Ingrese a cual materia deseas matricularse: ")).upper()
            
            if topi in curso.values():
                conocer_materia=topi
                print("La materia que eligio es: ",conocer_materia);time.sleep(2);os.system("cls")
                break

            elif topi in curso.keys():
                conocer_materia=curso[topi]
                print("La materia que eligio es: ",conocer_materia);time.sleep(2);os.system("cls")
                break

            else:
                print("Introdujo una materia que no esta registrada, intente de nuevo")
                time.sleep(3);os.system("cls")
                
        #Aqui es ingresar la fecha        
        while True:
            ano=int(input("Ingrese en que año estas: "))
            if ano>1980 and ano<=2019:
                time.sleep(1)
                ano2=str(ano)
                mes=int(input("Ingrese en que mes estas: "))
                if mes>0 and mes<=12:
                    time.sleep(1)
                    mes2=str(mes)
                    dia=int(input("Ingrese que dia es hoy: "))
                    if dia>0 and dia<=31:
                        time.sleep(1)
                        dia2=str(dia)
                        fecha=ano2+"/"+mes2+"/"+dia2
                        time.sleep(2);os.system("cls")
                        break
                    else:
                        print("Introdujo un dia invalido, intente de nuevo");time.sleep(2);os.system("cls")
                else:
                    print("Introdujo un mes invalido, intente de nuevo");time.sleep(2);os.system("cls")
            else:
                print("Introdujo un año invalido, intente de nuevo");time.sleep(2);os.system("cls")
                
        #monto de inscripcion
        while True:
            monto=int(input("Ingrese cuanto pago de Inscripcion: "))
            if monto>0 and monto<8000:
                print("Su pago de Inscripcion es de: $",monto);time.sleep(3);os.system("cls");break
            else:
                print("Su pago no puede pasar de 8,000, intente de nuevo");time.sleep(2);os.system("cls")

        datos_ins.append([matricula,nombre,sexo,edad,conocer_materia,fecha,monto])

def imprimir_inscri():
    saber=len(datos_ins);entrar=False

    if saber==0:
        print("Aun no hay estudiantes matriculado para imprimir...")
    
    else:
        while True:
            topi=str(input("Ingrese de cual materia deseas conocer sus datos: ")).upper()
            
            if topi in curso.values():
                conocer_materia=topi
                print("La materia que eligio es: ",conocer_materia);time.sleep(2);os.system("cls")
                break

            elif topi in curso.keys():
                conocer_materia=curso[topi]
                print("La materia que eligio es: ",conocer_materia);time.sleep(2);os.system("cls")
                break

            else:
                print("Introdujo una materia que no esta registrada, intente de nuevo")
           
                time.sleep(3);os.system("cls")

        for q in range(saber):
            if conocer_materia==datos_ins[q][4]:
                entrar=True

        if entrar==False:
            print("No hay alumnos matriculado en esta materia...")
        
        elif entrar==True:
            print(" Matricula       Sexo        Edad        Fecha de Inscripcion        Pago de Ins.         Materia                Nombre     ")
            print("----------------------------------------------------------------------------------------------------------------------------")        
            for a in range(saber):
                if conocer_materia==datos_ins[a][4]:
                    print(datos_ins[a][0],"         ",datos_ins[a][2],"         ",datos_ins[a][3],"         ",datos_ins[a][5],"                ",datos_ins[a][6],"         ",datos_ins[a][4],"         ",datos_ins[a][1],"         ",);time.sleep(2)

while True:

    try:
        print
        os.system("cls")
        inicio_2();time.sleep(4)
        os.system("cls");entrar=login()

        if entrar==True:

            cargando();os.system("cls");menu()
            while True:
                op=int(input("Ingrese un numero depediendo que deseas hacer: "))
                os.system("cls")
                time.sleep(0.25)

                if op==0:
                    os.system("cls")
                    menu()
                    time.sleep(4)
            
                elif op==1:
                    registrar_datos_estu()

                elif op==2:
                    registrar_datos_insc()

                elif op==3:
                    imprimir_datos()
                    time.sleep(7);os.system("cls")

                elif op==4:
                    imprimir_inscri()
                    time.sleep(7);os.system("cls")
            
                elif op==5:
                    curso_disp()

                elif op==6:
                    cerrar_programa()
                    break

                else:
                    print("introdujo un codigo invalido")
                
        else:            
            print("No pudiste entrar al sistema ")
            time.sleep(3);cerrar_programa()
            break
    except:
        print("")
        print("         Ha ocurrido un error el programa se reiniciara a continuacion")
        print("                asegure de introducir lo que se le pide")
        time.sleep(5)
        cargando();os.system("cls")