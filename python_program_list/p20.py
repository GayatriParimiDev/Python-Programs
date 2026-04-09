#This is a program to find the 12th character from a file.

with open(r"D:\PythonPrograms\python_program_list\infofile.txt", "r") as f:
    f.seek(11)  
    char = f.read(1)  
    print("The 12th character is:", char)