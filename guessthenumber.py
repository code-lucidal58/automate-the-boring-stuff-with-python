# Guess the number game
import random

if __name__ == '__main__':
    name = input("Hello! What is your name? ")
    print("Well {}! I am thinking of a number between 1 and 20.".format(name))
    print("You can make maximum 6 guesses")
    x = random.randint(1, 20)
    c = 0
    for i in range(1, 7):
        guess = int(input("Take a guess. "))
        if guess == x:
            print("Good! You guessed in {} guesses".format(c))
            break
        elif guess > x:
            print("Guess is too high")
        else:
            print("Guess is too low")
        c = i+1
    if c == 7:
        print("Nope. the number I was thinking is {}".format(x))
