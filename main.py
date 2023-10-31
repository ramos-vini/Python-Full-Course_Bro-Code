import functools

numbers = [5, 4, 3, 2, 1]

factorial = functools.reduce(lambda x, y: x * y, numbers)

print(factorial)

