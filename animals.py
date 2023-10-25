class Animal:
    alive = True

    def eat(self):
        print(f"This animal is eating.")


class Predator(Animal):
    def hunt(self):
        print("This predator hunts.")


class Prey(Animal):
    def flee(self):
        print("This prey flees.")


class Fish (Prey, Predator):
    def swim(self):
        print("This fish swims.")


