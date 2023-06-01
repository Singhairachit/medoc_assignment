import random

def coin_toss():
   
    return random.choice(['Heads', 'Tails'])

def play_game():
   
    print("Welcome to 'Heads or Tails'!")
    print("Let's toss a coin. You need to guess the result.")

    # Get user's choice
    user_choice = input("Enter your choice (Heads/Tails): ").capitalize()
    if user_choice not in ['Heads', 'Tails']:
        print("Invalid choice. Please try again.")
        return

    # Perform the coin toss
    result = coin_toss()

    # Determine the winner
    if result == user_choice:
        print(f"The coin landed on {result}.You win!")
    else:
        print(f"The coin landed on {result}. You lose!")

play_game()
