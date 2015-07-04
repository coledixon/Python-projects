import time

def listable():
    listable = [67, 45, 1 , 998, 13, 2]
    print(listable)

    time.sleep(0.4)
    practice()


def before():
    listable = [67, 45, 1 , 998, 13, 2]
    for i in listable:
            print(i)

    time.sleep(0.4)        
    practice()

def after():
    listable = [67, 45, 1 , 998, 13, 2]
    print(sorted(listable))

    time.sleep(0.4)
    practice()

def practice():
    print("SELECT ONE: ")
    print("1) PRINT LIST \n2) PRINT UNSORTED LIST \n3)\
 PRINT SORTED LIST")
    choice = input("> ")

    if choice == "1":
        listable()
    elif choice == "2":
        before()
    elif choice == "3":
        after()
    else:
        print("FOLLOW THE INSTRUCTIONS!")

practice()




