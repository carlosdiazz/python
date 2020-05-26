from karel.stanfordkarel import *

#I created a common function to fill 3 sides of the squares with beepers
def colocar():
    for i in range(3):
        while left_is_blocked():
            put_beeper()
            move()
        turn_left()
        move()

#Then in the main, I call 3 times my function since the examples always had 3 squares
def main():
    for i in range(3):
        colocar()
        turn_left()
        turn_left()
        move()

if __name__ == "__main__":
    run_karel_program()
