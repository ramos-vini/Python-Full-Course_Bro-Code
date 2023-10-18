import random

print(random.randint(1, 6))

print(random.random())

options = ["rock", "paper", "scissors"]
# print(type(options))

print(random.choice(options))

sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

random.shuffle(sequence)

print(sequence)

