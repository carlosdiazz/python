#Creando una tabla de Multiplicar, Con el ciclo For

numero=int(input("Cual numero quiere multiplicar: "))
for i in range(0,11,1):
    print(numero," * ",i," = ",i*numero )

n=int(input("Eliga un numero: "))
for i in range(11):
    print(f"{n} * {i} = {n * i}")

