import random

answer = random.randint(0, 5000)

guess = -1

while guess > answer or guess < answer: 
    guess = int(input("Guess a number between 0 and 5000 -> "))
    if guess < 0 or guess > 5000:
        print("It has to be a number between 0 and 5000.")
    if guess >= 0 and guess <= 5000 and guess < answer:
        print("Higher.")
    if guess >= 0 and guess <= 5000 and guess > answer:
        print("Lower.")
    if guess == answer:
        print("That's right.")