print("Practice:")

print("You\'ll need to know \'bout escapes with \\ \
that do \n newlines and \t tabs")

poem = "\tOnce upon a midnight dreary,\
\n\t while I pondered, weak and weary, \
\n\t\t Over many a quaint and curious volume \
\n\tof forgotten lore- "

print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 6
print("This should equate to five: %s" % 5)

def secret_formula(start):
    jelly_beans = start * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates, = secret_formula(start_point)

print("Starting at: %d" % start_point)
print("There will be %d beans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print("Another way:")
print("There would be %d beans, %d jars, %d crates." % secret_formula(start_point))
