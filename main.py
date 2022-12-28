import random, time


choice = ["rock", "paper", "scissors"]


def main(y):
   Computer = random.choice(choice)
   c = choice
   print(f"choices: {c[0]}, {c[1]}, and {c[2]}")
   y = input("[move]> ")
   
   if Computer == y:
      print("It's a tie!")
   elif Computer == "rock" and y == "paper":
      print(f"{name} won! Paper beats rock.")

   elif Computer == "rock" and y == "scissors":
      print("Computer won! Rock beats scissors.")
      
   elif Computer == "paper" and y == "rock":
      print("Computer won! Paper beats rock.")
      
   elif Computer == "paper" and y == "scissors":
      print(f"{name} won! Scissors beat paper.")
      
   elif Computer == "scissors" and y == "rock":
      print(f"{name} won! Rock beats scissors.")
      
   elif Computer == "scissors" and y == "paper":
      print("Computer won! Scissors beat paper.")
  
   else:
      print("Invalid move")


name = input("Enter your name: ")
while True:
  main(name)
  time.sleep(0.5)