try:
    numerator = float(input("Enter the numerator of the division: "))
    denominator = float(input("Now enter the denominator: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can not divide a number by Zero.")
except ValueError as e:
    print(e)
    print("Please enter only numbers.")
except Exception as e:
    print(e)
    print("Something went wrong.")
else:
    print(f"Result: {result}")
finally:
    print("This will always be executed.")

