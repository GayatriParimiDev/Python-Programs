import re

text = """
Your long text goes here. It may contain emails like john.doe@example.com, 
contact@my-site.org, or support123@company.co.in anywhere.
"""

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(pattern, text)

print("Email addresses found:")
for email in emails:
    print(email)
