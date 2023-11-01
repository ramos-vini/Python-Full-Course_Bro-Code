cities_temp = {"Rio": 34, "Berlin": 13, "Madrid": 21, "Denmark": 7}
print(cities_temp)

cities_temp_fahrenheit = {key: round(value/5*9+32) for (key, value) in cities_temp.items()}
print(cities_temp_fahrenheit)

warm_cities_temp = {key: value for (key, value) in cities_temp.items() if value >= 20}
print(warm_cities_temp)

cities_temp_desc = {key: "Acceptable" if value >= 10 else "No way" for (key,value) in cities_temp.items()}
print(cities_temp_desc)


def check_temp(value):
    if value >= 30:
        return "Too hot"
    elif value >= 20:
        return "Good hot"
    elif value >= 10:
        return "Nice cold"
    else:
        return "Absolutely freezing"


cities_temp_desc_2 = {key: check_temp(value) for (key, value) in cities_temp.items()}
print(cities_temp_desc_2)
