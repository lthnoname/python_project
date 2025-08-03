import random
def choose():
    choice  = random.randint(1, 3)
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    else:
        return "scissors"

def Judge(player, bot):
    if player == bot:
        return -1
    elif (player == "scissors" and bot == "paper") or (player == "paper" and bot == "rock") or (player == "rock" and bot == "scissors"):
        return 1
    else:
        return 0
    
print("LET'S PLAY ROCK PAPER SCISSORS!!!!!!!!!!!")

GameOver = False

while GameOver == False:
    your_choice = input("Select (rock / paper / scissors): ").lower()
    bot_choice = choose()
    
    print("")
    print(f"You chose: {your_choice}")
    print(f"Computer chose: {bot_choice}\n")

    judge = Judge(your_choice, bot_choice)

    if judge == -1:
        print("It's a draw!!! Let's play again until we find a winner!!")
    elif judge == 1:
        print("Congratulations!!!!! YOU WON\n")
    else:
        print("OOPS! The compter has won\n")

    PlayAgain = input("Do you wish to play again?   (y/n)")
    if PlayAgain == 'n':
        GameOver = True

print("Thank you for playing")