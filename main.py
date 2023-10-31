store = [
    ("shirt", 10.0),
    ("shoes", 18.00),
    ("socks", 6.50)
]

to_euros = lambda data: (data[0], data[1] * 0.95)

store_euros = map(to_euros, store)

for i in store_euros:
    print(i)

