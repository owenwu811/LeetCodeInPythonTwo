#3059
#easy

#Write a solution to find all unique email domains and count the number of individuals associated with each domain. Consider only those domains that end with .com.

#Return the result table orderd by email domains in ascending order.

#The result format is in the following example.

#my own solution using python3:

#tallup all domains ending in .com, and then use a hashmap to count the frequency with the part before @trimmed off, and then sort and gather the data

import pandas as pd

def find_unique_email_domains(emails: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(int)
    for i, e in enumerate(emails["email"]):
        if e.endswith(".com"):
            print(e)
            idx = e.index("@")
            d[e[idx + 1:]] += 1
    print(d)
    ans = []
    for a, b in d.items():
        ans.append([a, b])
    ans.sort(key=lambda x: (x[0]))
    one, two = [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
    res = pd.DataFrame()
    res["email_domain"] = one
    res["count"] = two
    return res

