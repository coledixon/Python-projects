the_count = [1,2,3,4,5,6,7,8,9]

fruits = ["apples", "oranges", "starwberries", "pineapple"]

change = [1, "pennies", 2, "dimes", 3, "nickels"]

for number in the_count:
    print("This is count %d" % number)

for fruit in fruits:
    print("A fruit of type: %s." % fruit)

for i in change:
    print("I only have %r." % i)

elements = []

for i in range(0, 9):
    print("Adding %d to list." % i)
    elements.append(i)

for i in elements:
    print("Element was: %d." % i)
