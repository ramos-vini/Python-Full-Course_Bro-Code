name = "bro Code"

if name[0].islower():
    name = name.capitalize()

print(name)

first_name = name[:3].upper()
last_name = name[4:].upper()

print(first_name)
print(last_name)
print(last_name[-1])
