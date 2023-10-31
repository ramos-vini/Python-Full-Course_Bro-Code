# my_list = ["belly", "sugar", "petota"]
#
# my_tuple = ("belly", "sugar", "petota")
#
# my_list.sort()
#
# for i in my_list:
#     print(i)
#
# sorted_tuple = sorted(my_tuple)
#
# for i in sorted_tuple:
#     print(i)

tuples_list = [
    ("Belly", "C", 18),
    ("Sugar", "A", 22),
    ("Petota", "F", 36)
]

grade_key = lambda grade: grade[1]

tuples_list.sort(key=grade_key)

for i in tuples_list:
    print(i)