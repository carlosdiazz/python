#Video 13

def asig():
    print("Asignaturas optativas: Informatica - Audio - Pintor")
    OPmateria=str(input("Introduce que materias deseas: "))
    materia=OPmateria.upper()


    if materia in ("INFORMATICA","AUDIO","PINTOR"):
        print("Asigantura elegida: ",materia,"----- Has selecioando corretamente")
    else:
        print("No elegiste una materia valida")
asig()

def becas():
    distancia=int(input("Introduce a que distancia vives de la Universidad: "))
    herman=int(input("Introduce cuantos hermanos tienes: "))
    sala=int(input("Introduce su salario anual: "))

    if (distancia > 40)and(herman>2)or(sala<10000):
        print("Usted aplica para una beca")

    else:
        print("Usted no aplica para una beca")
becas()

#Video 12
def salario():
    salario_pre=int(input("Ingrese el salario del Presidente: "))
    salario_dire=int(input("Ingrese el salario del Director: "))
    salario_jefe=int(input("Ingrese el salario del Jefe: "))
    salario_adm=int(input("Ingrese el salario del adm: "))

    if salario_adm<salario_jefe<salario_dire<salario_pre:
        print("Todo va bien")
    elif salario_adm<salario_jefe<salario_pre<salario_dire:
        print("El director gana mas que el presidente")
    elif salario_adm<salario_pre<salario_dire<salario_jefe:
        print("El jefe esta ganando mas que el director")
    elif salario_pre<salario_jefe<salario_dire<salario_adm:
        print("El administrativo esta ganando mas que el presidente")
    else:
        print("Hay un error en la distribucion de dinero")
salario()

def edad(edadd):
    
    if 0<edadd<100:
        print("Su edad es correcta")
    else:
        print("Su edad es incorrecta")
edad_n=int(input("Introduzca su edad: "))
edad(edad_n)

#Ejercicios video 11
def media():
    nu1=int(input("Introduzca un numero: "))
    nu2=int(input("Introduzca un numero: "))
    nu3=int(input("Introduzca un numero: "))
    resultado= (nu1+nu2+nu3)/3
    print("Su media arimetica de los numeros introducido es: ",resultado)
media()

def mayor():
    nume1=int(input("Introduce un numero:"))
    nume2= int(input("Introduce otro numero:"))
    lista=[nume1,nume2]
    print ("El numero mayor es: ",(max(lista)))
mayor()

def datos():
    nombre=str(input("Introduce su nombre: "))
    direccion=str(input("Introduce su direccion: "))
    telefono=str(input("Introduce su telefono: "))
    lista=[nombre,direccion,telefono]
    print("Su nombre es: ",lista[0], "\nSu direccion es: ", lista[1], "\nSu telefono es: ",lista[2])
datos()

#Video 10 y 11
def nota2(cali2):
    if cali2 <= 5:
        print("Reprobado")
    elif cali2 == 6:
        print("Insuficiente")
    elif cali2 == 7:
        print("Notable")
    elif cali2== 8:
        print("Bien")
    elif cali2 ==9:
        print("Exelente")
    elif cali2 == 10:
        print("Sacaste la mayor nota posible")
    else:
        print("Introdujo una nota invalida")

def aceder(edad):
    if edad >= 18 and edad <= 110:
        print("Puedes pasar eres mayor")
    elif edad >111:
        print("Introdujo una edad invalida")
    else:
        print("No puedes pasar eres menor de edad")
    
def nota(cali):
    resultado=("Aprobado")
    if cali < 5:
        resultado=("Reprobado")
    return resultado

cali2=float(input("Introduce su nota: "))
print (nota2(cali2))

edad=int(input("Introduzca su edad: "))
print(aceder(edad))

cali=float(input("Introduce su nota: "))
print (nota(cali))