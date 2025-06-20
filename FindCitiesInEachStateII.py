
#3328
#medium


#Write a solution to find all the cities in each state and analyze them based on the following requirements:

#Combine all cities into a comma-separated string for each state.
#Only include states that have at least 3 cities.
#Only include states where at least one city starts with the same letter as the state name.
#Return the result table ordered by the count of matching-letter cities in descending order and then by state name in ascending order.

#The result format is in the following example.

#my own solution using python3:

#follow the directions

import pandas as pd

def state_city_analysis(cities: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, v in enumerate(cities["state"]):
        d[v].append(cities["city"][i])
    #print(d)
    ad = defaultdict(list)
    for k in d:
        if len(d[k]) >= 3:
            flag = False
            for a in d[k]:
                if k[0] == a[0]:
                    flag = True
                    break
            if flag:
                ad[k] = d[k]
    #print(ad)
    ans = []
    for a in ad:
        cnt = 0
        for b in ad[a]:
            if a[0] == b[0]:
                cnt += 1
        #print(a, ad[a], cnt)
        ans.append([cnt, sorted(ad[a]), a])
        #ans.append([a, sorted(ad[a]), cnt])
    #print(ans)
    ans.sort(reverse=True)
    print(ans)
    cities["cities"] = cities["city"]
    cities["matching_letter_count"] = 0
    cnt = 0
    for a in ans:
        cities["state"][cnt] = a[-1]
        cities["cities"][cnt] = ", ".join(a[1])
        cities["matching_letter_count"][cnt] = a[0]
        cnt += 1

    return pd.DataFrame(cities, columns=["state", "cities", "matching_letter_count"]).head(len(ans))

        
