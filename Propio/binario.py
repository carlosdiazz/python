import os,random;os.system("clear")

def binario(nume):
    final=[]
    if nume == 0:
        return "0000000000000"
    else:
        while nume>0:
            bina=nume%2
            nume=nume//2
            final.append(bina)
        final.reverse()
        #Aqui estoy convirtiendo la cadena en un string 
        binario="".join(map(str, final))

        while len(binario)<13:
            binario="0"+binario
        
        return binario

def linea_ale():
    linea=""

    for i in range(20):
        ale=random.randint(0,1)
        if ale == 1:
            linea=linea+"-"
        else:
            linea=linea+"~"
    return linea

def encriptar(lista):

    inicial=linea_ale()
    for i in lista:
        if i == str(1):
            inicial=inicial+"~"
        else:
            inicial=inicial+"-"

    return inicial

def desencriptar(lista):
    nueva=lista[20:]
    final=""
    for i in nueva:
        
        if i == "~":
            final=final+"1"
        else:
            final=final+"0"
    return final

def convertir_a_decimal(lista):
    final=0
    ok=len(lista)
    #Aqui el string lo estoy invirtiendo
    lista=lista[::-1]
    for i in range(ok):
        if lista[i]=="0":
            final=final+0
        elif lista[i]=="1":
            final=final+(2**i)
    return final    

def imprimir():
    numero=int(input("Ingrese un numero para convertir: "))
    bina=binario(numero)

    print("-----------------------------------------------------------------")
    print(f"Uste ingreso el numero {numero} en binario es: {bina}")

    print("-----------------------------------------------------------------")
    print("Aqui esta encriptado en la linea: ")
    encriptado=encriptar(bina)
    print(encriptado)

    print("-----------------------------------------------------------------")
    print("Aqui se esta desencripto la linea en binario: ")
    desen=desencriptar(encriptado)
    print(desen)

    print("-----------------------------------------------------------------")
    print("Aqui se esta desencripto el binario en decimal: ")
    print(convertir_a_decimal(desen))
#imprimir()

def mensaje_final(mensaje,terminal):

    print(f"Aviso, esta es la terminal:         {terminal} \n")
    numero_binario=binario(terminal)
    linea_encriptada=encriptar(numero_binario)

    print(linea_encriptada)
    print(f"\nEl mensaje es: \n \n \n {mensaje} \n \n \n")
    print(linea_encriptada)
    print(f"\nAviso, esta es la terminal:         {terminal}\n \n")

def mandar():
    mensaje=input("Que mensaje deseas mandar a las terminales: ")
    terminal=int(input("A cual terminar le deseas mandar el mensaje: "))
    os.system("clear")
    mensaje_final(mensaje,terminal)

def comprobar_linea():
    nada=input("Enter Para continuar: ")
    os.system("clear")
    linea=input("Copie la linea para desencriptar el numero: ")
    binario_enlinea = desencriptar(linea)
    decimal_enbianrio=convertir_a_decimal(binario_enlinea)
    print(f"El binario es {binario_enlinea} y el numero es: {decimal_enbianrio}")

mensaje_final("Hola ustedes fallaron",2062)

#for i in range(10):
#    ok=(encriptar(binario(12)))
#    print(ok)

#mandar()
comprobar_linea()