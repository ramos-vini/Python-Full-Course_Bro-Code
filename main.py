import os

src = "text.txt"
destination = "/Users/viniciusramos/Desktop/text.txt"

try:
    if os.path.exists(destination):
        print("This path already exists in the destination.")
    else:
        os.replace(src, destination)
        print(f"'{src}' was successfully moved.")

except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)


