#3586
#medium

#Write a solution to find patients who have recovered from COVID - patients who tested positive but later tested negative.

#A patient is considered recovered if they have at least one Positive test followed by at least one Negative test on a later date
#Calculate the recovery time in days as the difference between the first positive test and the first negative test after that positive test
#Only include patients who have both positive and negative test results
#Return the result table ordered by recovery_time in ascending order, then by patient_name in ascending order.

#The result format is in the following example.

#my own solution using python3:

#gather all the test results for each patient id, and then find the positive then negative pattern after sorting each value list by the timestamp, and then do the conversion back without duplicate patient ids in the answer

import pandas as pd

def find_covid_recovery_patients(patients: pd.DataFrame, covid_tests: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, c in enumerate(covid_tests["patient_id"]):
        #if covid_tests["result"][i] == "Positive":
        d[c].append([covid_tests["test_date"][i], covid_tests["result"][i]])
    name = dict()
    age = dict()
    for i, p in enumerate(patients["patient_id"]): 
        name[p] = patients["patient_name"][i] 
        age[p] = patients["age"][i]

    ans = []
    seen = set()
    for k in d:
        for j, a in enumerate(d[k]):
            if a[1] == "Positive":
                start = a[0]
                for i in range(j + 1, len(d[k])):
                    if d[k][i][-1] == "Negative":
                        diff = pd.to_datetime(d[k][i][0]) - pd.to_datetime(start)
                        #print(k, diff)
                        now = str(diff).split(" ")[0]
                        if k not in seen:
                            ans.append([k, name[k], age[k], int(now)])
                            seen.add(k)
                            break
    ans.sort(key=lambda x: (x[-1], x[1]))
    print(ans)
    one, two, three, four = [], [], [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
        three.append(a[2])
        four.append(a[3])
    res = pd.DataFrame()
    res["patient_id"] = one
    res["patient_name"] = two
    res["age"] = three
    res["recovery_time"] = four
    return res
    
