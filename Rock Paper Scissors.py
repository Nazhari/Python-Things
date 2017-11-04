import random

win = 'false'

while win == 'false':
    ai = random.randint(1,3)
    player = 0
    
    player = int(input("1 for Rock, 2 for Paper, 3 for Scissors. The games end when you win. -> "))
        
    #Check if it's a tie. If it's not a tie, go down.
    if player == ai:
        print("It's a tie!")
    
    #Possible Win/Lose outcomes for Rock.    
    elif player == 1:
        if ai == 2:
            print("Rock Vs. Paper. You lose.")
        else:
            print("Rock Vs. Scissors. You win.")
            win = 'true'
            
    #Possible Win/Lose outcomes for Paper.          
    elif player == 2:
        if ai == 3:
            print("Paper Vs. Scissors. You lose.")
        else:
            print("Paper Vs. Rock. You win.")
            win = 'true'
            
    #Possible Win/Lose outcomes for Scissors.  
    elif player == 3:
        if ai == 1:
            print("Scissors Vs. Rock. You lose.")
        else:
            print("Scissors Vs. Paper. You win.")
            win = 'true'
            
    else:
        print("You made an unidentifiable hand gesture. You lose.")    
