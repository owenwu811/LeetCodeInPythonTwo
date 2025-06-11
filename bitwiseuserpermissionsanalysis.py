
#3204
#medium

#Consider that each bit in the permissions integer represents a different access level or feature that a user has.

#Write a solution to calculate the following:

#common_perms: The access level granted to all users. This is computed using a bitwise AND operation on the permissions column.
#any_perms: The access level granted to any user. This is computed using a bitwise OR operation on the permissions column.
#Return the result table in any order.

#The result format is shown in the following example.


#my own solution using python3:

#just do exactly what they say - no tricks

import pandas as pd

def analyze_permissions(user_permissions: pd.DataFrame) -> pd.DataFrame:
    cp, ap = user_permissions["permissions"][0], user_permissions["permissions"][0]
    for i in range(1, len(user_permissions["permissions"])):
        cp = cp & user_permissions["permissions"][i]
        ap = ap | user_permissions["permissions"][i]

    user_permissions["common_perms"] = cp
    user_permissions["any_perms"] = ap
    return pd.DataFrame(user_permissions, columns=["common_perms", "any_perms"]).head(1)
