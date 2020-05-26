from karel.stanfordkarel import *

#The first function is to rotate 180 degrees
def atras():
    turn_left()
    turn_left()

#The second option is to scroll a row horizontally, and fill it in case you find a beeper
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

#Finally create a cycle, that while the front is clean, call me to my two functions
def main():
    while front_is_clear():
        subir()
        move()
        if front_is_blocked():
            subir()

# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program()
