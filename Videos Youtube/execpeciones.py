import os,time,math

#VIDEO 23

#Aqui especificamos un error especifico
def cal_raiz(nu):

    if nu<0:
        raise ValueError("El numero no puede ser menor que 0")
    else:
        return math.sqrt(nu)

nu=int(input("Introduce un numero para sacar raiz: "))

try:
    print(cal_raiz(nu))
except ValueError as Error_Numero_Negativo:
    print(Error_Numero_Negativo)


#Aqui decimos que si se cumple algo incorrecto de un error
def eva_edad(edad):
    
    if edad<0:
        raise TypeError("Su edad no puede ser menor que 0")

        
    if edad <20:
        return("Eres joven")
    elif edad<40:
        return("Ya va casi por los 40")
    elif edad<65:
        return("Ya esta maduro")
    elif edad<100:
        return"Cuidate mas"
    else:
        return"Su edad es indefinida"
edad=int(input("Ingrese su edad: "))
print(eva_edad(edad))




#VIDEO 22
#Aqui cualquier error siempre aparecera el mismo mensaje
def divi():

    try:
        op1=(float(input("Introduce un numero: ")))
        op2=(float(input("Introduce un numero: ")))
        print("La division es: ",op1/op2)

    except:
        print("Ocurrio un error inesperado, intente mas tarde")
divi()
time.sleep(4)

def dividi():

    try:
        op1=(float(input("Introduce un numero: ")))
        op2=(float(input("Introduce un numero: ")))
        print("La division es: ",op1/op2)

    except ZeroDivisionError:
        print("no puedes dividir entre cero")
    
    except NameError:
        print("Introdujo simbolos invalidos")

    finally:
        print("Operacion correcta")
dividi()
time.sleep(4)


#VIDEO 21
#aqui tenemos un ejemplo de una division evaluando 2 errores...
def dividir(op1,op2):

    try:
        return op1/op2

    except ZeroDivisionError:
        print("No puedes dividir entre 0")
        return ("Opercion erronea")

while True:
    while True:
        os.system("cls")
        try:
            op1=int(input("Ingrese el numerador: "))
            op2=int(input("Ingrese el denominador: "))
            break
        except ValueError:
            print("Los valores introducidos no son correctos")
            time.sleep(2)
    print(dividir(op1,op2))
    time.sleep(2)
