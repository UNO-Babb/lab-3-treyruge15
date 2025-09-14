#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0

  playAgain = "Y"
  while playAgain == "Y":
    #Create a loop that continues as long as the user wants to play.
    #User can play as many games as they wish.

    #Randomly choose the computer between 'R', 'P', or 'S'
    computer = random.choice(["R", "P", "P", "P", "P", "S"])
    player = input("Get ready to play Rock, Paper, Scissors! Choose either R, P, or S to Win: ")
    #Prompt the user for their RPS selection
    #Determine winner and state what happened to the user
    if player == "R":
      print("Player chose Rock")

    elif player == "P":
      print("Player chose Paper")

    else:
      print("Player chose Scissors")

    if computer == "R":
      print("Computer chose Rock")

    elif computer == "P":
      print("Computer chose Paper")

    else:
      print("Computer chose Scissors")

    if player == "R" and computer == "P":
      print("You Lose.")
      losses = losses + 1

    if player == "R" and computer == "S":
      print("You Win!")
      wins = wins + 1

    if player == "P" and computer == "R":
      print("You Win!")
      wins = wins + 1

    if player == "P" and computer == "S":
      print("You Lose.")
      losses = losses + 1

    if player == "S" and computer == "R":
      print("You Lose.")
      losses = losses + 1

    if player == "S" + "scissors" and computer == "P":
      print("You Win!")
      wins = wins + 1

    if player == computer:
      print("Tie")
      ties = ties + 1

  #Ask the user if they would like to play again.
    playAgain = input("Play Again? (Y/N): ")
  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
