#1341
#medium

#Write a solution to:

#Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
#Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.
#The result format is in the following example.

#my own solution using python3:

#messy but working solution - do exactly as asked

import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    c = Counter(movie_rating["user_id"])
    biggest = max(c.values())
    d = dict()
    names = []
    for i, u in enumerate(users["user_id"]):
        d[u] = users["name"][i]
    for a, b in c.items():
        if b == biggest: names.append(d[a])
    names.sort()

    print(names)
    feb = []
    rat = defaultdict(list)
    for i, m in enumerate(movie_rating["created_at"]):
        cur = str(m).split(" ")[0]
        #print(cur)
        first = cur[:7]
        #print(first)
        if cur[:7] == "2020-02":
            rat[movie_rating["movie_id"][i]].append(movie_rating["rating"][i])
    biggestmean = -1
    for r in rat:
        #print(r, rat[r])

        curmean = sum(rat[r]) / len(rat[r])
        #print(curmean)
        biggestmean = max(biggestmean, curmean)
    md = dict()
    for i, m in enumerate(movies["movie_id"]):
        md[m] = movies["title"][i]
    two = []
    for r in rat:
        cur = sum(rat[r]) / len(rat[r])
        if cur == biggestmean:
            #print(r)
            two.append(md[r])
    two.sort()
    print(two)
    ans = []
    if names:
        ans.append(names[0])
    if two:
        ans.append(two[0])
    res = pd.DataFrame()
    res["results"] = ans
    return res
    
