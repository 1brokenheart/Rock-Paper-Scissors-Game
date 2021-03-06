#Rock-Paper-Scissors Game

#import the randint from random module
from random import randint
#create a list with the 3 different alternatives to choose from
options = ["ROCK", "PAPER", "SCISSORS"]

#create a dictionary with the different messages that the user can get.
message = {"tie": "BOOO it's a tie!","won": "Yeah you won!","lost": "Oh nooo you lost!"}

#create a function to decide the winner.
def decide_winner(user_choice, computer_choice):
    #print user selected choice
    print ("You selected %s: " % user_choice)
  
    #print the computer choice
    print ("Computer selected %s: " % computer_choice)

    #create an if statement to determine if the User's choice is equal to the Computer's choice.
    if user_choice == computer_choice:
        print (message["tie"])
 
    #create an elif statement where the User wins.
    elif user_choice == options[0] and computer_choice == options[2]:
        print (message["won"])
    elif user_choice == options[1] and computer_choice == options[0]:
        print (message["won"])
    elif user_choice == options[2] and computer_choice == options[1]:
        print (message["won"])

    #after taking care of all the possible scenarios where the User can win, the remaining choices will result in a win for the computer the Computer. 
    else:
        print (message["lost"])
        
#create a function to play the game Rock, Paper, Scissors (RPS)
def play_RPS():
#Prompt user to select one among the three choices.
    user_choice = input("Enter Rock, Paper, or Scissors: ")
    
#change the font of the user's choice to upper case
    user_choice = user_choice.upper()

#let the cimputer randomly select one choice from the option list.
    computer_choice = options[randint(0, 2)]
    decide_winner(user_choice, computer_choice)

play_RPS()


