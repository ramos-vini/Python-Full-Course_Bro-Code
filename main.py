usernames = ["billy", "johnson", "petodas"]

passwords = ["billy_matato", "sonjohn", "potatoes"]

users = dict(zip(usernames, passwords))

print(type(users))

for (key, value) in users.items():
    print(key + " : " + value)
