with open("sample.txt", "r") as f:
    for i in range(5):
        line = f.readline()
        if not line:
            break
        print(line.strip())
