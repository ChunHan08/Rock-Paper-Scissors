from random import randint
t = ["R", "P", "S"]
computer = t[randint(0,2)]
player = False
name = input("And your name is ?:")
You = 0
PC = 0
print("Type in 'reset' to reset the score")


def win():
  global You
  You +=1
  print(message)
  print('Computer =', PC, '\n', name, '=', You)


def lose():
  global PC
  PC+=1
  print(message)
  print('Computer =', PC, '\n', name, '=', You)


while player == False:
    player = input("Rock, Paper, Scissors?(r,p,s)")
    if player == computer:
        print("Tie!")
        print('computer =', PC)
        print(name, '=', You)
    elif player == "r":
        if computer == "p":
            message = "HAHAH you lose!,Paper covers Rock"
            lose()
        else:
            message = "YAYYYY You win! Scissors cuts Paper"
            win()  
    elif player == "p":
        if computer == "s":
            message = "hahahhahah You lose!,Scissors cuts Rock"
            lose()
        else:
            message = "YESSSS You win!, Scissors cuts Paper"
            win()
    elif player == "s":
        if computer == "r":
            message = " BOOOOO You lose!,Paper covers Rock"
            lose()
        else:
            message = "HAHAHHA You win!, Scissors cuts Paper"
            win()
    elif player == "reset":
      You=1*0
      PC=1*0
      print("Score Reset")
    else:
        print("That's not valid, choose another option!")
    player = False
    computer = t[randint(0,2)]