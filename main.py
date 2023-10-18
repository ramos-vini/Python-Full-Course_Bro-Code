text = "This is just some random text.\n"

try:
    with open("write.txt", "w") as write_file: # This one gets overwritten
        write_file.write(text)

except Exception as e:
    print(e)

try:
    with open("append.txt", "a") as append_file:
        append_file.write(text)

except Exception as e:
    print(e)

