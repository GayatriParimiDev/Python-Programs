#This program for using the readline() to find or print upto 5 lines from five lines.

with open("demofile.txt", "r") as f:
    for i in range(5):
        line = f.readline()
        if not line:
            break
        print(line.strip())

    