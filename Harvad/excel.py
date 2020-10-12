import csv

file = open("texto.csv", "a")

nombre=input("Ingrese su nombre: ")
numero=input("Ingrese su numero: ")

escribir=csv.writer(file)
escribir.writerow((nombre,numero))

file.close()