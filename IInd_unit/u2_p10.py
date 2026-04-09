
# Task 10: Replace all occurrences of 'gujarat' with 'gujrat' in a file.

def main():
    src = "state.txt"
    with open(src, "w", encoding="utf-8") as f:
        f.write("Many people in gujarat love kite festivals.\nGujarat is also known for crafts.\n")
    with open(src, "r", encoding="utf-8") as f:
        data = f.read()
    replaced = data.replace("gujarat", "gujrat")  # case-sensitive as specified
    dst = "state_fixed.txt"
    with open(dst, "w", encoding="utf-8") as f:
        f.write(replaced)
    print("Original:\n", data, sep="")
    print("Replaced:\n", replaced, sep="")
    print(f"Output written to {dst}")

if __name__ == "__main__":
    main()
