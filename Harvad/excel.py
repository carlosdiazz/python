import csv

file = open("./Harvad/texto.csv", "a")

nombre=input("Ingrese su nombre: ")
numero=input("Ingrese su numero: ")

escribir=csv.writer(file)
escribir.writerow((nombre,numero))

file.close()