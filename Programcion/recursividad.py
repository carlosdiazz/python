contra= "admi";user="usuario"
    
def login(intentos=1):  

    use=str(input("Escriba su user: "))
    cont=str(input("Escriba su contrsena : "))

    if (cont!=contra or use!=user):
        if intentos < 3:
            intentos = intentos + 1
            print("Datos erroneos, intentalo otra vez")
            login(intentos)
        else:
            print("Ya  no puedes entrar mas reinicia el programa...")
            
    else:
        print()

