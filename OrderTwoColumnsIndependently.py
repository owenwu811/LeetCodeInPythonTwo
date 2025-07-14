#2159
#medium

#Write a solution to independently:

#order first_col in ascending order.
#order second_col in descending order.
#The result format is in the following example.

#my own solution using python3:

#just sort the first list and then the second list in reverse order

import pandas as pd

def order_two_columns(data: pd.DataFrame) -> pd.DataFrame:
    one, two = [], []
    for i, d in enumerate(data["first_col"]):
        one.append(d)
        two.append(data["second_col"][i])
    one.sort()
    two.sort(reverse=True)
    res = pd.DataFrame()
    res["first_col"] = one
    res["second_col"] = two
    return res
