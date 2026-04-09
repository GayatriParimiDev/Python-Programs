
# Task 15: Find all email addresses out of a long text.

import re

def main():
    text = """
Emails: a@iitb.ac.in, test.user+lab@domain.co.in, bad@@mail, name@localhost,
first.last@sub.domain.com, x@y.z, spaced @bad.com, z_o-o@ex-ample.org
"""
    email_pat = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
    emails = email_pat.findall(text)
    seen, uniq = set(), []
    for e in emails:
        if e not in seen:
            seen.add(e)
            uniq.append(e)
    print("Emails found:", uniq)

if __name__ == "__main__":
    main()
