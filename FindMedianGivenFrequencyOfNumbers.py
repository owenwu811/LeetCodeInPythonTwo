
#571
#Hard

#The median is the value separating the higher half from the lower half of a data sample.

#Write a solution to report the median of all the numbers in the database after decompressing the Numbers table. Round the median to one decimal point.

#The result format is in the following example.




#my own solution using python3:

#literally just use the median function

import pandas as pd

def median_frequency(numbers: pd.DataFrame) -> pd.DataFrame:
    cur = []
    for i, v in enumerate(numbers["num"]):
        val = numbers["frequency"][i]
        while val > 0:
            cur.append(v)
            val -= 1
    print(cur)
    print(median(cur))
    numbers["median"] = median(cur)
    return pd.DataFrame(numbers, columns=["median"]).head(1)
