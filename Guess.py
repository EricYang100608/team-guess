import random

answer = random.randint(1, 100)
guess = int(input("Guess a number (1-100): "))

if guess == answer:
    print("Correct!")
elif guess < answer:
    print("Too low!")
elif guess > answer:
    print("Too high!")