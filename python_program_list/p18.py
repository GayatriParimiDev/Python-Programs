#this program is to perform the file methods in python using the read nad write methods.

import os

filename = "demofile.txt"

# Check if file exists, if not, create it
if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("This is the initial content.\n")
    print(f"{filename} created.")

# Perform write operation
with open(filename, "a") as f:
    f.write("Now the file has more content!\n")

# Perform read operation
with open(filename, "r") as f:
    content = f.read()
    print("File Content:")
    print(content)