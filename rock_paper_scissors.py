import random
def play_game():
    ##asks how many times would the user would like to play the game
    how_many_times = int(input("How many games would you like to play? "))
    uwins = 0
    cwins = 0
    var = 0
    choices =("Rock", "Paper", "Scissors")

    ##loop for game
    for i in range(how_many_times):
        
        ##Takes the input from the user for the game and checks the input
        ##so that it can correct the user if it is not the right input.    
        rps = str(input("Rock, Paper, or Scissors? "))
        
        while rps != 'Rock' and rps != 'Paper' and rps != 'Scissors':
            rps = str(input("Rock, Paper, or Scissors? ")) 
        ##print(rps);

        ##Computer's choices and makes a choice
        ##print(random.random())
        rannum = random.random()
        if (rannum <= 0.3):
            choice = choices[0]
        elif(rannum <= 0.6):
            choice = choices[1]
        else:
            choice = choices[2]


        ##Compare the choices and decide who wins
        if(rps == choice):
            print("Tie")
        elif(rps != choice):
            if(rps == "Rock"):
                if(choice == "Paper"):
                    print("computer wins")
                    cwins += 1
                else:
                    print("User wins")
                    uwins += 1
            if(rps == "Paper"):
                if(choice == "Scissors"):
                    print("computer wins")
                    cwins += 1
                else:
                    print("User wins")
                    uwins += 1
            if(rps == "Scissors"):
                if(choice == "Rock"):
                    print("computer wins")
                    cwins += 1
                else:
                    print("User wins")
                    uwins += 1
        print("The game is Player: " + str(uwins) + " Computer: " + str(cwins))


