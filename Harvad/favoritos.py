import csv

#Aqui estoy importando de excel, datos, y voy a saber cual es el favorito si se reite uno con un diccionario

with open("./Harvad/cs50-video7.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["title"])