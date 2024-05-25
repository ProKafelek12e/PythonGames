import keyboard
import random
import sys
selected = 1
RED = "\033[91m"
GREEN= "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

def show_menu():
    global selected
    print("\n" * 30)
    print("Choose an option:")
    options = ["Rock", "Paper", "Scissors"]
    for i in range(1, 4):
        print("{1} {0}. {2} {3}".format(i, ">" if selected == i else " ", options[i-1], "<" if selected == i else " "))

def up():
    global selected
    if selected == 1:
        return
    selected -= 1
    show_menu()

def down():
    global selected
    if selected == 4:
        return
    selected += 1
    show_menu()
def select():
    print("\n" * 30)

    #Player
    print("You:")
    if(selected==1):
        print('Rock')
    elif(selected==2):
        print('Paper')
    elif(selected==3):
        print('Scissors')

    #Computer
    print("\nComputer:")
    computerPick = random.randint(1,3)
    if(computerPick==1):
        print('Rock')
    elif(computerPick==2):
        print('Paper')
    elif(computerPick==3):
        print('Scissors')

    #Result
    print("\n\nResult:")
    if(selected==computerPick):
        print(f'{BLUE}Draw{RESET}')
    elif((selected==1 and computerPick==3) or (selected==2 and computerPick==1) or (selected==3 and computerPick==2)):
        print(f'{GREEN}Player Win{RESET}',file=sys.stderr)
    elif((selected==3 and computerPick==1) or (selected==1 and computerPick==2) or (selected==2 and computerPick==3)):
        print(f'{RED}Player Lost{RESET}',file=sys.stderr)



def playAgain():
    show_menu()

show_menu()
keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('enter',select)
keyboard.add_hotkey('space',playAgain)
keyboard.wait()