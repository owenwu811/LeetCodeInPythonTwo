#596
#easy

#Write a solution to find all the classes that have at least five students.

#Return the result table in any order.

#The result format is in the following example.


#my own solution using python3:

#use a hashmap and append every student for that course, and loop through the dictionary and check the size of the key's list to determine if valid or not

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, c in enumerate(courses["class"]):
        d[c].append(courses["student"][i])
    ans = []
    for k in d:
        if len(d[k]) >= 5:
            ans.append(k)
    res = pd.DataFrame()
    res["class"] = ans
    return res
