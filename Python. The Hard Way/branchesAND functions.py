import time
from sys import exit

def gold_room():
    print("This room is full of gold. \nHow much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("TYPE A DAMN NUMBER")

    if how_much < 50:
        print("You're not greedy. Kudos")
        exit(0)
    else:
        dead("You greedy bastard.")

def bear_room():
    print("There is a bear here.")
    time.sleep(1)
    print("The bear has a bunch of honey.")
    time.sleep(1)
    print("The fat bear is in front or another door.")
    time.sleep(1)
    print("What do you do? \
\n\t1: Take some honey. \n\t2: Taunt the bear. \
\n\t3: Soil yourself, turn and run away. \
\n\t4: Open door.")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "1":
            dead("The bear slaps your face right off.")
        elif choice == "2" and not bear_moved:
            print("The bear looks at you, grimaces, and moves aside.")
            bear_moved == True
            gold_room()
        elif choice == "2" and bear_moved:
            dead("The bear slowly ambles towards you, knocks you to the ground and chews your leg off.")
        elif choice == "3":
            print("Not your proudest moment.")
        elif choice == "4" and bear_moved:
             gold_room()
        else:
            print("You are not very good at following instructions.")
        
def void_room():
    print("This room is void of all time and space.")
    time.sleep(1)
    print("A faint nissing begins to build up around you.")
    time.sleep(1)
    print("You vision begins to blur and you mouth is dry.")
    time.sleep(1)
    print("As you begin to passout, you catch a glimpse of a shadow.")
    time.sleep(1)
    print("What do you do? \
\n\t1: Ask the shadowy figure for assistance. \
\n\t2: Let yourself fall to the ground. \
\n\t3: Soil yourself and fall to the ground.")

    choice = input("> ")

    if choice == "1":
        dead("The shadow wraps itself around you and slowly digests your flesh.")
    elif choice == "2":
        print("You fall hard to the ground.")
        start()
    elif choice == "3":
        print("Another proud moment in your life.")
    else:
        void_room()

def dead(why):
    print(why, "good job!")
    exit(0)

def start():
    print("You awaken in a dark room.")
    time.sleep(1)
    print("There is a door to your left and a door to your right.")
    time.sleep(1)
    print("Which one do you take? \
\n\t1: Right \n\t2: Left")

    choice = input("> ")

    if choice == "1":
        bear_room()
    elif choice == "2":
        void_room()
    else:
      dead("You stumble around the room until you starve.")

start()
