nice = 0
mean = 0

def main():
    start()

def start():
    print "NICE OR MEAN"
    name  = raw_input("What is your name? : ")
    print "Hello "+name+"!"
    print "In this game, you will be greeted by several individuals and you decide whether to be nice or mean to them."
    print "Your fate will be determined by your choices."

    choice = raw_input ("Would you like to play? y/n ")

    if choice == "y":
        print "Let's begin!"
        print "It is fairly simple: "
        print "Use 'm' to be mean, and 'n' to be nice."
        begin()

    if choice == "n":
        print "You're loss."
        print "Bye!"

def begin():
    global nice
    global mean

    if nice > 2:
        print "Psh, goody-two-shoes."
        print "We all can't be saints like you."
        choice = raw_input("Play again? y/n ")

        if choice == "y":
            print "Alright, here we go..."
            nice = 0
            begin()

        if choice == "n":
            print "I don't blame you."
            exit()

    if mean > 2:
        print "Somebody didn't have their coffee today."
        print "GAME OVER!"
        choice = raw_input("Play again? y/n ")

        if choice == "y":
            print "Better luck this time, Buttercup."
            mean = 0
            begin()

        if choice == "n":
            print "Figured as much."
            print "You grump."
            exit()

        elif choice != "y"+"n":
            print "ENTER A DAMN ANSWER!"

            if choice == "y":
                begin()
            if choice == "n":
                print "Meh."
                exit()

            if choice != "y"+"n":
                choice = raw_input("PLEASEEE! y/n ")

    pick = raw_input("A vagrant askes you for a dollar. Nice or Mean? n/m ")

    if pick == "n":
        print "You've got a heart of gold!"
        nice = nice+1
        print "Score: " +str(nice) + " nice."
        begin()

    if pick == "m":
        print "You cold hearted bastard!"
        mean = mean+1
        print "Score: " +str(mean) + " mean."
        begin()

    
    #pick2 = raw_input("A dapper gentleman askes you for the time. Nice or Mean? n/m ")

    #if pick2 == "n":
        #print "You tell him the correct time."
        #nice = nice+1
        #print "Score: " +str(nice) + " nice."
        #begin()

    #if pick2 == "m":
        #print "You lie and say it is an hour later than it is."
        #mean = mean+1
        #print "Score: " +str(mean) + " mean."
        #begin()




start()

