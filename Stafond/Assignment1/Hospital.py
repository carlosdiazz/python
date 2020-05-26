from karel.stanfordkarel import *

def derecha():
    for i in range(3):
        turn_left()

def hospital():
    turn_left()
    for i in range(2):
        move()
        put_beeper()
    derecha()
    move()
    derecha()
    for i in range(2):
        put_beeper()
        move()
    put_beeper()
    turn_left()
    if front_is_clear():
        move()

def main():
    while front_is_clear():
        if beepers_present():
            hospital()
        else:
            move()

if __name__ == "__main__":
    run_karel_program()
