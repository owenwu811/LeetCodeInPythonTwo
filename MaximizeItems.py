#3052
#Hard

#Leetcode warehouse wants to maximize the number of items it can stock in a 500,000 square feet warehouse. It wants to stock as many prime items as possible, and afterwards use the remaining square footage to stock the most number of non-prime items.

#Write a solution to find the number of prime and non-prime items that can be stored in the 500,000 square feet warehouse. Output the item type with prime_eligible followed by not_prime and the maximum number of items that can be stocked.

#Note:

#Item count must be a whole number (integer).
#If the count for the not_prime category is 0, you should output 0 for that particular category.
#Return the result table ordered by item count in descending order.

#The result format is in the following example.


#my own solution using python3:

#use rounding and sorting and try to find the threshold using a loop

import pandas as pd

def maximize_items(inventory: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, v in enumerate(inventory["item_id"]):
        if inventory["item_type"][i] == "prime_eligible":
            d['p'].append(inventory["square_footage"][i])
        else:
            d['np'].append(inventory["square_footage"][i])
    size = 500000
    tot = sum(d["p"])
    big = float('-inf')
    for i in range(10000):
        if tot * i > 500000:
            #print(i)
            big = i - 1
            break
    ans = dict()
    if big != float('-inf'):
        print(tot, big)
        to = round(tot * big)
        ans["prime_eligible"] = len(d["p"]) * big
        size -= to
    print(size)
    tot = sum(d["np"])
    nextb = float('-inf')
    for i in range(10000):
        if tot * i > size:
            nextb = i - 1
            break
    if nextb != float('-inf'):
        ans["not_prime"] = len(d["np"]) * nextb
    print(ans)
    ans = list(ans.items())
    ans.sort(key=lambda x: x[1], reverse=True)
    print(ans)
    one, two = [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
    pdd = pd.DataFrame()
    pdd["item_type"] = one
    pdd["item_count"] = two
    return pdd
    
