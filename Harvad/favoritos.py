import csv

#Aqui estoy importando de excel, datos, y voy a saber cual es el favorito si se reite uno con un diccionario
counts={}
with open("./Harvad/cs50-video7.csv","r") as file:
    reader = csv.DictReader(file)

#Esta funcion agrupa los progframa que se repiten dentro de un diccionario
    for row in reader:
        
        title = row["title"].upper()

        if title in counts:
            counts[title]+=1

        else:
            counts[title] = 1

#Esta funcion imprimir los nombres de los programa y si se repite, indica cuanta veces se repitio
for title, count in counts.items():
    print(title,count)


#Esta cuncion imporime en orden de los progrmas que mas se repiten a los que menos se repiten
for title, count in sorted(counts.items(),key=lambda item:item[1],reverse=True):
    print(title, count, sep=" \ ")
