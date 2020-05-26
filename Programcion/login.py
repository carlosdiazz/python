import random
codigo_acceso=random.randint(100,1000)


def login():
    contra1="123";user1="jose";intentos=1
    
    while True:
        user=str(input("Ingrese su nombre: "))
        contra=str(input("Ingrese su contraseña: "))
        if (user == user1 and contra == contra1):
            print("Ingresaste Correctamente")
            print("Ingrese con este codigo: ",codigo_acceso)
            break

        else:
            if intentos < 3:
                intentos=intentos + 1
                print("Introdujo unos datos incorrecto")
            else:
                print("Ya no peudes entrar mas al programa, REINICIE TODO")
                break

