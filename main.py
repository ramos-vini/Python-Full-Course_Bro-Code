clothes = {"shirt", "pants"}
utensils = {"knife", "map", "lighter", "lighter"}
dishes = {"knife", "plate", "cup"}

clothes.add("hat")

utensils.update(clothes)

print(utensils)

print(utensils.intersection(dishes))

print(utensils.difference())

