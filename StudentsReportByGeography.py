#618
#Hard

#A school has students from Asia, Europe, and America.

#Write a solution to pivot the continent column in the Student table so that each name is sorted alphabetically and displayed underneath its corresponding continent. The output headers should be America, Asia, and Europe, respectively.

#The test cases are generated so that the student number from America is not less than either Asia or Europe.

#The result format is in the following example.



#my own solution using python3:

#literally just follow the instructions

import pandas as pd

def geography_report(student: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    size = -1
    for i, v in enumerate(student["continent"]):
        d[v].append(student["name"][i])
        d[v].sort()
        size = max(size, len(d[v]))
    print(d)
    print(size)
    student["America"] = None
    student["Asia"] = None
    student["Europe"] = None
    for k in d:
        cnt = 0
        for a in d[k]:
            student[k][cnt] = a
            cnt += 1
        
        

    return pd.DataFrame(student, columns=["America", "Asia", "Europe"]).head(size)
