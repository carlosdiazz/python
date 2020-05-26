import os; import time
codigo=[];nombres=[];cargo=[];sueldos=[]
os.system("cls")
 
def inicio():
    print("*"*70);print("*"*70);print("*"*5," "*56,"*"*7);print("*"*5," "*10,"Digite 1 para ingresar un Empleado"," "*10,"*"*7)
    print("*"*5," "*10,"Digite 2 para imprimir todas las listas"," "*5,"*"*7);print("*"*5," "*6,"Digite 3 para buscar los datos de un empleado"," "*3,"*"*7);print("*"*5," "*3,"Digite 4 para calcular los descunetos de un empleado","*"*7)
    print("*"*5," "*56,"*"*7);print("*"*70); print("*"*70)

while True:
    time.sleep(5)
    os.system("cls")
    inicio()
    time.sleep(21)
    os.system("cls")
    op=int(input("\nIngrese un numero depediendo que deseas hacer: "))
    
    if op == 1:
        codi=str(input("\nIngrese su codigo: "))
        nom=str(input("\nIngrese su nombre: "))
        car=str(input("\nIngrese su cargo: "))
        suel=int(input("\nIngrese su sueldo: "))
        
        codigo.extend([codi]); nombres.extend([nom]);cargo.extend([car]);sueldos.extend([suel])

    
    elif op == 2:
        print("\nTodos los codigos almacenados son: ",codigo)
        print("\nTodos los Nombres almacenados son: ",nombres)
        print("\nTodos los Cargos almacenados son: ",cargo)
        print("\nTodos los Sueldos almacenados son: ",sueldos)

    
    elif op ==3:
        buscar_car=str(input("\nDe que cargo deseas conocer sus datos: "))
        
        if buscar_car in cargo:
            saber_nom=cargo.index(buscar_car)
            saber_suel=cargo.index(buscar_car)
            saber_codi=cargo.index(buscar_car)
            print("\nEl nombre de quien trabaja de: ",buscar_car, " es: ", nombres[saber_nom])
            print("\nEl sueldo de quien trabaja de: ",buscar_car, " es: ", sueldos[saber_suel])
            print("\nEl Codigo de quien trabaja de: ",buscar_car, " es: ", codigo[saber_codi])
        else:
            print("\nIntrodujo un cargo que no existe")

    elif op == 4:
        descuentos=str(input("\nIngrese el nombre de quien deseas conocer sus descuentos: "))

        if descuentos in nombres:
            posicion_sueldo=nombres.index(descuentos)
            sueldo_empleado=sueldos[posicion_sueldo]
            print("\nSu sueldo sin aplicar los descuentos es: ",sueldo_empleado)


            isr2=(sueldo_empleado*0.028)
            isr=(sueldo_empleado-sueldo_empleado*0.028)
            print("\nAplicando el descuento de Inversion Sobre la Renta, su sueldo es de: ",isr)

            afp2=(sueldo_empleado*0.023)
            afp=((sueldo_empleado-sueldo_empleado*0.023))
            print("\nAplicando el descuento de  A... F... P..., su sueldo es: ",afp)

            sg2=(sueldo_empleado*0.024)
            sg=((sueldo_empleado-sueldo_empleado*0.024))
            print("\nAplicando el descuento de  Seguro Social, su sueldo es: ",sg)

            total_desuentos=(isr2+afp2+sg2)
            total_desuentos2=(sueldo_empleado-total_desuentos)
            print("\nSu sueldo incluyendo todos los descuentos seria: ", total_desuentos2)

        else:
            print("\nIntrodujo un nombre que no esta registrado, intente de nuevo...")
    else:
        print("\nIntrodujo un numero invalido")
