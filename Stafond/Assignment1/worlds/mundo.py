from karel.stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def paso():
    turn_left()

    while front_is_clear():
        #move()
        if beepers_present():
            while front_is_clear():

                if front_is_blocked():
                    if facing_south():
                        turn_left()
                        move()
                        break
                    turn_left()
                    turn_left()

                if beepers_present():
                    move()
                if no_beepers_present():
                    put_beeper()

            if facing_north():
                if front_is_blocked():
                    turn_left()
                    turn_left()


        if front_is_blocked():
            if facing_south():
                turn_left()
                move()
                break
            turn_left()
            turn_left()
        move()



def main():
    while front_is_clear():

        paso()
        if facing_north():
            turn_right()
            move()
    if right_is_blocked():
        turn_left()
        while front_is_clear():
            move()



# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program()
