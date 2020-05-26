def promedio(a,b):
    prome=(a+b)/2
    return prome

def numfav(a):

    print("Su numero favorito es el: ",a)

def agregar(a,palabra):
    b = " "
    for i in range (a):

        print(b,palabra)
        b = b + " "

    a2 = a
    for q in range(a):
        a2=a2-1
        b=a2*" "
        print(b,palabra)


def factorial(a):
    for i in range(a):
        print(i,"-",faltorial2(i))

def faltorial2(a):
    resul=1
    for i in range(1,a+1):
        resul=resul*i
    return resul

def main():
    factorial(10)
    agregar(3,"Carlos")
    numfav(10)
    print(promedio(10,10))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
