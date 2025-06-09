
#2882
#easy

#There are some duplicate rows in the DataFrame based on the email column.

#Write a solution to remove these duplicate rows and keep only the first occurrence.

#The result format is in the following example.

#my own solution using python3:

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates('email')
