
# Task 9: Split text into words from one file and join words to form a sentence in another file.

import re

def main():
    src = "text_src.txt"
    with open(src, "w", encoding="utf-8") as f:
        f.write("This is, perhaps, a test.\nWith multiple lines and punctuation!")

    with open(src, "r", encoding="utf-8") as f:
        data = f.read()

    words = re.findall(r"\w+", data)
    sentence = " ".join(words) + "."
    dst = "text_sentence.txt"
    with open(dst, "w", encoding="utf-8") as f:
        f.write(sentence)

    print("Words:", words)
    print(f"Wrote sentence to {dst}")
    with open(dst, "r", encoding="utf-8") as f:
        print("Sentence content:")
        print(f.read())

if __name__ == "__main__":
    main()
