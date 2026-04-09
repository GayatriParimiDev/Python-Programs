

import shutil

def main():
    src = "sample.txt"
    with open(src, "w", encoding="utf-8") as f:
        f.write("Hello file.\nThis is a sample.\nLine 3.\n")

    print(f"Contents of {src}:")
    with open(src, "r", encoding="utf-8") as f:
        print(f.read())

    dst = "sample_copy.txt"
    shutil.copyfile(src, dst)
    print(f"Copied to {dst}")
 
    rw = "sample_rw.txt"
    with open(rw, "w", encoding="utf-8") as f:
        f.write("Start\n")
    with open(rw, "a", encoding="utf-8") as f:
        f.write("Appended\n")
    with open(rw, "r", encoding="utf-8") as f:
        print(f"Contents of {rw}:\n{f.read()}")

if __name__ == "__main__":
    main()
