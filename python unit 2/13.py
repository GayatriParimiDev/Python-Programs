import csv
from collections import defaultdict

file_path = "registrations.csv"

records = []
with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if not row or all(v.strip() == "" for v in row.values()):
            continue
        records.append(row)

non_students = [r for r in records if r.get('Role', '').lower() != 'student']
print("Number of non-students registered:", len(non_students))

iit_participants = [r for r in records if 'iit' in r.get('Affiliation', '').lower()]
print("\nParticipants from IITs:")
for r in iit_participants:
    print(f"{r.get('Name')} - {r.get('Affiliation')}")

seen = set()
duplicates = []
for r in records:
    identifier = tuple(r.items())
    if identifier in seen:
        duplicates.append(r)
    else:
        seen.add(identifier)

print("\nDuplicate records:")
for r in duplicates:
    print(r)

grouped = defaultdict(list)
for r in records:
    affiliation = r.get('Affiliation', 'Unknown')
    grouped[affiliation].append(r.get('Name'))

print("\nParticipants grouped by affiliation:")
for affil, names in grouped.items():
    print(f"{affil}: {', '.join(names)}")
