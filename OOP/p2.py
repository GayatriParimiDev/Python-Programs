from datetime import date, datetime

class Person:
    def __init__(self, name, country, date_of_birth_str):
        """
        date_of_birth_str should be in format 'YYYY-MM-DD', e.g. '2000-05-21'
        """
        self.name = name
        self.country = country
        # Convert string to date object
        self.date_of_birth = datetime.strptime(date_of_birth_str, "%Y-%m-%d").date()

    def get_age(self):
        today = date.today()
        years = today.year - self.date_of_birth.year
        # Adjust if birthday has not occurred yet this year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1
        return years


# Example usage
person1 = Person("Alice", "India", "2002-08-15")
print("Name:", person1.name)
print("Country:", person1.country)
print("Date of Birth:", person1.date_of_birth)
print("Age:", person1.get_age())
