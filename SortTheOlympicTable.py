#2377
#easy

#The Olympic table is sorted according to the following rules:

#The country with more gold medals comes first.
#If there is a tie in the gold medals, the country with more silver medals comes first.
#If there is a tie in the silver medals, the country with more bronze medals comes first.
#If there is a tie in the bronze medals, the countries with the tie are sorted in ascending order lexicographically.
#Write a solution to sort the Olympic table.

#The result format is shown in the following example.

#my own solution using python3:

import pandas as pd

def sort_table(olympic: pd.DataFrame) -> pd.DataFrame:
    ans = []
    for i, o in enumerate(olympic["country"]):
        ans.append([o, olympic["gold_medals"][i], olympic["silver_medals"][i], olympic["bronze_medals"][i]])
        ans.sort(key=lambda x: (-x[1], -x[2], -x[3], x[0]))
    print(ans)
    one, two, three, four = [], [], [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
        three.append(a[2])
        four.append(a[3])
    res = pd.DataFrame()
    res["country"] = one
    res["gold_medals"] = two
    res["silver_medals"] = three
    res["bronze_medals"] = four
    return res
