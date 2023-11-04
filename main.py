import threading
import time


def time_counter():
    print()
    print()
    counter = 0
    while True:
        time.sleep(1)
        counter += 1
        print(f"Your program has been running for {counter} seconds")


x = threading.Thread(target=time_counter, daemon=True)
x.start()

answer = input("Type in anything in order to exit the program: \n")


