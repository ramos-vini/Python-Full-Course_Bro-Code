numbers = []

for i in range(1, 11):
    numbers.append(i)

print(numbers)

numbers2 = [i for i in range(1, 11)]
print(numbers2)

numbers_even = list(filter(lambda i: i % 2 == 0, numbers))
print(numbers_even)

numbers_odd = [i for i in range(1, 11) if i % 2 != 0]
print(numbers_odd)

numbers_odd_x = [i if i % 2 != 0 else "X" for i in range(1, 11)]
print(numbers_odd_x)

