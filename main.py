name = "Bro Code"

# Indexing: [start:stop:step]
print(name[4:])
print(name[:5])
print(name[::2])
print(name[2:6:1])
print(name[::-1])

# slice()

website1 = "http://google.com"
website2 = "http://wikipedia.com"

websiteSlice = slice(7, -4)

print(website1[websiteSlice])
print(website2[websiteSlice])
