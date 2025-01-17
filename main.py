import random

n = random.randint(1,100)
a = -1
guesses = 1


while (a != n):

    a = int(input("Guess the number: "))

    if (a>n):
        print("Lower number please!\n")
        guesses += 1

    elif(a<n):
        print("Higher number please!\n")
        guesses += 1

print(f"\nYou have guessed the number {n} corretly in {guesses} attempts!")


if (guesses<=10):
    print("Thats a WILD guess!")
