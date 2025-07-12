
#1990
#medium

#Write a solution to report the number of experiments done on each of the three platforms for each of the three given experiments. Notice that all the pairs of (platform, experiment) should be included in the output including the pairs with zero experiments.

#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#make sure all combinations of activities and platforms are considered 

import pandas as pd

def count_experiments(experiments: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(int)
    ee = ["Reading", "Sports", "Programming"]
    vv = ["IOS", "Web", "Android"]
    for i, e in enumerate(experiments["platform"]):
        en = experiments["experiment_name"][i]
        #ee.append(experiments["experiment_name"][i])
        #vv.append(e)
        d[(e, en)] += 1
    for y in ee:
        for h in vv:
            if (h, y) not in d:
                d[(h, y)] = 0
    print(d)
    one, two, three = [], [], []
    for k in d:
        one.append(k[0])
        two.append(k[1])
        three.append(d[k])
    res = pd.DataFrame()
    res["platform"] = one
    res["experiment_name"] = two
    res["num_experiments"] = three
    return res
