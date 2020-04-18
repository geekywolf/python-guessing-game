import random 

def random_generator(x,y):
    number = random.randint(x,y)
    return number

def easy():
    check = True
    count = 6

    randomnum = random_generator(0,10)

    while check:
        try:
            user = int(input(f"\nYou have {count} tries left\nEnter a number between 1 - 10:    "))
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

def medium():
    check = True
    count = 4

    randomnum = random_generator(0,20)

    while check:
        try:
            user = int(input(f"\nYou have {count} tries left\nEnter a number between 1 - 20:    "))
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

def hard():
    check = True
    count = 3

    randomnum = random_generator(0,50)

    while check:
        try:
            user = int(input(f"\nYou have {count} tries left\nEnter a number between 1 - 50:    "))
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
            easy()
        elif initial_page == 2:
            medium()
        else:
            hard()
    else:
        print("Not an option")
        
