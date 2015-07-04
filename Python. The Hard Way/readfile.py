from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file %r:" % filename)
print(txt.read())

print("Type file name:")
file_again = input("> ")

text_again = open(file_again)

print(txt_againg.read)
