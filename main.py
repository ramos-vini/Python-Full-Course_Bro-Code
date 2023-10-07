print("Let's build a rectangle!")

symbol = input("Enter a symbol: ")
rows = int(input("Now enter the number os rows: "))
columns = int(input("And finally the number of columns: "))

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()