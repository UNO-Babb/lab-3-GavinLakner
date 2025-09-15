#RPS.py
#Name: Gavin Lakner
#Date: 9/14/2025
#Assignment: RPS
import random

def main():
  wins = 0
  ties = 0
  losses = 0
game = input("Want to play Rock Paper Scissors? (Yes/No):")
if game == "Yes": 
  elif print("Goodbye!") == "No":
  print("R = Rock, P = Paper, S = Scissors")
  print('')
  user = int(input("Choose Wisely:"))
  print('')
  'R' == 1
  'P' == 2
  'S' == 3
  if user == 1 and computer == 1:
    print("Must play again! We both played Rock!")
  elif user == 1 and computer == 2:
    print("You lose! You played Rock and I played Paper!")
  elif user == 1 and computer == 3:
    print("You win! You played Rock and I played Scissors!")
  elif user == 2 and computer == 1:
    print("You win! You played Paper and I played Rock!")
  elif user == 2 and computer == 2:
    print("Must play again! We both played Paper!")
  elif user == 2 and computer == 3:
    print("You lose! You played Paper and I played Scissors!")
  elif user == 2 and computer == 1:
    print("You lose! You played Scissors and I played Rock!")
  elif user == 3 and computer == 2:
    print("You win! You played Scissors and I played Paper!")
  elif user == 3 and computer == 3:
    print("Must play again! We both played Scissors!")
  else:
    print("Not a choice.")    
  outcome = random.choice(["win", "lose", "tie"])
  if outcome == "win":
        print("You won this round!")
        wins += 1
  elif outcome == "lose":
        print("You lost this round!")
        losses += 1
  else :outcome == "tie" 
  print("This round was a tie!")
  ties += 1
  user_input = input("Would you like to play again? (yes/no): ").lower()
  if user_input != 'yes':
        play_again = False       
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.
  #In the end, print the stats
print("Wins \t Ties \t Losses")
print("---- \t ---- \t ------")
print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
