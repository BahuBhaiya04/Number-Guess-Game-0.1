# nice one
from random import randint


# Function Define


def inp_try():
    while True:
        try:
            guess = int(input())
            break
        except:
            print("Wrong Input\nInput A Number")
    return guess


def gam_cont():
    global boolean_main  # Brings Variable from outside scope
    print("         Play Again\n Yes:No")

    while True:
        gam_cont_ch = input()

        if gam_cont_ch.upper() == "NO":
            #        globals(boolean_main)= True  # Modifying Global Variable WRONGGGGGGGG
            boolean_main = 0
            break
        elif gam_cont_ch.upper() == "YES":
            break
        else:
            print("I did Not Understand Yes:No")
            continue
    return boolean_main


def game_end_msg():
    print(10 * "=", "GAME END", 10 * "=")


def result_call(guess1):
    global br_k
    if guess1 == g_num:
        print("HOORAHH!!!\nYOU WON\n In", i, "Tries\n",
              10 * "=")
        game_end_msg()
        gam_cont()
        br_k = 0
    elif i == chance:
        if guess1 != g_num:
            print("You Have Used All Your Chances\nCorrect Number Was", g_num,
                  "\nBETTER LUCK NEXT TIME\n")
            game_end_msg()
            gam_cont()
        elif guess1 == g_num:
            print("HOORAHH!!!\nYOU WON\n In", chance, "Tries\n",
                  10 * "=")
            game_end_msg()
            gam_cont()
    elif guess1 > g_num:
        print("Wrong Guess\nTry Lower ;)")
    elif guess1 < g_num:
        print("Wrong Guess\nTry Higher ;)")


# ===============================MAIN============================= #
boolean_main = 1
while True:
    # Game Loop
    if boolean_main == 1:

        # P1 Work Interaction
        while True:
            try:
                print("--Input Number Guessed Between\nMaximum Number Guessed")
                max_g = int(input())
                print("Minimum Number Guessed")
                min_g = int(input())
                g_num = randint(min_g, max_g)
                break
            except:
                print("Wrong Input\nInput A Number")

        # Chance input

        while True:
            try:
                print("Input Maximum and Minimum number of Chances\nMaximum Chances:")
                max_chance = int(input())
                print("Minimum Chances")
                min_chance = int(input())
                chance = randint(min_chance, max_chance)
                print("You got", chance, "Chances")
                break
            except:
                print("Wrong input\n", 10 * "=", "Input Number", 10 * "=")

        # GAME START MESSAGE
        print(10 * "=", "GAME START", 10 * "=", "\nYou Got", chance, "Tries\nGOOD LUCK!!!")

        # =================================Game Built================================== #
        br_k = 1
        for i in range(1, chance + 1):
            if br_k == 1:
                # Hope it may work
                if i != chance:
                    print("Chance", i, )
                    result_call(inp_try())
                else:
                    print(10 * "=", "Last Chance", 10 * "=")
                    result_call(inp_try())
            else:
                break
    else:
        print("Thankyou for Plying The GaME")
        break
