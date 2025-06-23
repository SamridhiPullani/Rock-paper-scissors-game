import random

choices = ["rock", "paper", "scissors"]

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def display_result(user, computer, winner):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if winner == "tie":
        print("Result: It's a tie! ")
    elif winner == "user":
        print("Result: You win this round! ")
    else:
        print("Result: Computer wins this round! ")

def play():
    user_score = 0
    comp_score = 0
    round_number = 1

    print("==== Welcome to Rock-Paper-Scissors ====")

    while True:
        print(f"\nRound {round_number}")
        user = input("Choose (rock/paper/scissors): ").lower()
        if user not in choices:
            print("Invalid input. Please try again.")
            continue

        computer = random.choice(choices)
        winner = get_winner(user, computer)

        display_result(user, computer, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            comp_score += 1

        print(f"Scoreboard ➤ You: {user_score} | Computer: {comp_score}")

        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("\nThanks for playing! ")
            if user_score > comp_score:
                print(" You won the game!")
            elif user_score < comp_score:
                print("Computer won the game!")
            else:
                print(" The game ended in a tie!")
            break

        round_number += 1

play()
