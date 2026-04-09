def find_and_replace(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        updated_content = content.replace('gujarat', 'gujrat')
        
        with open(filename, 'w') as file:
            file.write(updated_content)
        
        print("All occurrences of 'gujarat' replaced with 'gujrat'.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

find_and_replace('file.txt')
