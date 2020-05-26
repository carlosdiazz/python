def main():

    print("Milestone ")
    piedras=int(20)

    while piedras <=20 and piedras>0:


        while True:
            print("Quedan ", piedras, " piedras")
            jugador_1=int(input("Jugador 1, ¿te gustaría eliminar 1 o 2 piedras?: "))
            if jugador_1==1:
                if piedras>=1:
                    piedras = piedras-1
                    break
                else:
                    print("Ya no quedan mas piedras")
                    break

            elif jugador_1==2:
                if piedras>=2:
                    piedras = piedras-2
                    break
                else:
                    print("No puedes eliminar mas de 2 piedras")
                    break

            else:
                print("Ingreso un numero incorrecto, vuelva e intentelo")

        if piedras==0:
            print("El juigador #2, Gano")
            break

        while True:
            print("Quedan ", piedras, " piedras")
            jugador_2=int(input("Jugador 2, ¿te gustaría eliminar 1 o 2 piedras?: "))
            if jugador_2==1:
                if piedras>=1:
                    piedras = piedras-1
                    break
                else:
                    print("Ya no quedan mas piedras")
                    break

            elif jugador_2==2:
                if piedras>=2:
                    piedras = piedras-2
                    break
                else:
                    print("No puedes eliminar mas de 2 piedras")
                    break

            else:
                print("Ingreso un numero incorrecto, vuelva e intentelo")

        if piedras==0:
            print("El jugador #1, Gano")
            break


    piedras=int(20)
    print("Milestone 1")
    while piedras <=20 and piedras>0:

        while True:
            print("Quedan ",piedras," piedras disponibles")
            jugador=int(input("Cuantas piedras deseas eliminar: "))

            if jugador>=0:
                piedras=piedras-jugador
                break
            else:
                print("Ingreso un numero invalido, intente de nuevo")

    print("Game Over")



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
