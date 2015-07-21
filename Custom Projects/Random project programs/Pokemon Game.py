import time
global gold
global poke
gold = 0
poke = 0

def start():
    print("\t\tGOTTA CATCH 'EM ALL!")
    print("\n")
    name = input("INPUT YOUR NAME: ")
    print("\t\tINITIALIZING...")
    time.sleep(1)
    print("Hello, %s. Let's play a game." % name)
    time.sleep(1)
    print("The object of this game is to collect Pokemon.")
    time.sleep(1)
    print("After collecting the Pokemon, you sell them for gold.")
    time.sleep(1)
    choice = input("Do you want to play? y/n ")
    if choice == "y":
        begin()
    elif choice == "n":
        print("Fair enough. Bye..")

def money():
    global poke
    global gold
    time.sleep(0.4)
    print("Let's sell some Pokemon")
    time.sleep(0.5)
    amount = input("How many would you like to sell? ")
    if amount == "1":
        time.sleep(0.4)
        print("You sold 1 Pokemon for 1 gold.")
        poke = poke-1
        gold = gold+1
        print("You now have", +poke, " Pokemon and", +gold, " gold coin")
    elif amount > "1" and poke == 0:
        print("You don't have any Pokemon. Let's go catch some!")
        begin()
        
    elif amount == "2" and poke < 2:
        print("You do not have enough Pokemon.")
        begin()
    elif amount == "2":
        time.sleep(0.4)
        print("You sold 2 Pokemon for 2 gold.")
        poke = poke-2
        gold = gold+2
        print("You now have", +poke, " Pokemon and", +gold, " gold coins")
    elif amount == "3" and poke < 3:
        print("You do not have enough Pokemon.")
        begin()
    elif amount == "3":
        time.sleep(0.4)
        print("You sold 3 Pokemon for 3 gold.")
        poke = poke-3
        gold = gold+3
        print("You now have", +poke, " Pokemon and", +gold, " gold coins")
       
def other():
    global gold
    global poke
    print("1) SET THEM FREE")
    time.sleep(0.5)
    print("2) SELL THEM TO THE BUTCHER FOR MEAT")
    time.sleep(0.5)
    print("3) SKIN THEM AND MAKE A FINE COAT")
    option = input("> ")
    if option == "1":
        print("You let your Pokemon go.")
        poke = 0
        begin()
    elif option == "2":
        print("Your Pokemon have been butchered and you have fashioned \nthem into a hearty stew.")
    elif option == "3":
        print("You craft a fine coat from your adorable Pokemon \nand leave their corpses in the gutter.")

def begin():
    global poke
    global gold
    time.sleep(0.3)
    print("You head out exploring.")
    time.sleep(0.4)
    print("You see a wild Pokemon!")
    time.sleep(0.4)
    pick = input("Do you want to catch this Pokemon? y/n ")
    if pick == "y":
        time.sleep(0.4)
        print("You caught a Pokemon!")
        poke = poke+1
        time.sleep(0.3)
        print("You currently have", +poke, " Pokemon.")
        begin()
    elif pick == "y" and poke == 3:
        print("You have too many Pokemon. Try selling some.")
        money()
    elif pick == "n" and poke == 0:
        time.sleep(0.3)
        print("You can't get any gold unless you catch some Pokemon. \nThat's commerce.")
        begin()
    elif pick == "n" and poke >=1:
        time.sleep(0.3)
        sell = input("Do you want to sell a Pokemon? y/n ")
        if sell == "y" and poke >= 1:
            money()
        elif sell == "n":
            print("What do you want to do with your Pokemon then?")
            other()

start()
