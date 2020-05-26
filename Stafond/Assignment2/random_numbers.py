import random

def main():
    NUM_RANDOM=10
    MIN_RANDOM=0
    MAX_RANDOM=100
    for i in range(NUM_RANDOM):
        ok= random.randint(MIN_RANDOM,MAX_RANDOM)
        print(ok)

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
