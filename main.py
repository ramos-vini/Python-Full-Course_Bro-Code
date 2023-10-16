def sum_numbers(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    print(sum)


sum_numbers(1, 2, 3.5, 4)

