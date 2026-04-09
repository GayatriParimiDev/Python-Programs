
# Task 13: Process conference registration data with commas/newlines in fields and header issues.

import csv
import io
from collections import defaultdict, Counter

def main():
    csv_text = '''Name,Affiliation,Role,Email
"Dr. A", "IIT Bombay", "Professor", a@iitb.ac.in
"Ms. B", "IISc, Bengaluru", "Student", b@iisc.ac.in
"Mr. C", "IIT Madras", "Researcher", c@iitm.ac.in
"Mr. C", "IIT Madras", "Researcher", c@iitm.ac.in
"Dr. D", "NIT, Surat", "Professor", "d@nit.ac.in"
"Ms. E", "IIT Kanpur", "Student", "e@iitk.ac.in"
"Mr. F", "ACME, Inc.", "Industry", "f@acme.example"
"Dr. G", "Some University", "Professor",
"Dr. H", "IIT Delhi", "Professor", "h@iitd.ac.in"
"Dr. I", "Institute, of, Science", "Professor", "i@ios.edu"
"Ms. J", "IIT Guwahati", "Student", "j@iitg.ac.in"
"Mr. K", "Xyz College", "Student
Graduate", "k@xyz.edu"
'''
    reader = csv.reader(io.StringIO(csv_text), skipinitialspace=True)
    rows = [r for r in reader if any(c.strip() for c in r)]
    header, data = rows[0], rows[1:]

    def norm(row):
        r = row + [""] * (4 - len(row))
        return [c.strip().strip('"') for c in r[:4]]

    data = [norm(r) for r in data]

    non_students = [r for r in data if r[2].strip().lower() != "student"]
    print("Non-students count:", len(non_students))

    from_iits = [r for r in data if "iit" in r[1].lower()]
    print("Registered from IITs:")
    for r in from_iits:
        print(f"- {r[0]} ({r[1]})")

    counts = Counter(tuple(r) for r in data)
    duplicates = [list(k) for k, v in counts.items() if v > 1]
    print("Duplicate records:")
    for r in duplicates:
        print(r)

    groups = defaultdict(list)
    for name, aff, role, email in data:
        groups[aff].append(name)
    print("Participants grouped by affiliation:")
    for aff, names in groups.items():
        print(f"{aff}: {', '.join(names)}")

if __name__ == "__main__":
    main()
