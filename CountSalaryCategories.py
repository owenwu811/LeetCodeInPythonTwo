
#1907
#medium

#Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

#"Low Salary": All the salaries strictly less than $20000.
#"Average Salary": All the salaries in the inclusive range [$20000, $50000].
#"High Salary": All the salaries strictly greater than $50000.
#The result table must contain all three categories. If there are no accounts in a category, return 0.

#Return the result table in any order.

#The result format is in the following example.


#my own solution using python3:

#make sure to subsitute if any category is missing as 0

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(int)
    for i, a in enumerate(accounts["income"]):
        if a < 20000:
            d["Low Salary"] += 1
        elif 20000 <= a <= 50000:
            d["Average Salary"] += 1
        elif a > 50000:
            d["High Salary"] += 1
    one, two = [], []
    if "Low Salary" not in d:
        d["Low Salary"] = 0
    if "Average Salary" not in d:
        d["Average Salary"] = 0
    if "High Salary" not in d:
        d["High Salary"] = 0
    for k in d:
        one.append(k)
        two.append(d[k])
    res = pd.DataFrame()
    res["category"] = one
    res["accounts_count"] = two
    return res
