import random
import tkinter as tk
from tkinter import messagebox

OPTIONS = ['rock', 'paper', 'scissors']

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "win"
    else:
        return "lose"

def update_score(result):
    if result == "win":
        scores['player'] += 1
    elif result == "lose":
        scores['computer'] += 1
    else:
        scores['tie'] += 1

    score_label.config(text=f"Player: {scores['player']} | Computer: {scores['computer']} | Tie: {scores['tie']}")

def play_game(player_choice):
    computer_choice = random.choice(OPTIONS)

    result = determine_winner(player_choice, computer_choice)
    message = f"You chose {player_choice}\nComputer chose {computer_choice}\n\n"

    if result == "win":
        message += "You win!"
    elif result == "lose":
        message += "You lose!"
    else:
        message += "It's a tie!"

    messagebox.showinfo("Game Result", message)
    update_score(result)

# Create the main window
window = tk.Tk()
window.title("Rock/Paper/Scissors Game")

# Create the choice label
choice_label = tk.Label(window, text="Choose your move:")
choice_label.pack()

# Create the buttons for each option
button_frame = tk.Frame(window)
button_frame.pack()

for option in OPTIONS:
    button = tk.Button(button_frame, text=option.capitalize(), command=lambda o=option: play_game(o))
    button.pack(side=tk.LEFT, padx=5)

# Create the score labels
scores = {'player': 0, 'computer': 0, 'tie': 0}
score_label = tk.Label(window, text=f"Player: {scores['player']} | Computer: {scores['computer']} | Tie: {scores['tie']}")
score_label.pack()

# Start the main event loop
window.mainloop()
