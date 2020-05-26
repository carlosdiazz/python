import random

def main():

    correct=0

    while correct<3:

        Num_1=random.randint(10,99)
        Num_2=random.randint(10,99)
        suma=Num_1+Num_2
        print("Cuanto es la sumatoria de :",Num_1," + ",Num_2)
        res=int(input("Ingrese su respesta: "))

        if res==suma:
            correct = correct + 1
            print("Correcto, Has conseguido: ",correct," respuestas correctas")

        else:
            print("Incorrecto, la sumatoria de: ", Num_1, " + ", Num_2, " es: ", suma)
            correct=0

    print("Felicidades ya sabes sumar")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
