from karel.stanfordkarel import *


def atras():
    turn_left()
    turn_left()


def derecha():
    turn_left()
    turn_left()
    turn_left()


def subir():
    turn_left()

    while facing_north():
        if front_is_clear():
            if no_beepers_present():
                move()

        if front_is_clear():
            if beepers_present():
                move()
                if no_beepers_present():
                    put_beeper()

        if front_is_blocked():
            atras()

            while facing_south():
                if front_is_clear():
                    if no_beepers_present():
                        move()

                if front_is_clear():
                    if beepers_present():
                        move()
                        if no_beepers_present():
                            put_beeper()

                if front_is_blocked():
                    turn_left()


def main():
    while front_is_clear():
        subir()
        move()
        if front_is_blocked():
            subir()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program()
