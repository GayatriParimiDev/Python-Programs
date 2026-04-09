# This program is regarding findding the student's department from their roll number. 

roll_number = input("Enter the student's roll number: ")

if 'cs' in roll_number.lower():
    print("The student is from the CS department.")
else:
    print("The student is not from the CS department.")