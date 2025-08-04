import random

guesses = 1

result = random.randint(1, 100)

print("Guess the number (from 1 to 100)\n")

while True:
    your_choice = int(input("Choose your number from 1 to 100: "))
    if(your_choice == result):
        print("Correct!!")
        print(f"Total guesses: {guesses}")
        break
    elif your_choice > result:
        print("Too High")

    else:
        print("Too Low")
    guesses += 1

