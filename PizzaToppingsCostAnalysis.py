
#3050
#medium

#Write a solution to calculate the total cost of all possible 3-topping pizza combinations from a given list of toppings. The total cost of toppings must be rounded to 2 decimal places.

#Note:

#Do not include the pizzas where a topping is repeated. For example, ‘Pepperoni, Pepperoni, Onion Pizza’.
#Toppings must be listed in alphabetical order. For example, 'Chicken, Onions, Sausage'. 'Onion, Sausage, Chicken' is not acceptable.
#Return the result table ordered by total cost in descending order and combination of toppings in ascending order.

#The result format is in the following example.

#my own solution using python3:

#generate all unique permutations

import pandas as pd

def cost_analysis(toppings: pd.DataFrame) -> pd.DataFrame:
    cur = []
    d = dict()
    
    for i, t in enumerate(toppings["topping_name"]):
        cur.append(t) 
        d[t] = toppings["cost"][i]
    used = []
    ans = []
    for a in permutations(cur, 3):
        now = list(sorted(a))
        tot = 0
        if now not in used:
            k = sorted(a)
            for thing in k:
                tot += d[thing]
            tot = round(tot, 2)
            ans.append([k, tot])

        used.append(now.copy())
    ans.sort(key=lambda x: (-x[1], x[0]))
    print(ans)
    one, two = [], []
    for a in ans:
        one.append(",".join(a[0]))
        two.append(a[1])
    res = pd.DataFrame()
    res["pizza"] = one
    res["total_cost"] = two
    return res
