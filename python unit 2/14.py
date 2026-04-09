import re

text = """
Your long text goes here. It may contain numbers like 9876543210, +91-98765-43210,
or 09876543210 scattered anywhere.
"""

pattern = r'(\+91[-\s]?|0)?\d{10}'

mobile_numbers = re.findall(pattern, text)

mobile_numbers = [num if num.startswith('+') or num.startswith('0') else '+91'+num for num in re.findall(r'\+91[-\s]?\d{10}|0?\d{10}', text)]

print("Mobile numbers found:")
for num in mobile_numbers:
    print(num)
