import random

print("******👾  WELCOME TO THIS GAME  👾******")
print("\n")
print("Winning rules for STONE, PAPER, SCISSORS are :")
print("Rock vs Paper -> Paper wins.")
print("Rock vs Scissors -> Scissor wins.")
print("Paper vs Scissors -> Scissor wins.")
print("\n")

while True :
    print("Choices : \n 1 = Rock \n 2 = Paper \n 3 = Scissors")
    print("\n")

    choice = int(input("Enter your choice : "))

    while choice > 3 or choice < 1 : 
        choice = int(input("Please enter valid choice : "))

    if choice == 1:
          choice_name = "Rock"
    if choice == 2 :
         choice_name = "Paper"
    if choice == 3 :
         choice_name = "Scissors" 

    print("\n")

    print("users choice is : ",choice_name)
    print("\n") 
    print("Now its computers Turn ...")
    print("\n")

    comp_choice = random.randint(1,3)

    while comp_choice == choice :
         comp_choice = random.randint(1,3)
        
    if comp_choice == 1 :
         comp_choice_name = "Rock"
    if comp_choice == 2 :
         comp_choice_name = "Paper"
    if comp_choice == 3 :
         comp_choice_name = "Scissors"

        
    if choice == comp_choice :
         print("It's a draw : ",end="")
         result = "DRAW"
    if choice == 1 and comp_choice == 2 :
         print("Paper wins => ",end="")
         result = "Paper"
    elif choice == 2 and comp_choice == 1 :
        print("Paper wins => ",end="")
        result = "Paper"
         
    if choice == 1 and comp_choice == 3 :
         print("Rock wins wins => ",end="")
         result = "Rock"
    elif choice == 3 and comp_choice == 1 :
        print("Rock wins wins => ",end="")
        result = "Rock"

    if choice == 2 and comp_choice == 3 :
         print("Scissor wins => ",end="")
         result = "Scissor"
    elif choice == 3 and comp_choice == 2 :
        print("Scissor wins => ",end="")
        result = "Scissor"
             
    if result == "DRAW" :
         print("It's a TIE")
    elif result == choice_name :
         print("congratulations !!, you won")
    else :
         print("computer wins ")
     
     

    print("\n do you want to play again ?\n enter(y/n)")
    ans = input()
    if ans == 'n':
         break
    
print("\n")
print("Thanks for playing 🫡")


    
