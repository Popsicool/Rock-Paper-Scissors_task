import random
options = ["R", "P", "S"]
# All posible outcomes when its not a draw
outcome1 = ["R", "P"]
outcome2 = ["P", "R"]
outcome3 = ["R", "S"]
outcome4 = ["S", "R"]
outcome5 = ["P", "S"]
outcome6 = ["S", "P"]


def game():
    print("Rock-Paper-Scissors game")
    print("R stands for Rock, \nP stands for paper,\nS stands for Scissors")
    state = False
    while state == False:
        choice = input("Pick an option between R, P or S: \n")
        # convert choice to uppercase to match what is in the output list incase its inputed in lower case
        choice = choice.upper()
        # when valid option is inputted
        if choice in options:
            com = random.choice(options)
            output = [choice, com]
            if output == outcome1:
                print('Player(Rock):CPU(Paper)')
                print("CPU wins")
                state = True
            elif output == outcome2:
                print('Player(Paper):CPU(Rock)')
                print("Player wins!")
                state = True
            elif output == outcome3:
                print('Player(Rock):CPU(Scissors)')
                print("Player wins!")
                state = True
            elif output == outcome4:
                print('Player(Scissors):CPU(Rock)')
                print("CPU wins!")
                state = True
            elif output == outcome5:
                print('Player(Paper):CPU(Scissors)')
                print("CPU wins!")
                state = True
            elif output == outcome6:
                print('Player(Scissors):CPU(Paper)')
                print("Player wins!")
                state = True
            else:
                # both Player and CPU choose the same Character hence, not among the posible outcomes earlier listed
                if choice == "R":
                    print('Player(Rock):CPU(Rock)')
                    print("Its a Tie! \nReplay the game")
                    state = False
                elif choice == "P":
                    print('Player(Paper):CPU(Paper)')
                    print("Its a Tie! \nReplay the game")
                    state = False
                else:
                    print('Player(Scissors):CPU(Scissors)')
                    print("Its a Tie! \nReplay the game")
                    state = False
        # when the inputted value is not valid
        else:
            print("invalid option selected,Please try again")
            state = False


game()
