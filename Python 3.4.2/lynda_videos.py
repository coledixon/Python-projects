class Duck:       
    def quack(self):
        print("Quaaack!")

    def walk(self):
        print('Walks like a duck.')

    def bark(self):
        print('cannot bark')

    def fur(self):
        print('duck has feathers')

class dog:
    def bark(self):
        print('ARF!')

    def fur(self):
        print('Brown and white fur.')

    def walk(self):
        print('walks like a dog')

    def quack(self):
        print('dog\'s don\'t quack')

def main():
    donald = Duck()
    fido = dog()
    in_the_forest(donald)
    in_the_pond(fido)

def in_the_forest(dog):
    dog.bark()
    dog.fur()

def in_the_pond(duck):
    duck.quack()
    duck.walk()
    
if __name__ == '__main__': main()
