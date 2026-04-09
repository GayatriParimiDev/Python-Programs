# Dictionary of names and birthdays in DD/MM/YY format
birthdays = {
    "luis": "12/01/99",
    "mary": "23/02/85",
    "jane": "05/03/90",
    "justin": "17/05/92",
    "pam": "30/08/01",
    "megan": "15/10/88",
    "phil": "01/11/95",
    "alex": "22/12/89",
}


month = input("Enter the month (MM): ")

print(f"Birthdays in month {month}:")
found = False
for name, date in birthdays.items():
    if date[3:5] == month:
        print(f"{name}: {date}")
        found = True

if not found:
    print("No birthdays found for this month.")