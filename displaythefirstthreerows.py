
#2879
#easy

#Write a solution to display the first 3 rows of this DataFrame.


#correct python3 solution (could not solve):

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
