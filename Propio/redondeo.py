def sumar():
    cuanto=int(input("Cuantos numeros deseas sumar: "))
    porcentaje=float(input("que porcentaje deseas calcular: "))
    total=0
    suma=0
    for i in range (cuanto):
        nume=int(input(f"Ingrese el #{i+1}: "))
        suma=suma+nume
        nume=round(nume*porcentaje/100)
        total=total+nume

    return (f"El total de la suma es: {suma} el total de comision es: {total}\n")

def total():
    tota=float(input("Ingrese el total de ventas: "))
    porce=float(input("Ingrese el porcentaje a calcular: "))

    return (f"El total que ingreso es: {tota} el porcentaje es: {round(tota*porce/100)}")

print(sumar())

print(total())