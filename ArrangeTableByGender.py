#2308
#medium

#Write a solution to rearrange the Genders table such that the rows alternate between 'female', 'other', and 'male' in order. The table should be rearranged such that the IDs of each gender are sorted in ascending order.

#Return the result table in the mentioned order.

#The result format is shown in the following example.

#my own solution using python3:

#use the gender as the key, and get all the ids for that gender, and then sort all the ids for each gender, and then keep popping in the female, other, male order one at a time until you can't

import pandas as pd

def arrange_table(genders: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, g in enumerate(genders["gender"]):
        d[g].append(genders["user_id"][i])
        d[g].sort()
    one, two = [], []
    while d["female"] and d["male"] and d["other"]:
        if d["female"]:
            print(d["female"][0], "female")
            one.append(d["female"][0])
            two.append("female")
            del d["female"][0]
        if d["other"]:
            print(d["other"][0], "other")
            one.append(d["other"][0])
            two.append("other")
            del d["other"][0]
        if d["male"]:
            print(d["male"][0], "male")
            one.append(d["male"][0])
            two.append("male")
            del d["male"][0]

    res = pd.DataFrame()
    res["user_id"] = one
    res["gender"] = two
    return res
