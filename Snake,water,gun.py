import random

title = """
            Welcome to Snake, Water, Gun Game
            First of 5 wins the game!
"""
print(title)

game_func = ['snake','water','gun']

user_score = 0
computer_score = 0
total_score = 5
game = True
while game:
    user = input("Enter your choice (snake, water, gun): ").lower()
    while user not in game_func:
        user = input("Invalid choice. Enter your choice (snake, water, gun): ").lower()
    computer = random.choice(game_func)
    print("Computer's choice: ", computer)

    if user == computer:
        print("TIE")
    elif (computer == 'snake' and user == 'water') or (computer == 'gun' and user == 'snake') or (computer == 'water' and user == 'gun'):
        print("Computer Won this round!")
        computer_score += 1
    elif (user == 'snake' and computer == 'water') or (user == 'gun' and computer == 'snake') or (user == 'water' and computer == 'gun'):
        print("You Won this round!")
        user_score += 1

    print("Score - Your score: ", user_score, "Computer score: ", computer_score)

    if user_score == total_score:
        print("You Won the game! Congratulations!")
        game = False
    elif computer_score == total_score:
        print("Computer Won the game! Better luck next time!")
        game = False

    
    choice = input("Do you want to continue? If yes press Y, if no press N: ").lower()
    while choice not in ['y', 'n']:
        choice = input("Invalid choice. If yes press Y, if no press N: ").lower()
    if choice == 'y':
        game = True
    else:
        game = False

print("Final Score - You: ", user_score, "Computer: ", computer_score)