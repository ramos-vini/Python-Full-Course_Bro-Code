class Animal:
    species = None

    alive = True

    def eat(self):
        print(f"This {self.species} is eating.")

    def sleep(self):
        print(f"This {self.species} is sleeping.")


class Dog(Animal):
    species = "dog"

    def bark(self):
        print("This dog is barking.")


class Cat(Animal):
    species = "cat"

    def meow(self):
        print("This cat is meowing.")
