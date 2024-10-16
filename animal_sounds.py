class Animal:
    def __init__(self, name):
        self._name = name

    def emitSound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def bark(self):
        print(self._name + " is barking.")

class Cat(Animal):
    def meow(self):
        print(self._name + " is meowing.")

def main():
    print("1. Dog")
    print("2. Cat")
    animal_type = input("Choose the type of animal (1 or 2): ")

    if animal_type == '1':
        name = input("Enter the dog's name: ")
        dog = Dog(name)
        dog.emitSound()
        dog.bark()
    elif animal_type == '2':
        name = input("Enter the cat's name: ")
        cat = Cat(name)
        cat.emitSound()
        cat.meow()
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
