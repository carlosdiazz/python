from karel.stanfordkarel import *

#The first function is to rotate 180 degrees
def giro():
    turn_left()
    turn_left()

#The second function is to fill the first line of beeper
def primera():
    while front_is_clear():
        put_beeper()
        move()
    if left_is_clear():
        put_beeper()
        if front_is_clear():
            giro()
        else:
            pick_beeper()

#The third line is to locate the midpoint of the table
def recorrer():
    while beepers_present():

        if beepers_present():
            if front_is_clear():
                move()
            if no_beepers_present():
                giro()
                move()
                pick_beeper()
                move()
        if front_is_blocked():
            if no_beepers_present():
                giro()
                move()
                pick_beeper()

        if front_is_blocked():
            pick_beeper()
            giro()
            move()

#The last function is to put a beeper at the midpoint when karel is there
def ultimo():
    if front_is_clear():
        giro()
        move()
        put_beeper()
        giro()

    if front_is_blocked():
        put_beeper()
        giro()

def main():
    primera()
    recorrer()
    ultimo()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
