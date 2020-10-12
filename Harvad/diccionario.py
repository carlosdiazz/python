palabra = set()

def chequear(word):
    if word.lower() in words:
        return True

    else:
        return False

def cargar(diccionario):
    archivo = open(diccionario, "r")
    for line in file:
        word.add(line.rstrip("\n"))
    file.close()
    return True
   

def tamano():
    return len(words)
    
def descargar():
    return True
   