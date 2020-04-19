import random 

def game_logic(x, y):
    check = True
    count = x

    randomnum = random.randint(1,y)

    while check:
        try:
            user = int(input(f"\nYou have {count} tries left\nEnter a number between 1 - {y - 1}:    "))
        except ValueError:
            print("Please enter a number")
            #check = False
        else:
            if count > 1:
                if (user != randomnum):
                    check = False
                    print("\nThats wrong, try again")
                    count -= 1
                    check = True
                else:
                    print("\nYou got it right")
                    check = False
            else:
                print("\nYou have used up all your tries. GAME OVER")
                check = False


try:
    initial_page = int(input("Choose a setting.\nEnter 1 for Easy\nEnter 2 for Medium\nEnter 3 for Hard\nChoice :   "))
except ValueError:
    print("Please enter a number")
else:
    if initial_page in range(0,4):
        if initial_page == 1:
            game_logic(x= 6, y = 11)
        elif initial_page == 2:
            game_logic(x = 4, y = 21)
        else:
            game_logic(x= 3, y = 51)
    else:
        print("Not an option")
        
