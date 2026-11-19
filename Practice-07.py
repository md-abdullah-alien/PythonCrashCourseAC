# Mini Project: Guessing Game
import random

def play_game():
    lucky_num = random.randint(1,50)

    while True:
        user_number = int(input("Guess the lucky number: "))
        if user_number == lucky_num:
            print("You won. Game Over!!!")
            break
        elif user_number < lucky_num:
            print("Too Low. Guess a Higher number")
        else:
            print("Too high. Guess a Lower number")

    print("Thank you for playing!!!")

play_game()





