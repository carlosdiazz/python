lista=[];import os,time
#print("")
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

def inicio():
    print("*"*70);print("*"*70);print("*"*5," "*56,"*"*7);print("*"*5," "*10,"Digite 1 para ingresar un Empleado"," "*10,"*"*7)
    print("*"*5," "*10,"Digite 2 para imprimir todas las listas"," "*5,"*"*7);print("*"*5," "*6,"Digite 3 para buscar los datos de un empleado"," "*3,"*"*7);print("*"*5," "*3,"Digite 4 para calcular los descuentos de un empleado","*"*7)
    print("*"*5," "*8,"Digite 6 si deseas limpiar la lista"," "*11,"*"*7);print("*"*5," "*16,"Digite 7 si deseas salir"," "*14,"*"*7)
    print("*"*5," "*56,"*"*7);print("*"*70); print("*"*70)

def inscribir():
    incentivo=True

    codigo=str(input("\nIngrese su codigo de empleado: "))

    nombre=str(input("\nIngrese un nombre: "))

    cargo=str(input("\nIngrese su cargo: "))

    sueldo=int(input("\nIngrese su sueldo: "))

    ince=int(input("\nIngrese 1 si aplica para incetivos: "))

    if ince == (1):
        ince=incentivo
    else:
        incetivo=False
        ince=incetivo

    lista.extend([codigo]);lista.extend([nombre]);lista.extend([cargo]);lista.extend([sueldo]);lista.extend([ince])
    
def buscar_empleado():

    buscar=str(input("Ingrese el codigo del empleado que deseas buscar: "))

    if buscar in lista:
        
        codigo=lista.index(buscar);nombre=codigo+1;cargo=nombre+1;sueldo=cargo+1

        print("\n Su codigo es: ",buscar)
        print("\n Su nombre es: ",(lista[nombre]))
        print("\n Su cargo es: ",(lista[cargo]))
        print("\n Su sueldo es: ",(lista[sueldo]))

    else:
        print("Introdujo un codigo invalido, intente mas tarde")

def emple_cargo():
    cargo=str(input("Ingrese de que cargo deseas conocer sus empleados: "))

    if cargo in lista:
        cargo2=lista.index(cargo)
        cargo3=cargo2-1
        print("Su cargo es: ",cargo)
        print("Su nombre es: ",(lista[cargo3]))

    else:
        print("Introdujo un cargo invalido, intente mas tarde...")
  
def descuentos2():
    codigo=str(input("\nIngrese el codigo de quien deseas saber sus descuentos: "))

    if codigo in lista:

        codigo_lista=lista.index(codigo)
        dinero=codigo_lista+3
        dinero=int(lista[dinero])
        incentivos=codigo_lista+4
        isr=0;afp=0;seg=0;total_des=0;sueldo_con_des=0;total_incetivos=0;sueldo_final=0
        idd=codigo_lista;idd=str(lista[idd]);nombre=codigo_lista+1;nombre=str(lista[nombre]);cargo=codigo_lista+2;cargo=str(lista[cargo])

        if ((dinero >=20000) and (dinero <=30000)):        
            isr=(dinero*0.023);afp=(dinero*0.012);seg=(dinero*0.0314)         
            total_des=(isr+afp+seg)
            sueldo_con_des=dinero-total_des

        elif (dinero<=19999):
            total_des=0
            sueldo_con_des=dinero

        elif ((dinero>=30001) and (dinero <= 40000)):
            isr=(dinero*0.025);afp=(dinero*0.016);seg=(dinero*0.0318)
            total_des=(isr+afp+seg)
            sueldo_con_des=dinero-total_des

        elif (dinero>=40001):
            isr=(dinero*0.029);afp=(dinero*0.020);seg=(dinero*0.035)
            total_des=(isr+afp+seg)
            sueldo_con_des=dinero-total_des

        if (lista[incentivos]) == True:
            calidad=(sueldo_con_des*0.04)
            puntualidad=(sueldo_con_des*0.03)
            total_incetivos=calidad+puntualidad

        elif (lista[incentivos]) == False:
            calidad=0
            puntualidad=0
        
        sueldo_final=dinero-total_des+total_incetivos
        
        os.system("cls")
        print("="*170);print("="*170);print("");print("")
        print(" ID  "," "*2,"Nombre"," "*2,"Cargo"," "*2,"Sueldo Bruto"," "*2,"Imp. De Renta"," "*2," AFP "," "*2,"Seg. Social"," "*2,"Total de Desc."," "*2,"Inc.de calidad"," "*2,"Inc. de Puntualidad"," "*2,"Total de Inc"," "*2,"Sueldo Neto")
        print("")
        print(idd," "*2,nombre," "*2,cargo," "*4,round(dinero)," "*10,round(isr)," "*8,round(afp)," "*6,round(seg)," "*8,round(total_des)," "*13,round(calidad)," "*12,round(puntualidad)," "*13,round(total_incetivos)," "*9,sueldo_final)
        print("");print("");print("="*170);print("="*170)
        time.sleep(15)
    else:
        print("El codigo que introdujo no aparece en la Base de Datos")

while True:
    
    time.sleep(4);cargando();os.system("cls");inicio()

    op=int(input("\nIngrese un numero depediendo que deseas hacer: "))

    if op == 1:
        inscribir()

    elif op == 2:
        saber=len(lista)
        if saber==0:
            print("Esta lista aun no tiene valores")
        else:
            print("Aqui estan todos los valores de la lista: ")
            for t in lista:
                print (" -",t)

    elif op == 3:
        buscar_empleado()

    elif op == 4:
        descuentos2()

    elif op==5:
        emple_cargo()

    elif op == 7:
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
        break

    elif op == 6:
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

    else:
        print("......")
        print("\nIntrodujo una letra invalida\n")
        print("......")