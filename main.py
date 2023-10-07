while True:
    name = input("What's your name?")
    if name != "":
        break

print("Hello " + name)

phoneNumber = "123-456-7890"

for i in phoneNumber:
    if i == "-":
        continue
    print(i, end="")
