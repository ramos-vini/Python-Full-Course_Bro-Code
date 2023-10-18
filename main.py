try:
    with open("test.txt") as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

