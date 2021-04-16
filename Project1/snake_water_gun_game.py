import random
#Rock Paper Scissors Game
def game(comp, your):
    #if two values are equal declare a tie
    if comp == your:
        return None
    #check for all possibilities when comp chose r    Rock 
    elif comp == "r":
        if your == 's':
            return False
        elif your == 'p':
            return True
    #check for all possibilities when comp chose p     Paper      
    elif comp == 'p':
        if your == 'r':
            return False
        elif your == 's':
            return True
    #check for all possibilities when comp chose s     Scissors   
    elif comp == 's':
        if your == 'p':
            return False
        elif your == 'r':
            return True

#gettin random number with random module
randno = random.randint(1, 3)
if randno == 1:
    comp ="r"
if randno == 2:
    comp ="p"
if randno == 3:
    comp = "s"
    

print("computer turn: Rock(r) Paper(p) or Scissor(s) ?")

your = input("players turn: Rock(r) Paper(p) or Scissor(s) ?")

print(f"computer chose : {comp}")
print(f"computer chose : {your}")


a = game(comp, your)

if a == None:
    print('the game is a tie')
elif a:
    print("you win")
else:
    print("u lose")        