def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))

def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))

def print_one(arg1):
    print("arg1: %r" % arg1)

def print_none():
    print("NOTHING!")

print_two("Cole", "Dixon")
print_two_again("Turtle", "Hat")
print_one("DONUTS")
print_none()


def cheese_and_crackers(cheese_count, cracker_boxes):
    print("I have %d cheese." % cheese_count)
    print("I also have %d boxes of crackers." % cracker_boxes)
    print("wish I had friends, though.")
    print("oh well, pity party!")
    
print("Function numbers: ")
cheese_and_crackers(20,42)

print("Variables from script: ")
amount_of_cheese = 12
amount_of_crackers = 19

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("Do math: ")
cheese_and_crackers(10+20, 5-4)
