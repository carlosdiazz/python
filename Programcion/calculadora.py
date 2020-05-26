def suma(nu1,nu2):
    return nu1+nu2

def restar(nu1,nu2):
    return nu1-nu2

def multiplicar(nu1,nu2):
    return nu1*nu2

def dividir(nu1,nu2):
    return nu1/nu2

while True:

    print("Calculadora")
    print(" Presione 1 si deseas sumar, \n Presione 2 si deseas restar, \n Presione 3 si deseas multiplicar \n precione 4 si deseas dividir ")
    op1=int(input("ingrese su primer digito: "))
    op2=int(input("ingrese su segundo digito: "))
    operacion=int(input("Ingrese un numero depediendo que deseas hacer: "))

    if operacion==1:
        print("La suma es: ",suma(op1,op2))

    if operacion==2:
        print("La resta es: ",restar(op1,op2))

    if operacion==3:
        print("La multiplicacion es: ",multiplicar(op1,op2))

    if operacion==4:
        print("La division es: ",dividir(op1,op2))
