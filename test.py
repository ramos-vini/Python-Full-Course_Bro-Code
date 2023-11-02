import main


def hello_test():
    print("hello from test.py")


if __name__ == "__main__":
    print("Now this is the main file")
else:
    hello_test()
    print(main.__name__)
