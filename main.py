name = ""

while len(name) == 0:
    name = input("What's your name?")
    name = name.replace(" ", "")

print("Hello " + name)