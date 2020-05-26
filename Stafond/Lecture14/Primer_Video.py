
puntuacion=".,"

def quitar_puntuacion(lista):

    resultado=""
    for ok in lista:

        if ok not in puntuacion:
           resultado=resultado+ok

    return resultado

def contar_palabras(file):

    nume=0
    palabras=file.split()

    for pala in palabras:
        print("#"+str(nume+1)+": "+pala)
        nume=nume+1

def contar_palabras2(file):

    nume=0
    for linea in open(file,'r'):
        linea=linea.strip()             #Remove newline
        lista_palabras=linea.split()    #Crear una lsita de palabra

        for pala in lista_palabras:
            print("#"+str(nume+1)+": "+pala)
            nume=nume+1

def main():

    #ok= quitar_puntuacion("Hola, COmo esta, me llamo Carlos y tu. COmo te llmas,")
    #contar_palabras("hola como estas me llamo carlos")
    contar_palabras2('hola.txt')
    #print(ok.strip())
    #print(ok)

if __name__ == '__main__':
    main()
