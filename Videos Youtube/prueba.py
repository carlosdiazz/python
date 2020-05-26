lista=[]


def entrar_nombre():
    nombre=input("Ingrese su nombre: ")
    idd=input("Ingrese su id: ")
    sueldo=input("Ingrese su sueldo: ")
    cargo=input("Ingrese su cargo")
    lista.extend([nombre,idd,sueldo,cargo])

def mostrar():
    saber=len(lista)
    

    if saber==0:
        print("La lista no tiene nada")

    else:
        print(saber)


while True:
    op=int(input("ingrese un numero depediendo que deseas hacer: "))

    if op==1:
        entrar_nombre()

    elif op==2:
        mostrar() 
    
    elif op==3:
        break