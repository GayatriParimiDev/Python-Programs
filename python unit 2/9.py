def split_and_join_words(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            text = file.read()

        words = text.split()
        sentence = ' '.join(words)

        with open(output_file, 'w') as file:
            file.write(sentence)

        print("Words split and joined successfully.")
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")

split_and_join_words('input.txt', 'output.txt')
