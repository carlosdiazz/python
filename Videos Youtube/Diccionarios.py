diccionario={"Canada":"Toronto","Francia":"Paris","Colmbia":"Bogota","España":"Madrid"}

#Aqui estoy agregando un valor
diccionario["Venezuela"]="Santiago"

#Aqui me imprime el valor que se encuentra en esta clave
print(diccionario["Canada"])

#Aqui me imprime el dicionario completo
print(diccionario)

#Aqui modifico el valor de una clave en el diccionario
diccionario["Venezuela"]="Caracas"
print(diccionario)

#Aqui elimianos una clave con su valor
del diccionario["Canada"]
print (diccionario)

#Aqui estamos colocando el nombre de la clave directamente de una tupla
pais=("Peru","Argentina","Panama","Mexico")
diccionario2={pais[0]:"Lima", pais[1]:"Buenos Aires", pais[2]:"Ciudad de Panama", pais[3]:"Ciudad de Mexico"}
print(diccionario2)

diccionario3={" Nombre ":" Carlos "," Pais ":" Rep. Dominicana ","Edad":[10,12,14,16]," Ciudad ": " La Vega "}
print(diccionario3["Edad"])

#Aqui me impirme las Claves del diccioanrio
print(diccionario3.keys())

#Aqui me imprime solo el valor de los diccioanrios
print(diccionario3.values())

#Aqui me impirme el valor de mi diccioanrio
print(len(diccionario3))
