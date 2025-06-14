
#2738
#medium

#Write a solution to find the number of files that have at least one occurrence of the words 'bull' and 'bear' as a standalone word, respectively, disregarding any instances where it appears without space on either side (e.g. 'bullet', 'bears', 'bull.', or 'bear' at the beginning or end of a sentence will not be considered) 

#Return the word 'bull' and 'bear' along with the corresponding number of occurrences in any order.

#The result format is in the following example.




#my own solution using python3:

#how many rows bull or bear appear in

import pandas as pd

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(int)
    d["bull"] = 0
    d["bear"] = 0
    for a in files["content"]:
        print(a.split(" "))
        if "bull" in a.split(" ")[1:-1]:
            d["bull"] += 1
        if "bear" in a.split(" ")[1:-1]:
            d["bear"] += 1
    files["word"] = files["file_name"]
    files["count"] = files["file_name"]
    a = list(d.items())
    #print(a)
    #print(files)
    for i, v in enumerate(files["word"]):
        if i < len(a):
            files["word"][i] = a[i][0]
            files["count"][i] = a[i][1]
    return pd.DataFrame(files, columns=["word", "count"]).head(2)
