import os
import shutil

path = "test.txt"

try:
    os.remove(path)        # for files
    # os.rmdir(path)       # for empty folders
    # shutil.rmtree(path)  # for folders with files (dangerous function)

except FileNotFoundError as e:
    print(e)
except PermissionError as e:
    print(e)
except OSError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f"{path} was successfully deleted.")


