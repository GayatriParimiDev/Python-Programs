def print_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File Contents:")
            print(contents)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def copy_file(source, destination):
    try:
        with open(source, 'r') as src, open(destination, 'w') as dest:
            for line in src:
                dest.write(line)
        print(f"File copied from '{source}' to '{destination}'.")
    except FileNotFoundError:
        print(f"Source file '{source}' not found.")

def read_write_file(filename):
    try:
        with open(filename, 'r+') as file:
            data = file.read()
            print("Original File Content:")
            print(data)
            file.write("\nThis is a new line added to the file.")
            print("New line written to the file.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

print_file_contents('example.txt')
copy_file('example.txt', 'copy_of_example.txt')
read_write_file('example.txt')
