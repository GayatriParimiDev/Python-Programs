
# Task 14: Find all mobile numbers out of a long text (Indian formats).

import re

def main():
    text = """
Reach me at 9876543210 or +91-98765-43210.
Alternate: 09876543210, +91 91234 56780, office: 022-234567.
Bad numbers: 12345, 1111111111, 555-5555, +1-202-555-0101.
"""
    pat = re.compile(r"""
        (?:
            (?:\+91[\s-]*)?      # optional +91
            (?:0[\s-]*)?         # optional leading 0
        )
        ([6-9]\d{9})            # 10 digits starting 6-9
    """, re.VERBOSE)
    found = pat.findall(text)
    seen, mobiles = set(), []
    for m in found:
        if m not in seen:
            seen.add(m)
            mobiles.append(m)
    print("Mobiles found:", mobiles)

if __name__ == "__main__":
    main()
