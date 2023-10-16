def print_name(**names):
    print("Hello, ", end=" ")
    for key, value in names.items():
        print(value, end=" ")


print_name(first="billy", middle="the burger", last="ocean")





